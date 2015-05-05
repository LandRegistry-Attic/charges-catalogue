from tests.helpers import with_client, setUpApp, with_context
import unittest
import mimetypes


class TestGovukAssets (unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    @with_client
    def test_image(self, client):
        res = client.get('/template/assets/images/favicon.ico')
        self.assertEqual(res.status_code, 200)
        icon_type = mimetypes.guess_type('favicon.ico')[0]
        self.assertIn(icon_type, res.headers['Content-Type'])

    @with_context
    @with_client
    def test_css(self, client):
        res = client.get('/template/assets/stylesheets/govuk-template.css')
        self.assertEqual(res.status_code, 200)
        css_type = mimetypes.guess_type('govuk-template.css')[0]
        self.assertIn(css_type, res.headers['Content-Type'])

    @with_context
    @with_client
    def test_js(self, client):
        res = client.get('/template/assets/javascripts/govuk-template.js')
        self.assertEqual(res.status_code, 200)
        js_type = mimetypes.guess_type('govuk-template.js')[0]
        self.assertIn(js_type, res.headers['Content-Type'])
