from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        
        for i in range(10):
            User.objects.get_or_create(
                username=f"user_{i}",
                defaults={
                    "email": f"user_{i}@company.com",
                    "first_name": fake.first_name(),
                    "last_name": fake.last_name()
                }
            )
        
        self.stdout.write("✓ Users created")