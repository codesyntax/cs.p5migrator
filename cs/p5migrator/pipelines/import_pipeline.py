from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
from Products.Five.browser import BrowserView
from collective.transmogrifier.transmogrifier import Transmogrifier
from collective.transmogrifier.transmogrifier import configuration_registry


class ImportPipeline(BrowserView):

    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        pipeline_id = 'importp4content'
        pipelines = configuration_registry.listConfigurationIds()
        if pipeline_id is not None and pipeline_id in pipelines:
            transmogrifier = Transmogrifier(self.context)
            transmogrifier(pipeline_id)
            return 'done'

        return 'invalid pipeline'
