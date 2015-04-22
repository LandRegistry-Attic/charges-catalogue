from flask_stache import render_view
from govuk_template.flask.mustache import GovukTemplate


class View(object):

    def render(self):
        return render_view(self)


class PropositionHeader(View):

    def __init__(self, serviceName):
        self.serviceName = serviceName


class CookieMessage(View):
    pass


class Base(View):

    def __init__(self, view):
        self.view = view
        self.pageTitle = view.pageTitle
        self.content = render_view(view)


class Template (object):
    pageTitle = 'A Blank Page'
    assetPath = '/template/assets/'
    serviceName = 'Service Name'
    headerClass = 'with-proposition'

    def cookieMessage(self):
        return CookieMessage().render()

    def propositionHeader(self):
        return PropositionHeader(self.serviceName).render()

    def render(self):
        return GovukTemplate().render(
            self,
            content=Base(self).render(),
            pageTitle=self.pageTitle + ' - ' + self.serviceName
        )
