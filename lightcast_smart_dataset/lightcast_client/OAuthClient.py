import requests
import json


class OAuthClient:

    def __init__(self, auth_url, username, password):
        self.__auth_url = auth_url
        self.__username = username
        self.__password = password

    def getAuthorizationString(self):  # pragma: no cover
        login_payload = {
            "username": self.__username,
            "password": self.__password
        }

        headers = {'Content-Type': "application/json"}

        response = requests.request("POST", self.__auth_url,
                                    data=json.dumps(login_payload),
                                    headers=headers)
        response = json.loads(response.text)
        tokens = response["tokens"]
        access_token = tokens["access_token"]

        return f'Bearer {access_token}'
