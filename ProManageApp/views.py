import json
from datetime import datetime, timedelta

from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from ProManageApp.models import Users


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


@csrf_exempt
def login_with_username(request):
    username = ''
    try:
        UserDetails = request.POST['UserDetails']
        u_data = json.loads(UserDetails)
        username = u_data.get('username')
        password = u_data.get('password')
        response, session = login_with_username_service(username, password)
        request.session['username'] = session['username']
        request.session['u_id'] = session['u_id']
        request.session.set_expiry(5000)
        session_expiry_seconds = 5000
        request.session.set_expiry(session_expiry_seconds)
        expiry_timestamp = datetime.now() + timedelta(seconds=session_expiry_seconds)
        request.session['session_expiry_time'] = expiry_timestamp.isoformat()
        return JsonResponse(response)
    except Exception as e:
        print("Exception in login_with_username : ", e)
        return HttpResponse(json.dumps({"result": "error", "msg": "login error."}), content_type="application/json")

def login_with_username_service(username, password):
    try:
        session = {'username': '', 'u_id': ''}
        if username:
            try:
                validate_user = Users.objects.get(u_username=username,
                                                  u_password=password)

            except Users.DoesNotExist:
                validate_user = None

            if validate_user != None:
                u_id = validate_user.u_id

                session['username'] = validate_user.u_username
                session['u_id'] = validate_user.u_id

                return {"result": "valid", "u_id": u_id}, session
            else:
                return {"result": "Invalid", "msg": "Invalid User credentials."}, session
        else:
            return {"result": "Invalid", "msg": "Invalid Username."}
    except Exception as e:
        return {"result": "error", "msg": "login error."}