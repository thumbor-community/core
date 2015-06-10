# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop

from thumbor.handlers.healthcheck import HealthcheckHandler
from thumbor_community import Extensions


class App(tornado.web.Application):

    def __init__(self, context):
        '''
        :param context: `Context` instance
        '''

        self.context = context

        if self.context.config.get('COMMUNITY_EXTENSIONS', None):
            for extension in self.context.config.get('COMMUNITY_EXTENSIONS'):
                Extensions.load(extension)

        super(App, self).__init__(self.get_handlers())

    def get_handlers(self):
        handlers = [
            (r'/healthcheck', HealthcheckHandler)
        ]

        for extensions in Extensions.extensions:
            for handler in extensions.handlers:
                handlers.append(handler)

        return handlers
