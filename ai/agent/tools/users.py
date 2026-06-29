import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../backend'))

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User 
from langchain.tools import tool

@tool
def get_users(
    username: str = None,
    email: str = None,
    first_name: str = None,
    last_name: str = None,
    is_staff: bool = None
):
    """Get users with flexible filtering"""
    try:
        print("DEBUG: Starting get_users")
        query = User.objects.all()
        print(f"DEBUG: Query created, count: {query.count()}")
        
        if username:
            query = query.filter(username__icontains=username)
        if email:
            query = query.filter(email__icontains=email)
        if first_name:
            query = query.filter(first_name__icontains=first_name)
        if last_name:
            query = query.filter(last_name__icontains=last_name)
        if is_staff is not None:
            query = query.filter(is_staff=is_staff)
        
        print(f"DEBUG: About to get values, query count: {query.count()}")
        results = list(query.values('id', 'username', 'email', 'first_name', 'last_name', 'is_active'))
        
        print(f"DEBUG: Got {len(results)} results")
        
        if not results:
            return "No users found"
        
        output = "Users:\n"
        for r in results:
            active_status = "Active" if r['is_active'] else "Inactive"
            output += f"- {r['username']}: {r['first_name']} {r['last_name']} ({r['email']}) | {active_status}\n"
        
        return output
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Error: {str(e)}"