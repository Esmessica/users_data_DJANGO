import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'small_database.settings')
import django

django.setup()
from user_app.models import UserProfileInfo
from django.contrib.auth.models import User
from faker import Faker

fakegen = Faker()
def populate(n=5):
    for entry in range(n):
        fake_name = fakegen.name()
        fake_email = fakegen.email()

        # Create a User instance
        user = User.objects.get_or_create(username=fake_name, email=fake_email)[0]
        user.set_password(fake_name)  # Set the password using set_password
        user.save()

        # Create a UserProfileInfo instance and associate with the user
        user_profile = UserProfileInfo.objects.create(user=user, personal_site=fakegen.url(), profile_pic='')


if __name__ == '__main__':
    print('Populating database')
    populate(25)
    print('All done')
