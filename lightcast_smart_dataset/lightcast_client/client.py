
from lightcast_client.uk_dataset import UK
from lightcast_client.global_dataset import Global
from lightcast_client.taxonomy import Taxonomy
from lightcast_insight.occupation_insight import OccupationInsight, \
    BasicOccupationInsightResponseParser, \
    OccupationInsightRequestClient
from lightcast_insight.taxonomy_insight import TaxonomyInsight, \
    TaxonomyRequestClient, \
    BasicTaxonomyResponseParser


class LightcastSmartDataset():

    def __init__(self, username: str, password: str) -> None:
        super(LightcastSmartDataset, self).__init__()
        self.__setUsername(username)
        self.__setPassword(password)

    def __setUsername(self, username: str) -> None:
        if not isinstance(username, str):
            raise TypeError("username is not an instance of str.")

        self.__username = username

    def __setPassword(self, password: str) -> None:
        if not isinstance(password, str):
            raise TypeError("password is not an instance of str.")

        self.__password = password

    def ukDataset(self) -> UK:  # pragma: no cover
        url = "https://solutions-api.lightcast.io/smart-dataset/occupation-insight/v1/uk"
        self.__uk_occupation_insight = OccupationInsight(url=url,
                                                         username=self.__username,
                                                         password=self.__password,
                                                         insight_response=BasicOccupationInsightResponseParser(),
                                                         insight_request=OccupationInsightRequestClient())
        return UK(self.__uk_occupation_insight)

    def globalDataset(self) -> Global:  # pragma: no cover
        url = "https://solutions-api.lightcast.io/smart-dataset/occupation-insight/v1/global"
        if (self.__global_occs_insight is None):
            self.__global_occs_insight = OccupationInsight(url=url,
                                                           username=self.__username,
                                                           password=self.__password,
                                                           insight_response=BasicOccupationInsightResponseParser(),
                                                           insight_request=OccupationInsightRequestClient())
        return Global(self.__global_occs_insight)

    def taxonomy(self) -> Taxonomy:  # pragma: no cover
        self.__taxonomuy_client = TaxonomyInsight(username=self.__username,
                                                  password=self.__password,
                                                  response=BasicTaxonomyResponseParser(),
                                                  request=TaxonomyRequestClient())
        return Taxonomy(self.__taxonomuy_client)
