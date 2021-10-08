"""
    Adversarial Security Assessment Platform for AI

    Adversarial Security Assessment Platform for AI API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: info@navinfo.eu
    Generated by: https://openapi-generator.tech
"""


import unittest

import asap_client
from asap_api.login_api import LoginApi  # noqa: E501


class TestLoginApi(unittest.TestCase):
    """LoginApi unit test stubs"""

    def setUp(self):
        self.api = LoginApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_auth_user(self):
        """Test case for get_auth_user

        Get the currently OAuth2 authenticated user platform token.  # noqa: E501
        """
        pass

    def test_login(self):
        """Test case for login

        Login app  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
