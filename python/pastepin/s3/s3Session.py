import boto3

class s3Session():
    def __init__(self,profile_name='pastebin_caller',region_name='eu-west-1'):
        """ This initialize class for defaul values"""
        "profile_name='pastebin_caller',region_name='eu-west-1',table_name='pastebin'"
        self.session = boto3.Session(profile_name=profile_name,region_name=region_name)
        self.s3 = self.session.resource('s3')

    def getSession(self):
        """This function returns a session for initialized aws region and user profile"""
        return self.session

    def getS3(self):
        """ Get S3 resource """
        return self.s3