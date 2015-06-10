# -*- coding: utf-8 -*-

from thumbor.context import Context as ThumborContext


class Context(ThumborContext):

    def __init__(self, server=None, config=None, importer=None,
                 request_handler=None):
        '''
        Class responsible for containing:
        * Server Configuration Parameters (port, ip, key, etc);
        * Configurations read from config file (or defaults);
        * Importer with imported modules (engine, filters, detectors, etc);
        * Request Parameters (width, height, smart, meta, etc).

        Each instance of this class MUST be unique per request.
        This class should not be cached in the server.

        :param server:
        :param config:
        :param importer:
        :param request_handler:
        '''

        super(Context, self).__init__(
            server=server,
            config=config,
            importer=None,  # Always load our ContextImporter
            request_handler=request_handler
        )

        # Load our ContextImporter
        if importer:
            self.modules = ContextImporter(self, importer)


