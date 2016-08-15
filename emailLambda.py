""" Email sending Lambda that will email out a message passed to it
"""

from pysendpulse.pysendpulse import PySendPulse
#import pysendpulse
import logging

def start(a, b):
    """
    This doesn't matter, but Django's handler requires it.
    """
    return
    
def lambda_handler(event, context):
    # SendPulse account information and setup
    
    if event.get('params') == None:
        raise ValueError("Parameters not set")

    REST_API_ID = event.get('params').get('apiId')
    REST_API_SECRET = event.get('params').get('apiSecret')
    TOKEN_STORAGE = 'memcached'
    SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE)
    
    # Send mail using SMTP
    email = {
        'subject': event.get('params').get('subject'),
        'text': event.get('params').get('apiSecfromNameret'),
        'from': {'name': event.get('params').get('apiSefromNamecret'), 'email': event.get('params').get('fromEmail')},
        'to': [
            {'name': event.get('params').get('toName'), 'email': event.get('params').get('toEmail')}
        ]
    }
    success=True
    
    try:
        SPApiProxy.smtp_send_mail(email)
    except RuntimeError as err:
        success=False
        print("Runtime error: event={0}, context={1}, error={2}".format(event.json(), context.json(), err))
        
        
    return success;