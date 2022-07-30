import unittest
from unittest import TestCase

from lightcast_client.OAuthClient import OAuthClient


class OAuthClientTests(TestCase):

    def test_new_expect_no_error(self):
        try:
            OAuthClient(auth_url="xxx", username="xxx", password="xxx")

        except Exception as e:
            self.fail(str(e))


if __name__ == '__main__':
    unittest.main()
