

from lightcast_insight.occupation_insight import OccupationInsight, \
    OccupationInsightRequest, \
    OccupationInsightResponse


class Global:

    def __init__(self, occupation_insight: OccupationInsight) -> None:
        super(Global, self).__init__()
        self.__occupation_insight = occupation_insight

    def getOccupationInsight(self,
                             occupation: str = "",
                             occupation_level: str = "3",
                             area: str = "",
                             area_level: str = "2") -> OccupationInsightResponse:
        request = OccupationInsightRequest()
        request.occupation = occupation
        request.area = area
        request.occupation_level = occupation_level
        request.area_level = area_level
        request.occupation_classification = "occupation"
        request.area_classification = "global"

        response = self.__occupation_insight.insight(request)
        return response
