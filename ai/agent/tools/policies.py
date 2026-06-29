import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../backend'))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from grc.models import Policy
from langchain.tools import tool

@tool
def get_policies(
    policy_id: str = None,
    policy_name: str = None,
    policy_code: str = None,
    department: str = None,
    action_owner: str = None,
    action_teams: str = None,
    status: str = None,
    created_at: str = None
):
    """Get security policies with flexible filtering"""
    try:
        print("DEBUG: Starting get_policies")
        query = Policy.objects.all()
        print(f"DEBUG: Query created, count: {query.count()}")
        
        if policy_id:
            query = query.filter(policy_id=policy_id)
        if policy_name:
            query = query.filter(policy_name__icontains=policy_name)
        if policy_code:
            query = query.filter(policy_code=policy_code)
        if department:
            query = query.filter(department=department)
        if action_owner:
            query = query.filter(action_owner__username=action_owner)
        if action_teams:
            query = query.filter(action_teams__username=action_teams)
        if status:
            query = query.filter(status=status)
        if created_at:
            query = query.filter(created_at__gte=created_at)
        
        print(f"DEBUG: About to get values, query count: {query.count()}")
        results = list(query.values(
            'policy_id', 
            'policy_name', 
            'policy_code', 
            'department', 
            'status',
            'action_owner__username',
            'created_at'
        ).distinct())
        
        print(f"DEBUG: Got {len(results)} results")
        
        if not results:
            return "No policies found"
        
        output = "Policies:\n"
        for r in results:
            owner = r['action_owner__username'] or "Unassigned"
            output += f"- {r['policy_id']}: {r['policy_name']} ({r['policy_code']}) | "
            output += f"Dept: {r['department']} | Owner: {owner} | "
            output += f"Status: {r['status']} | Created: {r['created_at']}\n"
        
        return output
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Error: {str(e)}"