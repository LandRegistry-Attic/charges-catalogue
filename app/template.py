from flask_stache import render_view
from govuk_template.flask.mustache import GovukTemplate


class Template (object):
    def render (self):
        return GovukTemplate().render(content=render_view(self))
