from fb_graph_api.config import *
import requests
from fb_app.models import UserInfo

class FbUtils:
    def get_access_token(self,code):
        response = requests.get(fb_end_point_for_code_exchange.format(app_id,login_redirect_uri,app_secret,code))
        access_token = response.json()['access_token']

        # Getting the expiration date
        # print(datetime.timestamp(datetime.now()))
        # expires_at = datetime.fromtimestamp(datetime.timestamp(datetime.now()) + response.json()['expires_in'])
        # print(expires_at)

        return access_token

    def inspect_access_token(self,access_token):
        response = requests.get(fb_end_pont_for_token_inspection.format(access_token,app_token))
        if response.status_code == 200:
            return response.json()
        return False