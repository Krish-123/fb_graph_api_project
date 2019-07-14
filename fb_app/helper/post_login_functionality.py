from fb_app.helper.fb_oauth_utlis import FbUtils
from fb_app.helper.user_info_db_utils import UserInfoDBUtils


def post_login_functionality(code):
    # Exchanging access token for code
    fb_utils = FbUtils()
    access_token = fb_utils.get_access_token(code)
    # Getting access token info using inspection url
    access_token_info = fb_utils.inspect_access_token(access_token)

    if not access_token_info:
        return {'status':'Login failed'}
    # Updating the UserInfo table with user data from access token
    user_info_db_utils = UserInfoDBUtils()
    user_info_db_utils.insert_or_update_user_info_in_DB(access_token,access_token_info)

    return access_token_info