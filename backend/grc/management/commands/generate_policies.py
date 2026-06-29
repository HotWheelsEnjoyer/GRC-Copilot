from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from grc.models import Policy
from faker import Faker

class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        users = User.objects.all()[:5]
        
        policies_data = [
            ("POL-001", "Data Protection Policy"),
            ("POL-002", "Access Control Policy"),
            ("POL-003", "Security Policy"),
            ("POL-004", "Incident Response Policy"),
        ]
        
        for policy_id, policy_name in policies_data:
            policy = Policy.objects.get_or_create(
                policy_id=policy_id,
                defaults={
                    "policy_name": policy_name,
                    "policy_code": f"CODE-{policy_id}",
                    "department": fake.random_element(["IT", "Security", "Compliance"]),
                    "action_owner": fake.random_element(users) if users else None,
                    "status": fake.random_element(["active", "draft", "archived"])
                }
            )[0]
            
            if users:
                policy.action_teams.add(*users[:3])
        
        self.stdout.write("✓ Policies created")