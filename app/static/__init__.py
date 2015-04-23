from flask.ext.assets import Environment
from . import pipeline
import re

assets = Environment()
assets.register('sass', pipeline.sass)


def register_assets(app):
    assets.init_app(app)
    return assets


def _strip_name(url):
    matches = re.match('.*?([a-zA-Z0-9]+)\.([a-zA-Z0-9]+)', url)
    name = matches.group(1)
    # ext = matches.group(2)
    return name


def urls():
    # Iterate through key in assets
        # Iterate through url in assets[key].urls()
            # Strip out name from url
            # append name -> url to dict
    # return dict
    all_urls = {}

    for bundle in assets:
        for url in bundle.urls():
            name = _strip_name(url)
            all_urls[name] = url

    return all_urls
