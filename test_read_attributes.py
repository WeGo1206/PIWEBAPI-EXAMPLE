""" This script contains the unit tests for the ReadAttributes Script """

import unittest

from appsettings import PIWEBAPI_URL, AF_SERVER_NAME, USER_NAME, USER_PASSWORD, AUTH_TYPE, VERIFY_SSL


class TestStringMethods(unittest.TestCase):
    """
        We recommend running these unit tests using the file syntax:
            python -m unittest test_read_attributes
        To discover and run all unit tests:  python -m unittest
        To run the unit tests in a file:  python -m unittest test_read_attributes
        To run a single test:
            python -m unittest test_read_attributes.TestStringMethods.test_readattributesnapshot
    """

    def test_readattributesnapshot(self):
        """ Test the read_attribute_snapshot method """
        from read_attributes import read_attribute_snapshot
        self.assertEqual(read_attribute_snapshot(PIWEBAPI_URL,
                                                 AF_SERVER_NAME, USER_NAME, USER_PASSWORD, AUTH_TYPE, VERIFY_SSL), 200)

    def test_readattributestream(self):
        """ Test the read_attribute_stream method """
        from read_attributes import read_attribute_stream
        self.assertEqual(read_attribute_stream(PIWEBAPI_URL,
                                               AF_SERVER_NAME, USER_NAME, USER_PASSWORD, AUTH_TYPE, VERIFY_SSL), 200)

    def test_readattributeselectedfields(self):
        """ Test the read_attribute_selected_fields method """
        from read_attributes import read_attribute_selected_fields
        self.assertEqual(read_attribute_selected_fields(PIWEBAPI_URL,
                                                        AF_SERVER_NAME,
                                                        USER_NAME, USER_PASSWORD, AUTH_TYPE, VERIFY_SSL), 200)


if __name__ == '__main__':
    unittest.main()
