# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import re  # noqa: F401
import sys  # noqa: F401

import six  # noqa: F401
import nulltype  # noqa: F401

from petstore_api.model_utils import (  # noqa: F401
    ModelComposed,
    ModelNormal,
    ModelSimple,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_get_composed_info,
)


class InlineObject3(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('number',): {
            'inclusive_maximum': 543.2,
            'inclusive_minimum': 32.1,
        },
        ('double',): {
            'inclusive_maximum': 123.4,
            'inclusive_minimum': 67.8,
        },
        ('pattern_without_delimiter',): {
            'regex': {
                'pattern': r'^[A-Z].*',  # noqa: E501
            },
        },
        ('integer',): {
            'inclusive_maximum': 100,
            'inclusive_minimum': 10,
        },
        ('int32',): {
            'inclusive_maximum': 200,
            'inclusive_minimum': 20,
        },
        ('float',): {
            'inclusive_maximum': 987.6,
        },
        ('string',): {
            'regex': {
                'pattern': br'[a-z]',  # noqa: E501
                'flags': (re.IGNORECASE)
            },
        },
        ('password',): {
            'max_length': 64,
            'min_length': 10,
        },
    }

    additional_properties_type = None

    @staticmethod
    def openapi_types():
        """
        This must be a class method so a model may have properties that are
        of type self, this ensures that we don't create a cyclic import

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'number': (float,),  # noqa: E501
            'double': (float,),  # noqa: E501
            'pattern_without_delimiter': (str,),  # noqa: E501
            'byte': (str,),  # noqa: E501
            'integer': (int,),  # noqa: E501
            'int32': (int,),  # noqa: E501
            'int64': (int,),  # noqa: E501
            'float': (float,),  # noqa: E501
            'string': (str,),  # noqa: E501
            'binary': (file_type,),  # noqa: E501
            'date': (date,),  # noqa: E501
            'date_time': (datetime,),  # noqa: E501
            'password': (str,),  # noqa: E501
            'callback': (str,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        'number': 'number',  # noqa: E501
        'double': 'double',  # noqa: E501
        'pattern_without_delimiter': 'pattern_without_delimiter',  # noqa: E501
        'byte': 'byte',  # noqa: E501
        'integer': 'integer',  # noqa: E501
        'int32': 'int32',  # noqa: E501
        'int64': 'int64',  # noqa: E501
        'float': 'float',  # noqa: E501
        'string': 'string',  # noqa: E501
        'binary': 'binary',  # noqa: E501
        'date': 'date',  # noqa: E501
        'date_time': 'dateTime',  # noqa: E501
        'password': 'password',  # noqa: E501
        'callback': 'callback',  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_from_server',
        '_path_to_item',
        '_configuration',
    ])

    def __init__(self, number, double, pattern_without_delimiter, byte, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs):  # noqa: E501
        """inline_object3.InlineObject3 - a model defined in OpenAPI

        Args:
            number (float): None
            double (float): None
            pattern_without_delimiter (str): None
            byte (str): None

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _from_server (bool): True if the data is from the server
                                False if the data is from the client (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            integer (int): None. [optional]  # noqa: E501
            int32 (int): None. [optional]  # noqa: E501
            int64 (int): None. [optional]  # noqa: E501
            float (float): None. [optional]  # noqa: E501
            string (str): None. [optional]  # noqa: E501
            binary (file_type): None. [optional]  # noqa: E501
            date (date): None. [optional]  # noqa: E501
            date_time (datetime): None. [optional]  # noqa: E501
            password (str): None. [optional]  # noqa: E501
            callback (str): None. [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        self.number = number
        self.double = double
        self.pattern_without_delimiter = pattern_without_delimiter
        self.byte = byte
        for var_name, var_value in six.iteritems(kwargs):
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
