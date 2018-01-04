import numpy as np
import pandas as pd


DEFAULT_API_VERSION = 2.6

class SlackApi(object):
    def __init__(self, access_token, **kwargs):
        '''
            @required:
                access_token
            @optional:
                api_version
                app_secret
        '''

        self.api_version = kwargs.get('api_version') or DEFAULT_API_VERSION
        self.app_secret = kwargs.get('app_secret')
        self.graph_url = 'https://slack.com/api/chat.postMessage'
        self.access_token = access_token

    @property
    def auth_args(self):
        auth_arguments = self.access_token
