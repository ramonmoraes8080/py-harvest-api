import os
import json
try:
    import ConfigParser
except ModuleNotFoundError as ex:
    from configparser import ConfigParser


HARVEST_DEBUG = int(os.environ.get('HARVEST_DEBUG', 0))


class Client(object):
    url =' https://api.harvestapp.com'
    api_version = 'v2'

    def get_base_api_url(self):
        return '{}/{}'.format(self.url, self.api_version)



class PersonalAccessAuthClient(Client):

    def __init__(self, token=None, account_id=None, cfg=None):
        if token:
            self.token = token
        else:
            self.token = os.environ.get('HARVEST_PA_TOKEN')
 
        if account_id:
            self.account_id = account_id
        else:
            self.account_id = os.environ.get('HARVEST_PA_ACCOUNT_ID')

        if cfg:
            config = ConfigParser.RawConfigParser()
            config.read(cfg)
            self.token = config.get('authentication', 'token')
            self.account_id = config.get('authentication', 'account_id')

    def get_headers(self):
        ret = {
            'Harvest-Account-ID': self.account_id,
            'Authorization': 'Bearer {}'.format(self.token),
            'User-Agent': 'Harvest API - Python',
        }
        return ret
