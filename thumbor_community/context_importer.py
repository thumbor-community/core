# -*- coding: utf-8 -*-

from thumbor.context import ContextImporter as ThumborContextImporter


class ContextImporter(ThumborContextImporter):

    _community_modules = []

    @classmethod
    def register(cls, name):
        cls._community_modules.append(name)

    def __init__(self, context, importer):
        '''
        :param context:
        :param importer:
        '''

        super(ContextImporter, self).__init__(self, context, importer)

        # Dynamically load registered modules
        for name in self._community_modules:
            if getattr(importer, name):
                instance = getattr(importer, name)(context)
                setattr(self, name, instance)
            else:
                setattr(self, name, None)
