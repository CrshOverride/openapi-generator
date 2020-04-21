# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import petstore_api
from petstore_api.models.format_test import FormatTest  # noqa: E501
from petstore_api.rest import ApiException

class TestFormatTest(unittest.TestCase):
    """FormatTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FormatTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = petstore_api.models.format_test.FormatTest()  # noqa: E501
        if include_optional :
            return FormatTest(
                integer = 1E+1,
                int32 = 2E+1,
                int64 = 56,
                number = 32.1,
                float = 54.3,
                double = 67.8,
                string = 'a',
                byte = 'YQ==',
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                uuid = '72f98069-206d-4f12-9f12-3d1e525a8e84',
                password = '0123456789',
                big_decimal = 1
            )
        else :
            return FormatTest(
                number = 32.1,
                byte = 'YQ==',
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                password = '0123456789',
        )

    def testFormatTest(self):
        """Test FormatTest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
