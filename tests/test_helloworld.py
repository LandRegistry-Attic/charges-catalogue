from tests.helpers import with_client, setUpApp, with_context
import unittest
from lxml.html import document_fromstring

class TestHelloWorld (unittest.TestCase):

    def setUp(self):
        setUpApp(self)


    @with_context
    @with_client
    def test_start_route(self,client):
        res = client.get('/helloworld')
        html = document_fromstring(res.get_data())

        self.assertEqual(res.status_code, 200)

        header = ''.join(html.xpath('//header//a/text()'))
        self.assertTrue('GOV.UK' in header)
