from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    try:
        return render(request, 'ProManageTemplates/index.html')
    except Exception as e:
        print("Exception at index --> ", e)
        return HttpResponseRedirect('/')
@csrf_exempt
def login(request):
    try:
        return render(request, 'ProManageTemplates/login.html')
    except Exception as e:
        print("Exception at index --> ", e)
        return HttpResponseRedirect('/')

@csrf_exempt
def managerDashboard(request):
    try:
        return render(request, 'ProManageTemplates/dashboard.html')
    except Exception as e:
        print('Exception add_invite ---> ', e, flush=True)
        return HttpResponseRedirect('/')

@csrf_exempt
def addProject(request):
    try:
        return render(request, 'ProManageTemplates/addProject.html')
    except Exception as e:
        print('Exception add_invite ---> ', e, flush=True)
        return HttpResponseRedirect('/')
