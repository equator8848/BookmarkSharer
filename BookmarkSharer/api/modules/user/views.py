from ..util import github_login_helper
import logging


def github_login_callback(req):
    code = req.GET.get('code')
    logging.debug(code)
    token = github_login_helper.access_token(code)
    logging.debug(token)
    user_info = github_login_helper.get_user_info(token)
    logging.debug(user_info)
