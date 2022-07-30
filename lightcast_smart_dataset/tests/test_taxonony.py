import unittest
from unittest import TestCase
from mock import Mock

from lightcast_client.taxonomy import Taxonomy
from lightcast_insight.taxonomy_insight import TaxonomyInsight, TaxonomyResponse


class TaxonomyTests(TestCase):

    def test_new_expect_no_error(self):
        try:
            client = Mock(spec=TaxonomyInsight)
            client.get.return_value = []
            Taxonomy(client)

        except Exception as e:
            self.fail(str(e))

    def test_get_taxonomy_insight_call(self):
        get = Mock(spec=TaxonomyInsight)
        response = TaxonomyResponse()
        response.raw_response = {}
        response.codelist = {"data": []}

        get.get.return_value = response
        client = Taxonomy(get)

        client.getGlobalMarket()

        get.get.assert_called()

    def test_get_taxonomy_soc4_call(self):
        get = Mock(spec=TaxonomyInsight)
        response = TaxonomyResponse()
        response.raw_response = {}
        response.codelist = {"data": []}

        get.get.return_value = response
        client = Taxonomy(get)

        r = client.getSocLevel4()

        self.assertEqual(r, response.codelist["data"])

    def test_get_taxonomy_soc3_call(self):
        get = Mock(spec=TaxonomyInsight)
        response = TaxonomyResponse()
        response.raw_response = {}
        response.codelist = {"data": []}

        get.get.return_value = response
        client = Taxonomy(get)

        r = client.getSocLevel3()

        self.assertEqual(r, response.codelist["data"])

    def test_get_taxonomy_soc2_call(self):
        get = Mock(spec=TaxonomyInsight)
        response = TaxonomyResponse()
        response.raw_response = {}
        response.codelist = {"data": []}

        get.get.return_value = response
        client = Taxonomy(get)

        r = client.getSocLevel2()

        self.assertEqual(r, response.codelist["data"])

    def test_get_taxonomy_soc1_call(self):
        get = Mock(spec=TaxonomyInsight)
        response = TaxonomyResponse()
        response.raw_response = {}
        response.codelist = {"data": []}

        get.get.return_value = response
        client = Taxonomy(get)

        r = client.getSocLevel1()

        self.assertEqual(r, response.codelist["data"])

    def test_get_taxonomy_global_market_call(self):
        get = Mock(spec=TaxonomyInsight)
        response = TaxonomyResponse()
        response.raw_response = {}
        response.codelist = {"data": []}

        get.get.return_value = response
        client = Taxonomy(get)

        r = client.getGlobalMarket()

        self.assertEqual(r, response.codelist["data"])

    def test_get_taxonomy_uk_lau_call(self):
        get = Mock(spec=TaxonomyInsight)
        response = TaxonomyResponse()
        response.raw_response = {}
        response.codelist = {"data": []}

        get.get.return_value = response
        client = Taxonomy(get)

        r = client.getUkLocalAreaUnit()

        self.assertEqual(r, response.codelist["data"])

    def test_get_taxonomy_uk_nuts3_call(self):
        get = Mock(spec=TaxonomyInsight)
        response = TaxonomyResponse()
        response.raw_response = {}
        response.codelist = {"data": []}

        get.get.return_value = response
        client = Taxonomy(get)

        r = client.getUkNuts3()

        self.assertEqual(r, response.codelist["data"])

    def test_get_taxonomy_occupation_call(self):
        get = Mock(spec=TaxonomyInsight)
        response = TaxonomyResponse()
        response.raw_response = {}
        response.codelist = {"data": []}

        get.get.return_value = response
        client = Taxonomy(get)

        r = client.getOccupation()

        self.assertEqual(r, response.codelist["data"])


if __name__ == '__main__':
    unittest.main()
