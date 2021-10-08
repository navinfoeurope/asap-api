"""
    Adversarial Security Assessment Platform for AI

    Adversarial Security Assessment Platform for AI API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: info@navinfo.eu
    Generated by: https://openapi-generator.tech
"""


import unittest

import asap_client
from asap_api.organization_api import OrganizationApi  # noqa: E501


class TestOrganizationApi(unittest.TestCase):
    """OrganizationApi unit test stubs"""

    def setUp(self):
        self.api = OrganizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_organization(self):
        """Test case for add_organization

        Add organization.  # noqa: E501
        """
        pass

    def test_delete_custom_dataset(self):
        """Test case for delete_custom_dataset

        Delete dataset.  # noqa: E501
        """
        pass

    def test_delete_organization(self):
        """Test case for delete_organization

        Delete an organization.  # noqa: E501
        """
        pass

    def test_download_dataset(self):
        """Test case for download_dataset

        Download dataset data.  # noqa: E501
        """
        pass

    def test_get_datasets(self):
        """Test case for get_datasets

        Get the datasets defined for this organization.  # noqa: E501
        """
        pass

    def test_get_defined_attacks(self):
        """Test case for get_defined_attacks

        Get the attacks defined for this organization.  # noqa: E501
        """
        pass

    def test_get_defined_defenses(self):
        """Test case for get_defined_defenses

        Get the defenses defined for this organization.  # noqa: E501
        """
        pass

    def test_get_defined_metrics(self):
        """Test case for get_defined_metrics

        Get the metrics defined for this organization.  # noqa: E501
        """
        pass

    def test_get_defined_noises(self):
        """Test case for get_defined_noises

        Get the noises defined for this organization.  # noqa: E501
        """
        pass

    def test_get_organization(self):
        """Test case for get_organization

        Get organization by id.  # noqa: E501
        """
        pass

    def test_get_organizations(self):
        """Test case for get_organizations

        Get organizations.  # noqa: E501
        """
        pass

    def test_update_custom_dataset(self):
        """Test case for update_custom_dataset

        Update dataset.  # noqa: E501
        """
        pass

    def test_update_organization(self):
        """Test case for update_organization

        Update organization.  # noqa: E501
        """
        pass

    def test_upload_dataset(self):
        """Test case for upload_dataset

        Upload dataset.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
