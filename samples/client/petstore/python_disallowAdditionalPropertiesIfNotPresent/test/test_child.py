# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import sys
import unittest

import petstore_api
try:
    from petstore_api.model import child_all_of
except ImportError:
    child_all_of = sys.modules[
        'petstore_api.model.child_all_of']
try:
    from petstore_api.model import parent
except ImportError:
    parent = sys.modules[
        'petstore_api.model.parent']
from petstore_api.model.child import Child


class TestChild(unittest.TestCase):
    """Child unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChild(self):
        """Test Child
        This will fail because additional_properties_type is None in ChildAllOf and it must be defined as any type
        to allow in the property radio_waves which is not defined in ChildAllOf, it is defined in Grandparent
        """
        # make an instance of Child, a composed schema model
        radio_waves = True
        tele_vision = True
        inter_net = True
        with self.assertRaises(petstore_api.exceptions.ApiValueError):
            child = Child(
                radio_waves=radio_waves,
                tele_vision=tele_vision,
                inter_net=inter_net
            )

if __name__ == '__main__':
    unittest.main()