

from client.client import Source
from insight.occupation_insight import OccupationInsight, \
    BasicOccupationInsightResponseParser, \
    OccupationInsightRequestClient, \
    OccupationInsightRequest


class Global(Source):

    def __init__(self, username: str, password: str) -> None:
        super(Global, self).__init__()
        self.__occupation_insight = OccupationInsight(username=username,
                                                      password=password,
                                                      insight_response=BasicOccupationInsightResponseParser(),
                                                      insight_request=OccupationInsightRequestClient())

    def getOccupationInsight(self,
                             occupation: str = "",
                             occupation_level: str = "4",
                             area: str = "",
                             area_level: str = "3") -> str:
        request = OccupationInsightRequest()
        request.occupation = occupation
        request.area = area
        request.occupation_level = occupation_level
        request.area_level = area_level
        request.occupation_classification = "occupation"
        request.area_classification = "global"

        response = self.__occupation_insight.insight(request)
        return response.raw_response.decode("utf-8")