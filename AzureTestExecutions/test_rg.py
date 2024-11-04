from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

# Replace these values with your Azure subscription ID, resource group, and storage account name
SUBSCRIPTION_ID = '86ac5624-f280-4b8f-8fd7-520872422e29'
RESOURCE_GROUP = 'demorg'

from AzureTestCases.azure_rg_tests import azure_check_if_rg_exists

# Authenticate using Azure CLI credentials
credential = AzureCliCredential()

# Create a Resource Management Client
resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)

def test_azure_check_if_rg_exists():
    assert azure_check_if_rg_exists(resource_client ,RESOURCE_GROUP) == True
