import boto3


class DynamoDbSession():
    def __init__(self, profile_name='pastebin_caller', region_name='eu-west-1', table_name='pastebin'):
        """This initialize class for default values"""
        "profile_name='pastebin_caller',region_name='eu-west-1',table_name='pastebin'"
        self.session = boto3.Session(profile_name=profile_name, region_name=region_name)
        self.dynamodb = self.session.resource('dynamodb')

    def getSession(self):
        """This function returns a session for initialized aws region and user profile"""
        return self.session

    def getDynamoDb(self):
        return self.dynamodb
