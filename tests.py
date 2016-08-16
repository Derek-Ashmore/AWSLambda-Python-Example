
import emailLambda
import unittest
import json

class MyTest(unittest.TestCase):
    def test(self):
        
        # Note that you need to provide a sendpulseKeys.json file for this test to work. See README.md
        keyInfo = None
        with open('sendpulseKeys.json') as json_data:
            keyInfo = json.load(json_data)
    
        event = {
            "body": "",
            "headers": {
                "Via": "1.1 e604e934e9195aaf3e36195adbcb3e18.cloudfront.net (CloudFront)",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip",
                "CloudFront-Is-SmartTV-Viewer": "false",
                "CloudFront-Forwarded-Proto": "https",
                "X-Forwarded-For": "109.81.209.118, 216.137.58.43",
                "CloudFront-Viewer-Country": "CZ",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "X-Forwarded-Proto": "https",
                "X-Amz-Cf-Id": "LZeP_TZxBgkDt56slNUr_H9CHu1Us5cqhmRSswOh1_3dEGpks5uW-g==",
                "CloudFront-Is-Tablet-Viewer": "false",
                "X-Forwarded-Port": "443",
                "CloudFront-Is-Mobile-Viewer": "false",
                "CloudFront-Is-Desktop-Viewer": "true",
            },
            "method": "POST",
            "params": {
                "apiId": keyInfo.get('apiId'),
                "apiSecretId": keyInfo.get('apiSecretId'),
                "subject": "Test subject",
                "message": "This is a test message - please ignore",
                "fromName": "Throc Morton",
                "fromEmail": "derek.ashmore@dvtconsulting.com",
                "toName": "Break The Monolith",
                "toEmail": "sales@breakthemonolith.guru"
            },
            "command": "emailContact",
        }
        
        context={
            "stubbed" : "out"
        }
        
        self.assertEquals(True, emailLambda.lambda_handler(event, context))
        
if __name__ == '__main__':
    unittest.main()