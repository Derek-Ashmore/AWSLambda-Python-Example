""" Email sending Lambda that will email out a message passed to it
"""

from pysendpulse.pysendpulse import PySendPulse
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
    REST_API_SECRET = event.get('params').get('apiSecretId')
    TOKEN_STORAGE = 'FILE'
    
    try:
        SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE)
    except Exception as err:
        print("Runtime error: REST_API_ID={0}, REST_API_SECRET={1}, event={2}, context={3}, error={4}".format(REST_API_ID, REST_API_SECRET, event, context, err))
        raise err
    
    # Send mail using SMTP
    email = {
        'subject': event.get('params').get('subject'),
        'text': event.get('params').get('message'),
        'html': event.get('params').get('message'),
        'from': {'name': event.get('params').get('fromName'), 'email': event.get('params').get('fromEmail')},
        'to': [
            {'name': event.get('params').get('toName'), 'email': event.get('params').get('toEmail')}
        ]
    }
    success=True
    
    try:
        SPApiProxy.smtp_send_mail(email)
    except Exception as err:
        success=False
        print("Runtime error: event={0}, context={1}, error={2}".format(event, context, err))
        
        
    return success;