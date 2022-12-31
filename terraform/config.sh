echo "Starting creating resources"

RESOURCE_GROUP_NAME="Azuredevops"
STORAGE_ACCOUNT_NAME="huent15"
CONTAINER_NAME="huent15"

# Get storage account key
ACCOUNT_KEY=$(az storage account keys list --resource-group $RESOURCE_GROUP_NAME --account-name $STORAGE_ACCOUNT_NAME --query '[0].value' -o tsv)

# Create blob container
az storage container create --name $CONTAINER_NAME --account-name $STORAGE_ACCOUNT_NAME --account-key $ACCOUNT_KEY 80d8Q~JYphu3mDompG8EZdIF4zK37adIO3PDocC7

echo "storage_account_name: $STORAGE_ACCOUNT_NAME"
echo "container_name: $CONTAINER_NAME"
echo "access_key: $ACCOUNT_KEY"
