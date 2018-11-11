from database.databaseSession import DynamoDbSession


def storeData(jsonDoc):
    """This function stores data (dict) to the Amazon aws dynamodb database"""
    dbSession = DynamoDbSession()
    session = dbSession.getSession()

    dynamodb=session.resource('dynamodb')

    table = dynamodb.Table('pastebin')

    table.put_item(
        Item=jsonDoc
    )