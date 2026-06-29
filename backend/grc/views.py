from django.shortcuts import render
from django.http import JsonResponse
import sys
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from ai.agent.agent import run_agent

def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        try:
            response = run_agent(message)
        except Exception as e:
            response = f"Error: {str(e)}"
        return JsonResponse({'response': response})
    
    return render(request, 'chat/index.html')