# -*- coding: utf-8 -*-

from thumbor.context import ContextImporter as ThumborContextImporter
from thumbor.utils import logger


class ContextImporter(ThumborContextImporter):

    _community_modules = []

    @classmethod
    def register(cls, name):
        '''Register an item with the importer.

        :param name:
        '''

        cls._community_modules.append(name)

    def __init__(self, context, importer):
        '''
        :param context:
        :param importer:
        '''

        ThumborContextImporter.__init__(self, context, importer)

        # Dynamically load registered modules
        for name in self._community_modules:
            if hasattr(importer, name):
                instance = getattr(importer, name)(context)
                setattr(self, name, instance)
            else:
                logger.warning("Module {name} is not configured.".format(
                    name=name.upper()
                ))
                setattr(self, name, None)
