import os
import uuid
from datetime import datetime as dt

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet

from storage.models import StoreFile, Store
from utils.s3_helper import S3Helper

FILE_TYPES = {
    'pdf': 'application/pdf',
    'zip': 'applicaion/zip',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'svg': 'image/svg+xml',
    'txt': 'text/plain',
    'mp4': 'video/mp4',
    'mpeg': 'audio/mpeg',
}


class StoreViewSet(ViewSet):
    permission_classes = []
    authentication_classes = []

    @staticmethod
    def list(request, *args, **kwargs):
        print(args)
        print(kwargs)
        return Response(HTTP_200_OK, status=HTTP_200_OK)

    @staticmethod
    def retrieve(request, pk=None, *args, **kwargs):
        print(args)
        print(kwargs)
        return Response(HTTP_200_OK, status=HTTP_200_OK)

    @action(methods=["POST"], detail=True)
    def upload(self, request, pk=None, *args, **kwargs):
        multipart_file = request.data.get("multipart_file")
        store_file = StoreFile(file_obj=multipart_file)
        store_file.store = Store(pk=pk)
        store_file.save()

        file_path = store_file.file_obj.path
        file_size = store_file.file_obj.size

        if file_path and not file_path == "":
            orig_filename = file_path
            filename = orig_filename.split("/")[-1].lower()
            file_ext = filename.split(".")[-1]
            filename_hash = '{}.{}'.format(uuid.uuid4(), file_ext)
            folder = 'dev_public/test'
            upload_request = S3Helper.upload_file(orig_filename, folder, filename_hash)

            if upload_request.get("status") == 200:
                # Delete created file object in disk
                store_file.file_obj.delete()

                # Update store_file
                store_file.storage_url = upload_request.get("upload_url")
                store_file.filename = filename_hash
                store_file.file_size = file_size
                store_file.content_type = FILE_TYPES[file_ext]
                store_file.save()

                return Response({
                    "status": HTTP_200_OK,
                    "store_file": store_file.to_json()
                }, status=HTTP_200_OK)

        return Response({"status": HTTP_400_BAD_REQUEST}, status=HTTP_400_BAD_REQUEST)


class StoreFileViewSet(ViewSet):
    permission_classes = []
    authentication_classes = []

    @staticmethod
    def list(request, store_pk=None, *args, **kwargs):
        print(args)
        print(kwargs)
        return Response(HTTP_200_OK, status=HTTP_200_OK)

    @staticmethod
    def retrieve(request, store_pk=None, pk=None, *args, **kwargs):
        print(args)
        print(kwargs)
        return Response(HTTP_200_OK, status=HTTP_200_OK)

    @staticmethod
    def create(request, store_pk=None, *args, **kwargs):
        print(args)
        print(kwargs)
        return Response(HTTP_200_OK, status=HTTP_200_OK)

    @staticmethod
    def destroy(request, store_pk=None, pk=None, *args, **kwargs):
        print(args)
        print(kwargs)
        return Response(HTTP_200_OK, status=HTTP_200_OK)
