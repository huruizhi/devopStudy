import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devopStudy.settings")

import django

django.setup()


from django.contrib.auth.models import User


def get_user():
    for u in User.objects.all():
        print(u.email)


if __name__ == '__main__':
    get_user()