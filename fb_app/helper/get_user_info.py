from fb_graph_api.config import *
from fb_app.models import UserInfo
import requests


fields = 'id,name,email,birthday,gender'

def get_user_info(user_id):
    user = UserInfo.objects.get(user_id=user_id)

    response = requests.get(fb_end_point_for_user_info.format(user.user_id,fields,user.access_token))
    return response.json()