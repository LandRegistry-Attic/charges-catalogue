from flask_stache import render_view
from govuk_template.flask.mustache import GovukTemplate


class Template (object):
    assetPath = '/assets/'

    def render(self):
        return GovukTemplate().render(self, content=render_view(self))
