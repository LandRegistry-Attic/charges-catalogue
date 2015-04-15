from tests.helpers import with_client, setUpApp, with_context
import unittest

class TestHelloWorld (unittest.TestCase):

    def setUp(self):
        setUpApp(self)


    @with_context
    @with_client
    def test_start_route(self,client):
        res = client.get('/helloworld')
        self.assertEqual(res.status_code, 200)
