from tests.helpers import setUpApp, with_context
import unittest
from flask.ext.assets import Bundle
from app.static import urls, _strip_name, assets


class TestStaticAssets(unittest.TestCase):

    def setUp(self):
        setUpApp(self)

    @with_context
    def test_url(self):
        assetsUrls = urls()
        self.assertIn('main', assetsUrls)

        main = assetsUrls['main']
        self.assertIn('/static/gen/main.css', main)

    @with_context
    def test_dynamic_adding_bundle(self):
        customBundle = Bundle('sass/main.scss',
                              output='gen/foo.bar')
        assets.register('custom', customBundle)

        assetsUrls = urls()
        self.assertIn('foo', assetsUrls)

    def test_strip_name_from_url(self):
        self.assertEqual('main', _strip_name('main.css'))
        self.assertEqual('main', _strip_name('/static/main.css'))
        self.assertEqual('main', _strip_name('/static/main.css?12345'))

        self.assertEqual('foo', _strip_name('foo.bar'))
        self.assertEqual('foo', _strip_name('/static/foo.bar'))
        self.assertEqual('foo', _strip_name('/static/foo.bar?12345'))
