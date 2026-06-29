import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../backend'))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from grc.models import Control
from langchain.tools import tool

@tool
def get_controls(
    control_id: str = None,
    control_name: str = None,
    control_code: str = None,
    department: str = None,
    function_group: str = None,
    action_owner: str = None,
    action_teams: str = None,
    status: str = None,
    policy_id: str = None,
    created_at: str = None
):
    """Get security controls with flexible filtering"""
    try:
        print("DEBUG: Starting get_controls")
        query = Control.objects.all()
        print(f"DEBUG: Query created, count: {query.count()}")
        
        if control_id:
            print(f"DEBUG: Filtering by control_id: {control_id}")
            query = query.filter(control_id=control_id)
        if control_name:
            print(f"DEBUG: Filtering by control_name: {control_name}")
            query = query.filter(control_name__icontains=control_name)
        if department:
            print(f"DEBUG: Filtering by department: {department}")
            query = query.filter(department=department)
        
        print(f"DEBUG: About to get values, query count: {query.count()}")
        results = list(query.values('control_id', 'control_name', 'status').distinct())
        print(f"DEBUG: Got {len(results)} results")
        
        if not results:
            return "No controls found"
        
        output = "Controls:\n"
        for r in results:
            output += f"- {r['control_id']}: {r['control_name']}\n"
        
        return output
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Error: {str(e)}"