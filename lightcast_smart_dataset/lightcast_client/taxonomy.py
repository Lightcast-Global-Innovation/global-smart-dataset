
from lightcast_insight.taxonomy_insight import TaxonomyInsight, \
    TaxonomyRequest, \
    TaxonomyResponse


class Taxonomy:

    def __init__(self, client: TaxonomyInsight) -> None:
        super(Taxonomy, self).__init__()
        self.__client = client

    def getSocLevel4(self) -> TaxonomyResponse:
        request = TaxonomyRequest()
        request.source = "uk"
        request.facet = "soc4"

        response = self.__client.get(request)
        return response.codelist['data']

    def getSocLevel3(self) -> TaxonomyResponse:
        request = TaxonomyRequest()
        request.source = "uk"
        request.facet = "soc3"

        response = self.__client.get(request)
        return response.codelist['data']

    def getSocLevel2(self) -> TaxonomyResponse:
        request = TaxonomyRequest()
        request.source = "uk"
        request.facet = "soc2"

        response = self.__client.get(request)
        return response.codelist['data']

    def getSocLevel1(self) -> TaxonomyResponse:
        request = TaxonomyRequest()
        request.source = "uk"
        request.facet = "soc1"

        response = self.__client.get(request)
        return response.codelist['data']

    def getOccupation(self) -> TaxonomyResponse:
        request = TaxonomyRequest()
        request.source = "uk"
        request.facet = "occupation"

        response = self.__client.get(request)
        return response.codelist['data']

    def getUkNuts3(self) -> TaxonomyResponse:
        request = TaxonomyRequest()
        request.source = "uk"
        request.facet = "nuts3"

        response = self.__client.get(request)
        return response.codelist['data']

    def getUkLocalAreaUnit(self) -> TaxonomyResponse:
        request = TaxonomyRequest()
        request.source = "uk"
        request.facet = "nuts4"

        response = self.__client.get(request)
        return response.codelist['data']

    def getGlobalMarket(self) -> TaxonomyResponse:
        request = TaxonomyRequest()
        request.source = "global"
        request.facet = "market"

        response = self.__client.get(request)
        return response.codelist['data']
