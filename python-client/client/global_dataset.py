

from insight.occupation_insight import OccupationInsight, \
    BasicOccupationInsightResponseParser, \
    OccupationInsightRequestClient, \
    OccupationInsightRequest, \
    OccupationInsightResponse


class Global:

    def __init__(self, username: str, password: str) -> None:
        super(Global, self).__init__()
        url = "https://solutions-api.lightcast.io/smart-dataset/occupation-insight/v1/global"
        self.__occupation_insight = OccupationInsight(url=url,
                                                      username=username,
                                                      password=password,
                                                      insight_response=BasicOccupationInsightResponseParser(),
                                                      insight_request=OccupationInsightRequestClient())

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
        request.area_classification = "global"

        response = self.__occupation_insight.insight(request)
        return response
