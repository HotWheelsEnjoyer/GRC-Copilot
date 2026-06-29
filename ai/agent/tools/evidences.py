import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../backend'))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from grc.models import Evidence
from langchain.tools import tool

@tool
def get_evidences(
    evidence_id: str = None,
    evidence_code: str = None,
    department: str = None,
    action_owner: str = None,
    action_teams: str = None,
    status: str = None,
    controls: str = None
):
    """Get evidence records with flexible filtering"""
    try:
        print("DEBUG: Starting get_evidences")
        query = Evidence.objects.all()
        print(f"DEBUG: Query created, count: {query.count()}")
        
        if evidence_id:
            query = query.filter(evidence_id=evidence_id)
        if evidence_code:
            query = query.filter(evidence_code__icontains=evidence_code)
        if department:
            query = query.filter(department=department)
        if action_owner:
            query = query.filter(action_owner__username=action_owner)
        if action_teams:
            query = query.filter(action_teams__username=action_teams)
        if status:
            query = query.filter(status=status)
        if controls:
            query = query.filter(controls__control_id=controls)
        
        print(f"DEBUG: About to get values, query count: {query.count()}")
        results = list(query.values(
            'evidence_id',
            'evidence_code',
            'department',
            'status',
            'action_owner__username'
        ).distinct())
        
        print(f"DEBUG: Got {len(results)} results")
        
        if not results:
            return "No evidence found"
        
        output = "Evidence:\n"
        for r in results:
            owner = r['action_owner__username'] or "Unassigned"
            output += f"- {r['evidence_id']} ({r['evidence_code']}): Dept: {r['department']} | "
            output += f"Owner: {owner} | Status: {r['status']}\n"
        
        return output
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Error: {str(e)}"