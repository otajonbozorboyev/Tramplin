import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edu_platform_api.settings')
import django

django.setup()

from apps.user_auth.models import User

User.objects.all().delete()

User.objects.create_superuser(username='admin', phone_number=998990232303, password='20012001a',birth_date='2001-01-01')

User.objects.create_superuser(username='admin', phone_number='998990232303', password='20012001a',
                              birth_date='2001-01-01')

