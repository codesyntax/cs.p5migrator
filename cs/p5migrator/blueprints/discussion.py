from Acquisition import aq_inner
from collective.transmogrifier.interfaces import ISection
from collective.transmogrifier.interfaces import ISectionBlueprint
from datetime import datetime
from plone.app.discussion.comment import Comment
from plone.app.discussion.interfaces import IConversation
from zope.interface import classProvides
from zope.interface import implements
from DateTime import DateTime

import logging


class DiscussionImporter(object):
    classProvides(ISectionBlueprint)
    implements(ISection)
    """
    Creates comments
    """

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        self.context = transmogrifier.context
        self.logger = logging.getLogger(options['blueprint'])

    def _traverse(self, path):
        return aq_inner(self.context.unrestrictedTraverse(path, None))

    def __iter__(self):
        for item in self.previous:

            if item['_type'] == 'Discussion Item':
                content, conversation, comment_id = item['_path'].rsplit('/', 2)
                content_item = self._traverse(content)
                if content_item is not None:
                    comment = Comment()
                    date = item.get('effective_date')
                    date_obj = DateTime(date).asdatetime()
                    comment.comment_id = int(comment_id)
                    #comment.creation_date = comment.modification_date = date_obj
                    comment.text = item.get('text')
                    comment.mime_type = item.get('text_format')
                    # XXX
                    comment.author_name = item.get('_owner')
                    adapted = IConversation(content_item)
                    adapted.addComment(comment)
                    self.logger.info('Comment added {}'.format(comment_id))

            yield item

