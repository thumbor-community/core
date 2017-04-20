# -*- coding: utf-8 -*-

# Copyright (c) 2017, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from thumbor.context import Context as ThumborContext
from thumbor.filters import FiltersFactory
from thumbor.metrics.logger_metrics import Metrics
from tc_core.context_importer import ContextImporter


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

        ThumborContext.__init__(
            self,
            server=server,
            config=config,
            importer=None,  # Always load our ContextImporter
            request_handler=request_handler
        )

        # Load our ContextImporter
        if importer:
            self.modules = ContextImporter(self, importer)
            self.filters_factory = FiltersFactory(self.modules.filters)
            if importer.metrics:
                self.metrics = importer.metrics(config)
            else:
                self.metrics = Metrics(config)

    @classmethod
    def from_context(cls, context, request_handler=None):
        return Context(
            context.server,
            context.config,
            context.modules.importer,
            request_handler=request_handler
        )
