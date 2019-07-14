from fb_app.models import UserInfo
from fb_graph_api.config import *


class UserInfoDBUtils:
    def get_or_create_user_object(self,user_id):
        query_set = UserInfo.objects.filter(user_id=user_id)
        if len(query_set) == 0:
            self.user = UserInfo(user_id=user_id)
            return self.user
        else:
            self.user = query_set[0]
            return self.user

    def insert_or_update_user_info_in_DB(self,access_token,access_token_info):
        user_id = access_token_info['data']['user_id']
        self.get_or_create_user_object(user_id)
        self.user.access_token = access_token
        self.user.issued_at = access_token_info['data']['issued_at']
        self.user.data_access_expires_at = access_token_info['data']['data_access_expires_at']
        self.user.token_expires_at = access_token_info['data']['expires_at']
        self.user.scopes = ','.join(access_token_info['data']['scopes'])
        self.user.save()

        return self.user.user_id