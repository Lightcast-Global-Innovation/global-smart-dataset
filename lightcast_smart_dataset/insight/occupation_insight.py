from abc import ABCMeta
import json
from lightcast_smart_dataset.OAuthClient import OAuthClient
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
        self.__raw_response = raw_response

    @property
    def refresh_date(self) -> str:
        return self.__refresh_date

    @refresh_date.setter
    def refresh_date(self, refresh_date: str) -> None:
        self.__refresh_date = refresh_date

    @property
    def current_year_active_postings(self) -> list:
        return self.__current_year_active_postings

    @current_year_active_postings.setter
    def current_year_active_postings(self, current_year_active_postings: list) -> None:
        if current_year_active_postings is not None and not \
           isinstance(current_year_active_postings, list):
            raise TypeError("current_year_active_postings must be a list")
        self.__current_year_active_postings = current_year_active_postings

    @property
    def previous_year_active_postings(self) -> list:
        return self.__previous_year_active_postings

    @previous_year_active_postings.setter
    def previous_year_active_postings(self, previous_year_active_postings: list) -> None:
        if previous_year_active_postings is not None and not \
           isinstance(previous_year_active_postings, list):
            raise TypeError("previous_year_active_postings must be a list")
        self.__previous_year_active_postings = previous_year_active_postings

    @property
    def salary_min(self) -> str:
        return self.__salary_min

    @salary_min.setter
    def salary_min(self, salary_min: str) -> None:

        self.__salary_min = salary_min

    @property
    def salary_max(self) -> str:
        return self.__salary_max

    @salary_max.setter
    def salary_max(self, salary_max: str) -> None:

        self.__salary_max = salary_max

    @property
    def salary_median(self) -> str:
        return self.__salary_median

    @salary_median.setter
    def salary_median(self, salary_median: str) -> None:

        self.__salary_median = salary_median

    @property
    def top_10_common_skills(self) -> list:
        return self.__top_10_common_skills

    @top_10_common_skills.setter
    def top_10_common_skills(self, top_10_common_skills: list) -> None:
        if top_10_common_skills is not None and not \
           isinstance(top_10_common_skills, list):
            raise TypeError("top_10_common_skills must be a list")
        self.__top_10_common_skills = top_10_common_skills

    @property
    def top_10_specialized_skills(self) -> list:
        return self.__top_10_specialized_skills

    @top_10_specialized_skills.setter
    def top_10_specialized_skills(self, top_10_specialized_skills: list) -> None:
        if top_10_specialized_skills is not None and not \
           isinstance(top_10_specialized_skills, list):
            raise TypeError("top_10_specialized_skills must be a list")
        self.__top_10_specialized_skills = top_10_specialized_skills

    @property
    def top_10_job_titles(self) -> list:
        return self.__top_10_job_titles

    @top_10_job_titles.setter
    def top_10_job_titles(self, top_10_job_titles: list) -> None:
        if top_10_job_titles is not None and not \
           isinstance(top_10_job_titles, list):
            raise TypeError("top_10_job_titles must be a list")
        self.__top_10_job_titles = top_10_job_titles

    @property
    def top_10_employers(self) -> list:
        return self.__top_10_employers

    @top_10_employers.setter
    def top_10_employers(self, top_10_employers: list) -> None:
        if top_10_employers is not None and not \
           isinstance(top_10_employers, list):
            raise TypeError("top_10_employers must be a list")
        self.__top_10_employers = top_10_employers


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
                   'Authorization': oauth.getAuthorizationString()}
        response = requests.post(url, data=json_payload, headers=headers)
        return response.text.encode('utf8')


class OccupationInsight:

    def __init__(self,
                 url: str = "https://solutions-api.lightcast.io/smart-dataset/occupation-insight/v1/uk",
                 auth_url: str = "https://solutions-api.lightcast.io/api/users/login",
                 username: str = "",
                 password: str = "",
                 insight_response: ResponseInsight = None,
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

    def __setInsightResponse(self, insight_response: ResponseInsight) -> None:
        if not isinstance(insight_response, ResponseInsight):
            raise TypeError("insight_response is not an instance of ResponseInsight.")

        self.__insight_response = insight_response

    def insight(self, request: InsightRequest) -> OccupationInsightResponse:
        try:
            return self.__insight(request)
        except Exception as e:
            raise e

    def __insight(self, request: InsightRequest) -> OccupationInsightResponse:
        oauth = OAuthClient(self.__auth_url, self.__username, self.__password)
        raw_response = self.__insight_request.write_request(self.__url, request, oauth)
        response = self.__insight_response.deserialize(raw_response)
        return response


class BasicOccupationInsightResponseParser(ResponseInsight):

    def __init__(self):
        pass

    def deserialize(self, raw_response: str):

        print(raw_response)
        json_response = json.loads(raw_response)
        refresh_date = json_response["date"]

        current_year_active_postings = json_response["current_year_active_postings"]["results"]
        previous_year_active_postings = json_response["previous_year_active_postings"]["results"]

        salary_max = json_response["salary"]["max"]
        salary_min = json_response["salary"]["min"]
        salary_median = json_response["salary"]["median"]

        top_10_employers = json_response["top_10_employers"]["results"]
        top_10_job_titles = json_response["top_10_job_titles"]["results"]
        top_10_common_skills = json_response["top_10_common_skills"]["results"]
        top_10_specialized_skills = json_response["top_10_common_skills"]["results"]

        response = OccupationInsightResponse()
        response.raw_response = raw_response
        response.refresh_date = refresh_date
        response.current_year_active_postings = current_year_active_postings
        response.previous_year_active_postings = previous_year_active_postings
        response.salary_max = salary_max
        response.salary_min = salary_min
        response.salary_median = salary_median

        response.top_10_common_skills = top_10_common_skills
        response.top_10_specialized_skills = top_10_specialized_skills
        response.top_10_job_titles = top_10_job_titles
        response.top_10_employers = top_10_employers

        return response
