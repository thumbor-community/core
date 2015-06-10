# -*- coding: utf-8 -*-
from thumbor.importer import Importer as ThumborImporter


class Importer(ThumborImporter):

    _community_modules = []

    @classmethod
    def register_module(cls, config_key, class_name, multiple=False):
        cls._community_modules.append(dict(
            config_key=config_key,
            class_name=class_name,
            multiple=multiple
        ))

    def __init__(self, config):
        '''
        :param config:
        '''
        super(Importer, self).__init__(config)

        # Autoload
        for module in self._community_modules:
            setattr(self, module.config_key.lower(), None)

    def import_modules(self):
        super(Importer, self).import_modules()

        # Autoload
        for module in self._community_modules:
            if hasattr(self.config, module.config_key):
                self.import_item(module.config_key, module.class_name)
