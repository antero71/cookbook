from s3.s3Session import s3Session

def storeDataToS3(name,data):
    # Let's use Amazon S3
    s3session = s3Session()
    #session = s3session.getSession()
    s3 = s3session.getS3()

    s3.Bucket('antero-s3-kori-1').put_object(Key='pastebin/'+name, Body=data)


