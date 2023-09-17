import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'small_database.settings')

import django

django.setup()
from user_app.models import User
from faker import Faker


fakegen = Faker()


def populate(n=5):
    for entry in range(n):
        fake_name = fakegen.name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(username=fake_name, email=fake_email, password=fake_name)[
            0]


if __name__ == '__main__':
    print('Populating database')
    populate(25)
    print('All done')
