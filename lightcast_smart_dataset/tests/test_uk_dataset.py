import unittest
from unittest import TestCase
from mock import Mock

from lightcast_client.uk_dataset import UK
from lightcast_insight.occupation_insight import OccupationInsight, \
    BasicOccupationInsightResponseParser, OccupationInsightRequestClient


class UKTests(TestCase):

    response = """
            {
                "area": "Camden and City of London",
                "occupation": "Programmers and software development professionals",
                "date": "2022-07-30T15:15:52.681",
                "area_classification": "lau1_name",
                "occupation_classification": "soc3_name",
                "salary": {
                    "min": 0,
                    "max": 0,
                    "median": 0,
                    "unique_postings": 0
                },
                "current_year_active_postings": {
                    "results": [
                    {
                        "month": "2021-06",
                        "unique_postings": 0
                    },
                    {
                        "month": "2021-07",
                        "unique_postings": 0
                    },
                    {
                        "month": "2021-08",
                        "unique_postings": 0
                    },
                    {
                        "month": "2021-09",
                        "unique_postings": 0
                    },
                    {
                        "month": "2021-10",
                        "unique_postings": 0
                    },
                    {
                        "month": "2021-11",
                        "unique_postings": 0
                    },
                    {
                        "month": "2021-12",
                        "unique_postings": 0
                    },
                    {
                        "month": "2022-01",
                        "unique_postings": 0
                    },
                    {
                        "month": "2022-02",
                        "unique_postings": 0
                    },
                    {
                        "month": "2022-03",
                        "unique_postings": 0
                    },
                    {
                        "month": "2022-04",
                        "unique_postings": 0
                    },
                    {
                        "month": "2022-05",
                        "unique_postings": 0
                    },
                    {
                        "month": "2022-06",
                        "unique_postings": 0
                    }
                    ],
                    "total_unique_postings": 0
                },
                "previous_year_active_postings": {
                    "results": [
                    {
                        "month": "2020-06",
                        "unique_postings": 0
                    },
                    {
                        "month": "2020-07",
                        "unique_postings": 0
                    },
                    {
                        "month": "2020-08",
                        "unique_postings": 0
                    },
                    {
                        "month": "2020-09",
                        "unique_postings": 0
                    },
                    {
                        "month": "2020-10",
                        "unique_postings": 0
                    },
                    {
                        "month": "2020-11",
                        "unique_postings": 0
                    },
                    {
                        "month": "2020-12",
                        "unique_postings": 0
                    },
                    {
                        "month": "2021-01",
                        "unique_postings": 0
                    },
                    {
                        "month": "2021-02",
                        "unique_postings": 0
                    },
                    {
                        "month": "2021-03",
                        "unique_postings": 0
                    },
                    {
                        "month": "2021-04",
                        "unique_postings": 0
                    },
                    {
                        "month": "2021-05",
                        "unique_postings": 0
                    },
                    {
                        "month": "2021-06",
                        "unique_postings": 0
                    }
                    ],
                    "total_unique_postings": 0
                },
                "top_10_specialized_skills": {
                    "results": [
                    ],
                    "limit": 10,
                    "rank_by": "unique_postings",
                    "analyzed_unique_postings": 0
                },
                "top_10_common_skills": {
                    "results": [
                    ],
                    "limit": 10,
                    "rank_by": "unique_postings",
                    "analyzed_unique_postings": 0
                },
                "top_10_employers": {
                    "results": [
                    ],
                    "limit": 10,
                    "rank_by": "unique_postings",
                    "analyzed_unique_postings": 0
                },
                "top_10_job_titles": {
                    "results": [
                    ],
                    "limit": 10,
                    "rank_by": "unique_postings",
                    "analyzed_unique_postings": 0
                }
                }
    """

    def test_new_expect_no_error(self):
        try:
            insight = Mock(spec=OccupationInsight)
            insight.insight.return_value = []
            UK(insight)

        except Exception as e:
            self.fail(str(e))

    def test_get_occupation_insight_call(self):
        insight = Mock(spec=OccupationInsight)
        insight.insight.return_value = []
        uk_dataset = UK(insight)

        uk_dataset.getOccupationInsight(occupation="xxx", area="xxx")

        insight.insight.assert_called()

    def test_get_occupation_insight_call_return_occupation_insight_response(self):
        client = Mock(spec=OccupationInsightRequestClient)
        client.write_request.return_value = self.response
        insight = OccupationInsight(url="xxx",
                                    auth_url="xxx",
                                    username="xxx",
                                    password="xxx",
                                    insight_response=BasicOccupationInsightResponseParser(),
                                    insight_request=client)
        uk_dataset = UK(insight)

        r = uk_dataset.getOccupationInsight(occupation="xxx", area="xxx")

        self.assertEqual(r.raw_response, self.response)

    def test_get_soc_insight_call(self):
        insight = Mock(spec=OccupationInsight)
        insight.insight.return_value = []
        uk_dataset = UK(insight)

        uk_dataset.getSocOccupationInsight(occupation="xxx", area="xxx")

        insight.insight.assert_called()

    def test_get_soc_insight_call_return_occupation_insight_response(self):
        client = Mock(spec=OccupationInsightRequestClient)
        client.write_request.return_value = self.response
        insight = OccupationInsight(url="xxx",
                                    auth_url="xxx",
                                    username="xxx",
                                    password="xxx",
                                    insight_response=BasicOccupationInsightResponseParser(),
                                    insight_request=client)
        uk_dataset = UK(insight)

        r = uk_dataset.getSocOccupationInsight(occupation="xxx", area="xxx")

        self.assertEqual(r.raw_response, self.response)


if __name__ == '__main__':
    unittest.main()
