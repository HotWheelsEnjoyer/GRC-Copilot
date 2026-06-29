from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from grc.models import Control, Policy
from faker import Faker

class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        users = User.objects.all()[:5]
        policies = Policy.objects.all()
        
        control_ids = ["AC-2", "AC-3", "AC-6", "AU-2", "AU-12", "SC-7", "SC-28"]
        
        for control_id in control_ids:
            control = Control.objects.get_or_create(
                control_id=control_id,
                defaults={
                    "control_name": fake.sentence(nb_words=3),
                    "control_code": f"CODE-{control_id}",
                    "department": fake.random_element(["IT", "Security", "Compliance"]),
                    "function_group": fake.random_element(["Access", "Audit", "Encryption"]),
                    "action_owner": fake.random_element(users) if users else None,
                    "status": fake.random_element(["gap", "implemented", "partial"]),
                    "policy": fake.random_element(policies) if policies else None
                }
            )[0]
            
            if users:
                control.action_teams.add(*users[:3])
        
        self.stdout.write("✓ Controls created")