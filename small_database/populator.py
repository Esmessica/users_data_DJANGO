import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'small_database.settings')

import django

django.setup()
from user_app.models import User
from faker import Faker
from random import randint

fakegen = Faker()


def populate(n=5):
    for entry in range(n):
        fake_name = fakegen.name()
        fake_email = fakegen.email()
        rand_age = randint(18, 85)
        user = User.objects.get_or_create(user_name=fake_name, email=fake_email, age=rand_age)[
            0]


if __name__ == '__main__':
    print('Populating database')
    populate(25)
    print('All done')
