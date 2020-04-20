import os, sys
import django


sys.path.append('../s3boto_exercise')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 's3boto_exercise.settings')
django.setup()

from django.db import IntegrityError
from django.contrib.auth.models import User


def create_root_user():
    print('\n')
    print('>> Creating Root User ...')

    try:
        root_user = User.objects.create(
            username='root',
            email='',
            is_superuser=True,
            is_staff=True
        )

        root_user.set_password('p@ssw0rD')
        root_user.save()

        print('>> DONE!' if root_user else '>> ERROR')

    except IntegrityError as e:
        print('>> ERROR: create_root_user()')
        print(e)


if __name__ == '__main__':
    create_root_user()
