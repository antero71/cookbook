import boto3
# Get the service resource.

session = boto3.Session(profile_name='pastebin_caller',region_name='eu-west-1')

dynamodb = session.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='pastebin',
    KeySchema=[
        {
            'AttributeName': 'key',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'scrape_url',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'scrape_url',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'key',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='pastebin')

# Print out some data about the table.
print(table.item_count)