
from lightcast_insight.occupation_insight import OccupationInsight, \
    OccupationInsightRequest, \
    OccupationInsightResponse


class UK:

    def __init__(self, occupation_insight: OccupationInsight) -> None:
        super(UK, self).__init__()
        self.__occupation_insight = occupation_insight

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
