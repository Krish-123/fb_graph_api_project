from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from fb_app.helper.fb_utlis import FbUtils
from fb_app.helper.user_info_db_utils import UserInfoDBUtils
from fb_app.helper.post_login_functionality import post_login_functionality
from fb_graph_api.config import *


# Create your views here.

def fb_login(request):
    return HttpResponseRedirect(fb_login_dialog.format(app_id,login_redirect_uri,state,resonse_type,fb_access_permissions))


def login(request):
    return render(request,'fb_app/login_page.html',{})


def login_redirect(request):
    get_params = request.GET
    code = get_params['code']
    access_token_info = post_login_functionality(code)
    return JsonResponse(access_token_info,safe=False)


def access_token(request):
    user_object = UserInfoDBUtils()
    return HttpResponse(user_object.insert_or_update_user_info_in_DB())