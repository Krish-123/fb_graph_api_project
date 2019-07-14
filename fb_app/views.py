from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from fb_app.helper.get_access_token import get_access_token
from fb_app.helper.inspect_access_token import inspect_access_token
from fb_graph_api.config import *

# Create your views here.

def fb_login(request):
    return HttpResponseRedirect(fb_login_dialog.format(app_id,login_redirect_uri,state,resonse_type,fb_access_permissions))

def login(request):
    return render(request,'fb_app/login_page.html',{})

def login_redirect(request):
    get_params = request.GET
    code = get_params['code']
    access_token = get_access_token(code)
    response = inspect_access_token(access_token)

    if not response:
        return JsonResponse({'status':'Login failed'})
    return JsonResponse(response,safe=False)