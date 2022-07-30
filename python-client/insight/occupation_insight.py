from abc import ABCMeta
import json
from client.OAuthClient import OAuthClient
import requests


class OccupationInsightRequest:

    def __init__(self):
        self.source = None
        self.occupation = None
        self.area = None
        self.occupation_level = None
        self.area_level = None
        self.occupation_classification = None
        self.area_classification = None

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str) -> None:
        self.__source = source

    @property
    def occupation(self) -> str:
        return self.__occupation

    @occupation.setter
    def occupation(self, occupation: str) -> None:
        self.__occupation = occupation

    @property
    def area(self) -> str:
        return self.__area

    @area.setter
    def area(self, area: str) -> None:
        self.__area = area

    @property
    def occupation_level(self) -> str:
        return self.__occupation_level

    @occupation_level.setter
    def occupation_level(self, occupation_level: str) -> None:
        self.__occupation_level = occupation_level

    @property
    def area_level(self) -> str:
        return self.__area_level

    @area_level.setter
    def area_level(self, area_level: str) -> None:
        self.__area_level = area_level

    @property
    def occupation_classification(self) -> str:
        return self.__occupation_classification

    @occupation_classification.setter
    def occupation_classification(self, occupation_classification: str) -> None:
        self.__occupation_classification = occupation_classification

    @property
    def area_classification(self) -> str:
        return self.__area_classification

    @area_classification.setter
    def area_classification(self, area_classification: str) -> None:
        self.__area_classification = area_classification


class OccupationInsightResponse:

    def __init__(self):
        pass

    @property
    def raw_response(self) -> str:
        return self.__raw_response

    @raw_response.setter
    def raw_response(self, raw_response: str) -> None:
        if raw_response is not None and not isinstance(raw_response, str):
            raise TypeError("raw_response must be a string")
        self.__raw_response = raw_response


class ResponseInsight(metaclass=ABCMeta):

    def deserialize(response) -> OccupationInsightResponse:
        raise NotImplementedError()


class InsightRequest(metaclass=ABCMeta):

    def write_request(self, url: str, request: OccupationInsightRequest, oauth: OAuthClient) -> dict:
        raise NotImplementedError()


class OccupationInsightRequestClient(InsightRequest):

    def __create_parse_command(self, request: OccupationInsightRequest) -> str:
        payload = {
            "occupation": request.occupation,
            "area": request.area,
            "occupation_level": request.occupation_level,
            "area_level": request.area_level,
            "occupation_classification": request.occupation_classification,
            "area_classification": request.area_classification
        }

        return json.dumps(payload)

    def write_request(self, url: str, request: OccupationInsightRequest, oauth: OAuthClient) -> str:
        json_payload = self.__create_parse_command(request)
        headers = {'Content-Type': "application/json",
                   'Accept': "application/json",
                   'Authorization': oauth.get_authorizationString()}
        response = requests.post(url, data=json_payload, headers=headers)
        return response.text.encode('utf8')


class OccupationInsight:

    def __init__(self,
                 url: str = "https://solutions-api.lightcast.io/smart-dataset/occupation-insight/v1",
                 auth_url: str = "https://solutions-api.lightcast.io/smart-dataset/occupation-insight/v1",
                 username: str = "",
                 password: str = "",
                 insight_response: OccupationInsightResponse = None,
                 insight_request: InsightRequest = None) -> None:
        self.__url = url
        self.__auth_url = auth_url
        self.__username = username
        self.__password = password
        self.__setInsightResponse(insight_response)
        self.__setInsightRequest(insight_request)

    def __setInsightRequest(self, insight_request: InsightRequest) -> None:
        if not isinstance(insight_request, InsightRequest):
            raise TypeError("insight_request is not an instance of InsightRequest.")

        self.__insight_request = insight_request

    def __setInsightResponse(self, insight_response: OccupationInsightResponse) -> None:
        if not isinstance(insight_response, OccupationInsightResponse):
            raise TypeError("insight_response is not an instance of OccupationInsightResponse.")

        self.__insight_response = insight_response

    def insight(self, request: InsightRequest) -> OccupationInsightResponse:
        try:
            return self.__insight(request)
        except Exception as e:
            raise e

    def __insight(self, request: InsightRequest) -> OccupationInsightResponse:
        oauth = OAuthClient(self.__auth_url, "POST", self.__username,
                            self.__password)
        raw_response = self.__insight_request.write_request(self.__url, request, oauth)
        response = self.__insight_response.deserialize(raw_response)
        return response


class BasicOccupationInsightResponseParser(ResponseInsight):

    def __init__(self):
        pass

    def __check_error(self, response: str):
        error_message = ""
        if error_message:
            raise Exception(error_message)

    def deserialize(self, raw_response: str):

        response = OccupationInsightResponse()
        response.raw_response = raw_response
        return response
