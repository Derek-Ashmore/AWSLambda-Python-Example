""" Email sending Lambda that will email out a message passed to it
"""

from pysendpulse import PySendPulse
import logging
    
def my_handler(event, context):
    # SendPulse account information and setup
    REST_API_ID = event['apiId']
    REST_API_SECRET = event['apiSecret']
    TOKEN_STORAGE = 'memcached'
    SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE)
    
    # Send mail using SMTP
    email = {
        'subject': event['subject'],
        'text': event['message'],
        'from': {'name': event['fromName'], 'email': event['fromEmail']},
        'to': [
            {'name': event['toName'], 'email': event['toEmail']}
        ]
    }
    success=True
    
    try:
        SPApiProxy.smtp_send_mail(email)
    except RuntimeError as err:
        success=False
        print("Runtime error: event={0}, context={1}, error={2}".format(event.json(), context.json(), err))
        
        
    return success;