from abc import ABCMeta
from client.OAuthClient import OAuthClient
import requests


class TaxonomyRequest:

    def __init__(self):
        self.source = None
        self.facet = None
        self.limit = None

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str) -> None:
        self.__source = source

    @property
    def facet(self) -> str:
        return self.__facet

    @facet.setter
    def facet(self, facet: str) -> None:
        self.__facet = facet

    @property
    def limit(self) -> str:
        return self.__limit

    @limit.setter
    def limit(self, limit: str) -> None:
        self.__limit = limit


class TaxonomyResponse:

    def __init__(self):
        pass

    @property
    def raw_response(self) -> str:
        return self.__raw_response

    @raw_response.setter
    def raw_response(self, raw_response: str) -> None:
        self.__raw_response = raw_response

    @property
    def codelist(self) -> list:
        return self.__codelist

    @codelist.setter
    def codelist(self, codelist: list) -> None:

        self.__codelist = codelist


class ResponseTaxonomy(metaclass=ABCMeta):

    def deserialize(response) -> TaxonomyResponse:
        raise NotImplementedError()


class RequestTaxonomy(metaclass=ABCMeta):

    def write_request(self, url: str, request: TaxonomyRequest, oauth: OAuthClient) -> dict:
        raise NotImplementedError()


class TaxonomyRequestClient(TaxonomyRequest):

    def __create_parse_command(self,
                               url: str,
                               request: TaxonomyRequest) -> str:

        return url + "/" + request.source + "/" + request.facet + "?limit=" + request.limit

    def write_request(self, url: str, request: TaxonomyRequest, oauth: OAuthClient) -> str:
        headers = {'Content-Type': "application/json",
                   'Accept': "application/json",
                   'Authorization': oauth.getAuthorizationString()}
        final_url = self.__create_parse_command(url, request)
        response = requests.get(final_url, headers=headers)
        return response.text.encode('utf8')


class Taxonomy:

    def __init__(self,
                 url: str = "https://solutions-api.lightcast.io/smart-dataset/taxonomies",
                 auth_url: str = "https://solutions-api.lightcast.io/api/users/login",
                 username: str = "",
                 password: str = "",
                 response: ResponseTaxonomy = None,
                 request: RequestTaxonomy = None) -> None:
        self.__url = url
        self.__auth_url = auth_url
        self.__username = username
        self.__password = password
        self.__setResponse(response)
        self.__setRequest(request)

    def __setRequest(self, request: RequestTaxonomy) -> None:
        if not isinstance(request, RequestTaxonomy):
            raise TypeError("request is not an instance of RequestTaxonomy.")

        self.__request = request

    def __setResponse(self, response: ResponseTaxonomy) -> None:
        if not isinstance(response, ResponseTaxonomy):
            raise TypeError("response is not an instance of ResponseTaxonomy.")

        self.__response = response

    def get(self, request: TaxonomyRequest) -> TaxonomyResponse:
        try:
            return self.__get(request)
        except Exception as e:
            raise e

    def __get(self, request: TaxonomyRequest) -> TaxonomyResponse:
        oauth = OAuthClient(self.__auth_url, self.__username, self.__password)
        raw_response = self.__request.write_request(self.__url, request, oauth)
        response = self.__insight_response.deserialize(raw_response)
        return response


class BasicTaxonomyResponseParser(RequestTaxonomy):

    def __init__(self):
        pass

    def deserialize(self, raw_response: str):

        print(raw_response)
        response = TaxonomyResponse()
        response.raw_response = raw_response

        return response
