import boto3


session = boto3.Session(profile_name='pastebin_caller',region_name='eu-west-1')

# Let's use Amazon S3
s3 = session.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('test.jpg', 'rb')
s3.Bucket('antero-s3-kori-1').put_object(Key='test.jpg', Body=data)
data.close()