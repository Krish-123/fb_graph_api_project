from fb_graph_api.config import *
import requests
from datetime import datetime

def get_access_token(code):
    redirect_uri = 'http://localhost:8080/fbapp/postlogin/'
    response = requests.get(fb_end_point_for_code_exchange.format(app_id,redirect_uri,app_secret,code))
    access_token = response.json()['access_token']
    with open('access_token.txt','w') as file:
        file.write(access_token)

    # Getting the expiration date
    # print(datetime.timestamp(datetime.now()))
    # expires_at = datetime.fromtimestamp(datetime.timestamp(datetime.now()) + response.json()['expires_in'])
    # print(expires_at)

    return access_token