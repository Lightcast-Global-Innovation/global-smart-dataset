
from insight.occupation_insight import OccupationInsight, \
    BasicOccupationInsightResponseParser, \
    OccupationInsightRequestClient, \
    OccupationInsightRequest, \
    OccupationInsightResponse


class UK:

    def __init__(self, username: str, password: str) -> None:
        super(UK, self).__init__()
        self.__occupation_insight = OccupationInsight(username=username,
                                                      password=password,
                                                      insight_response=BasicOccupationInsightResponseParser(),
                                                      insight_request=OccupationInsightRequestClient())

    def getSocOccupationInsight(self,
                                occupation: str = "",
                                occupation_level: str = "4",
                                area: str = "",
                                area_level: str = "3") -> OccupationInsightResponse:
        request = OccupationInsightRequest()
        request.occupation = occupation
        request.area = area
        request.occupation_level = occupation_level
        request.area_level = area_level
        request.occupation_classification = "soc"
        request.area_classification = "nuts"

        response = self.__occupation_insight.insight(request)
        return response

    def getOccupationInsight(self,
                             occupation: str = "",
                             occupation_level: str = "4",
                             area: str = "",
                             area_level: str = "3") -> OccupationInsightResponse:
        request = OccupationInsightRequest()
        request.occupation = occupation
        request.area = area
        request.occupation_level = occupation_level
        request.area_level = area_level
        request.occupation_classification = "occupation"
        request.area_classification = "nuts"

        response = self.__occupation_insight.insight(request)
        return response
