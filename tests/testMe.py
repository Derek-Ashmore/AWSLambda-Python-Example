
from .context import emailLambda

import unittest

class MyTest(unittest.TestCase):
    def test(self):
        event=None
        event.apiId="foo"
        event.apiSecret="foo"
        event.subject="subject"
        event.message="This is a test message"
        event.fromName="tester name"
        event.fromEmail="test@testme.com"
        event.toName="Derek Ashmore"
        event.toEmail="dashmore@force66.com"
        
        context=None
        
        self.assertEquals(True, emailLambda.my_handler(event, context))
        
if __name__ == '__main__':
    unittest.main()