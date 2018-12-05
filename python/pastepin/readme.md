This program fetch pastes from pastebin and
stores them in the Amazon AWS. The metadata is stored to the DynamoDb
and actual pastes is stored to the S3.

The program used pastebin's
[scraping api](https://pastebin.com/doc_scraping_api)

This API requires Pastebin PRO account and whitelisting IP address
where calls this API.

You need Amazon aws account and user with proper authorization settings.

Follow [Aws lambda documentation](https://aws.amazon.com/premiumsupport/knowledge-center/build-python-lambda-deployment-package/)
when you install it.

You must install following python packages in the deploy zip

* requests
* configparser

You need also .env file where use configure
your Pastebin 
`api_dev_key` and `api_user_key`
You need also add parameter
`limit`. This is used limiting request size. It can be 
integer value between 1 and 250.

