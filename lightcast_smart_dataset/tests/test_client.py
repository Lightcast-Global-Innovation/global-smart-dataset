import unittest
from unittest import TestCase

from lightcast_client.client import LightcastSmartDataset


class LightcastSmartDatasetTests(TestCase):

    def test_new_expect_no_error(self):
        try:
            LightcastSmartDataset(username="xxx", password="xxx")

        except Exception as e:
            self.fail(str(e))

    def test_not_string_username_expect_error(self):
        with self.assertRaises(TypeError):
            LightcastSmartDataset(username=111, password="xxx")

    def test_not_string_password_expect_error(self):
        with self.assertRaises(TypeError):
            LightcastSmartDataset(username="xxx", password=111)


if __name__ == '__main__':
    unittest.main()
