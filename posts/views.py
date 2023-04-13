from django.shortcuts import HttpResponse
from datetime import datetime

# Create your views here.

'''NVC - MODEL VIEW CONTROLLER'''

def frist_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")

def second_view(requst):
    if requst.method == 'GET':
        return HttpResponse(f"{datetime.today()}")

def third_view(requst):
    if requst.method == 'GET':
        return HttpResponse(f"baibai")

