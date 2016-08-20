### Email Sending functionality for web sites

This product is designed to manage the sending of an email for a web site "contact us" page or something similar. This Python product was written to be deployed as an AWS Lambda through the AWS API Gateway.

## System Requirements
* SendPulse.com account capable of sending SMTP email.  You'll need the ApiId and ApiSecretKey.
* Python 2.7 or above (may work in other versions, but untested)
* You must include Python dependencies -- the bash script packIt.sh will do that for you.  Usage is ./packIt [temp build directory name]

## Inputs
This application accepts a JSON input.  An example follows below. The Json document can contain more, but must contain at least these fields.

```json
{
    "params": {
        "apiId": "API Id from sendpulse.com",
        "apiSecretId": "Api Secret Key from sendpulse.com",
        "subject": "Test subject",
        "message": "This is a test message - please ignore",
        "fromName": "Throc Morton",
        "fromEmail": "derek.ashmore@dvtconsulting.com",
        "toName": "Break The Monolith",
        "toEmail": "sales@breakthemonolith.guru"
    },
}
```

