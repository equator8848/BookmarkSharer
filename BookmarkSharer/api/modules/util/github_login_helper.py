from . import http_helper
from ....BookmarkSharer.SecretConfiguration import SecretConfiguration


def access_token(code):
    return http_helper.get_json('https://github.com/login/oauth/access_token', {
        'client_id': SecretConfiguration.GITHUB_CLIENT_ID.value,
        'client_secret': SecretConfiguration.GITHUB_CLIENT_SECRET.value,
        'code': code
    })['accessToken']


def get_user_info(token):
    return http_helper.get_json('https://api.github.com/user', headers={
        'Authorization': 'token ' + token
    })
