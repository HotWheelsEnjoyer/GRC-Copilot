from django.db import models
from django.contrib.auth.models import User

class Policy(models.Model):
    policy_id = models.CharField(max_length=50, unique=True)
    policy_name = models.CharField(max_length=255)
    policy_code = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    action_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="owned_policies")
    action_teams = models.ManyToManyField(User, related_name="policy_teams")
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Control(models.Model):
    control_id = models.CharField(max_length=50, unique=True)
    control_name = models.CharField(max_length=255)
    control_code = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    function_group = models.CharField(max_length=100)
    action_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="owned_controls")
    action_teams = models.ManyToManyField(User, related_name="control_teams")
    status = models.CharField(max_length=50)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Evidence(models.Model):
    evidence_id = models.CharField(max_length=50, unique=True)
    evidence_code = models.CharField(max_length=50)
    department = models.CharField(max_length=30)
    controls = models.ManyToManyField(Control,related_name="evidence_controls")
    action_owner = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name="evidence_owner")
    action_teams = models.ManyToManyField(User,related_name="evidence_teams")
    status = models.CharField(max_length=50)