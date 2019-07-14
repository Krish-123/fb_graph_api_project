import requests
from fb_graph_api.config import *

def inspect_access_token(access_token):
    response = requests.get(fb_end_pont_for_token_inspection.format(access_token,app_token))
    if response.status_code == 200:
        return response.json()
    return False