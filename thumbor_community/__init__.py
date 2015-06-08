# -*- coding: utf-8 -*-

from thumbor.context import Context, ContextImporter
from thumbor.importer import Importer


class CommunityExtensions(object):

    @classmethod
    def register_module(cls, config_key, class_name, multiple=False):
        # TODO Maybe pass in a CommunityModule object instead of values?

        CommunityContextImporter.register(config_key.lower())
        CommunityImporter.register_module(config_key, class_name, multiple)


class CommunityContextImporter(ContextImporter):

    __community_modules = []

    @classmethod
    def register(cls, name):
        cls.__community_modules.append(name)

    def __init__(self, context, importer):
        '''
        :param context:
        :param importer:
        '''

        super(CommunityContextImporter, self).__init__(self, context, importer)

        # Dynamically load registered modules
        for name in self.__community_modules:
            if getattr(importer, name):
                instance = getattr(importer, name)(context)
                setattr(self, name, instance)
            else:
                setattr(self, name, None)


class CommunityContext(Context):

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

        super(CommunityContext, self).__init__(
            server=server,
            config=config,
            importer=None,  # Always load our ContextImporter
            request_handler=request_handler
        )

        # Load our ContextImporter
        if importer:
            self.modules = CommunityContextImporter(self, importer)


class CommunityImporter(Importer):

    __community_modules = []

    @classmethod
    def register_module(cls, config_key, class_name, multiple=False):
        cls.__community_modules.append(dict(
            config_key=config_key,
            class_name=class_name,
            multiple=multiple
        ))

    def __init__(self, config):
        '''
        :param config:
        '''
        super(CommunityImporter, self).__init__(config)

        # Autoload
        for module in self.__community_modules:
            setattr(self, module.config_key.lower(), None)

    def import_modules(self):
        super(CommunityImporter, self).import_modules()

        # Autoload
        for module in self.__community_modules:
            if hasattr(self.config, module.config_key):
                self.import_item(module.config_key, module.class_name)
