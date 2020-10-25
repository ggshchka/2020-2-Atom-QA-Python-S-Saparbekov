import json
from urllib.parse import urljoin

import requests


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class MyTargetClient:

    def __init__(self, user, password):
        self.base_url = 'https://target.my.com'
        self.session = requests.Session()
        self.csrf_token = None
        self.user = user
        self.password = password

    def _request(self, method, location, headers=None, status_code=200,
                 params=None, data=None, json=True):
        url = urljoin(
            self.base_url,
            location
        )
        response = self.session.request(
            method, url, headers=headers,
            params=params, data=data,
        )
        if response.status_code != status_code:
            raise ResponseStatusCodeException(f' Got {response.status_code} '
                                              f'{response.reason} for URL "{url}"')

        if json:
            json_response = response.json()

            if json_response.get('bStateError'):
                error = json_response['sErrorMsg']
                raise RequestErrorException(f'Request "{url}" dailed '
                                            f'with error "{error}"!')
            return json_response
        return response

    def get_token(self):
        location = 'csrf'
        headers = self._request(
            method='GET',
            location=location,
            json=False
        ).headers
        return headers['Set-Cookie'].split(';')[0].split('=')[-1]

    def login(self) -> object:
        location = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        data = {
            'email': self.user,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?'
                        'state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/',
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': self.base_url
        }
        r = self._request(
            method='POST',
            location=location,
            headers=headers,
            data=data,
            json=False,
        )
        self.csrf_token = self.get_token()
        return r

    def create_segment(self, name):
        location = 'https://target.my.com/api/v2/remarketing/segments.json?' \
                   'fields=relations__object_type,relations__object_id,' \
                   'relations__params,relations_count,id,name,pass_condition,' \
                   'created,campaign_ids,users,flags'
        data = json.dumps(
            {
                "name":name,
                "pass_condition":1,
                "relations":[
                    {"object_type":"remarketing_player",
                     "params":{"type":"positive","left":365,"right":0}}
                ],
                "logicType":"or"
            }
        )
        headers = {
            'Content-Type': 'application/json',
            'Referer': 'https://target.my.com/segments/segments_list/new/',
            'X-CSRFToken': self.csrf_token
        }
        r = self._request(
            method='POST',
            location=location,
            data=data,
            headers=headers,
            json=True
        )
        return r

    def get_segment_id(self, response):
        return response['id']

    def delete_segment(self, id):
        location = 'https://target.my.com/api/v2/remarketing/segments/'+str(id)+'.json'

        headers = {
            'Content-Type': 'application/json',
            'Referer': 'https://target.my.com/segments/segments_list',
            'X-CSRFToken': self.csrf_token
        }
        r = self._request(
            method='DELETE',
            location=location,
            headers=headers,
            status_code=204,
            json=False
        )
        return r
