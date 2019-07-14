from fb_graph_api.config import *
import requests


class FbUtils:
    def get_access_token(self,code):
        response = requests.get(fb_end_point_for_code_exchange.format(app_id,login_redirect_uri,app_secret,code))
        access_token = response.json()['access_token']

        return access_token

    def inspect_access_token(self,access_token):
        response = requests.get(fb_end_pont_for_token_inspection.format(access_token,app_token))
        if response.status_code == 200:
            return response.json()

        return False

    def is_token_valid(self,access_token):
        access_token_info = self.inspect_access_token(access_token)
        is_valid = access_token_info['data']['is_valid']
        if is_valid is 'true':
            return True

        return False