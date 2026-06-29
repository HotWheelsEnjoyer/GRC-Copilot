from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from grc.models import Evidence, Control
from faker import Faker

class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        users = User.objects.all()[:5]
        controls = Control.objects.all()
        
        for i in range(10):
            evidence = Evidence.objects.get_or_create(
                evidence_id=f"EV-{i:03d}",
                defaults={
                    "evidence_code": f"CODE-EV-{i}",
                    "department": fake.random_element(["IT", "Security", "Compliance"]),
                    "action_owner": fake.random_element(users) if users else None,
                    "status": fake.random_element(["pending", "approved", "rejected"])
                }
            )[0]
            
            if controls:
                evidence.controls.add(*controls[:3])
            if users:
                evidence.action_teams.add(*users[:2])
        
        self.stdout.write("✓ Evidence created")