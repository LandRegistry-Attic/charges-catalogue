from tests.helpers import with_client, setUpApp, with_context
import unittest


class TestGovukAssets (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_image(self, client):
        res = client.get('/template/assets/images/favicon.ico')
        self.assertEqual(res.status_code, 200)
        self.assertTrue("image/x-icon" in res.headers['Content-Type'])

    @with_context
    @with_client
    def test_css(self, client):
        res = client.get('/template/assets/stylesheets/govuk-template.css')
        self.assertEqual(res.status_code, 200)
        self.assertTrue("text/css" in res.headers['Content-Type'])

    @with_context
    @with_client
    def test_js(self, client):
        res = client.get('/template/assets/javascripts/govuk-template.js')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(
            "application/javascript" in res.headers['Content-Type']
        )
