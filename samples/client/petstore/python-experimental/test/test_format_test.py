# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import datetime
import unittest

import petstore_api
from petstore_api.models.format_test import FormatTest  # noqa: E501
from petstore_api import ApiValueError


class TestFormatTest(unittest.TestCase):
    """FormatTest unit test stubs"""

    def setUp(self):
        self.required_named_args = dict(
            number=40.1,
            byte=b'what',
            date=datetime.date(2019, 3, 23),
            password='rainbowtable'
        )

    def test_integer(self):
        var_name = 'integer'
        validations = FormatTest.validations[(var_name,)]
        keyword_args = {}
        keyword_args.update(self.required_named_args)
        key_adder_pairs = [('inclusive_maximum', 1), ('inclusive_minimum', -1)]
        for key, adder in key_adder_pairs:
            # value outside the bounds throws an error
            with self.assertRaises(ApiValueError):
                keyword_args[var_name] = validations[key] + adder
                FormatTest(**keyword_args)

            # value inside the bounds works
            keyword_args[var_name] = validations[key]
            assert (getattr(FormatTest(**keyword_args), var_name) ==
                    validations[key])

    def test_int32(self):
        var_name = 'int32'
        validations = FormatTest.validations[(var_name,)]
        keyword_args = {}
        keyword_args.update(self.required_named_args)
        key_adder_pairs = [('inclusive_maximum', 1), ('inclusive_minimum', -1)]
        for key, adder in key_adder_pairs:
            # value outside the bounds throws an error
            with self.assertRaises(ApiValueError):
                keyword_args[var_name] = validations[key] + adder
                FormatTest(**keyword_args)

            # value inside the bounds works
            keyword_args[var_name] = validations[key]
            assert (getattr(FormatTest(**keyword_args), var_name) ==
                    validations[key])

    def test_number(self):
        var_name = 'number'
        validations = FormatTest.validations[(var_name,)]
        keyword_args = {}
        keyword_args.update(self.required_named_args)
        key_adder_pairs = [('inclusive_maximum', 1), ('inclusive_minimum', -1)]
        for key, adder in key_adder_pairs:
            # value outside the bounds throws an error
            with self.assertRaises(ApiValueError):
                keyword_args[var_name] = validations[key] + adder
                FormatTest(**keyword_args)

            # value inside the bounds works
            keyword_args[var_name] = validations[key]
            assert (getattr(FormatTest(**keyword_args), var_name) ==
                    validations[key])

    def test_float(self):
        var_name = 'float'
        validations = FormatTest.validations[(var_name,)]
        keyword_args = {}
        keyword_args.update(self.required_named_args)
        key_adder_pairs = [('inclusive_maximum', 1), ('inclusive_minimum', -1)]
        for key, adder in key_adder_pairs:
            # value outside the bounds throws an error
            with self.assertRaises(ApiValueError):
                keyword_args[var_name] = validations[key] + adder
                FormatTest(**keyword_args)

            # value inside the bounds works
            keyword_args[var_name] = validations[key]
            assert (getattr(FormatTest(**keyword_args), var_name) ==
                    validations[key])

    def test_double(self):
        var_name = 'double'
        validations = FormatTest.validations[(var_name,)]
        keyword_args = {}
        keyword_args.update(self.required_named_args)
        key_adder_pairs = [('inclusive_maximum', 1), ('inclusive_minimum', -1)]
        for key, adder in key_adder_pairs:
            # value outside the bounds throws an error
            with self.assertRaises(ApiValueError):
                keyword_args[var_name] = validations[key] + adder
                FormatTest(**keyword_args)

            # value inside the bounds works
            keyword_args[var_name] = validations[key]
            assert (getattr(FormatTest(**keyword_args), var_name) ==
                    validations[key])

    def test_password(self):
        var_name = 'password'
        validations = FormatTest.validations[(var_name,)]
        keyword_args = {}
        keyword_args.update(self.required_named_args)
        key_adder_pairs = [('max_length', 1), ('min_length', -1)]
        for key, adder in key_adder_pairs:
            # value outside the bounds throws an error
            with self.assertRaises(ApiValueError):
                keyword_args[var_name] = 'a'*(validations[key] + adder)
                FormatTest(**keyword_args)

            # value inside the bounds works
            keyword_args[var_name] = 'a'*validations[key]
            assert (getattr(FormatTest(**keyword_args), var_name) ==
                    'a'*validations[key])

    def test_string(self):
        var_name = 'string'
        validations = FormatTest.validations[(var_name,)]
        keyword_args = {}
        keyword_args.update(self.required_named_args)
        values_invalid = ['abc3', '1', '.', ' ', 'مرحبا', '']
        for value_invalid in values_invalid:
            # invalid values throw exceptions
            with self.assertRaises(ApiValueError):
                keyword_args[var_name] = value_invalid
                FormatTest(**keyword_args)

        # valid value works
        value_valid = 'abcdz'
        keyword_args[var_name] = value_valid
        assert getattr(FormatTest(**keyword_args), var_name) == value_valid


if __name__ == '__main__':
    unittest.main()
