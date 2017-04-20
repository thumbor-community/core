# -*- coding: utf-8 -*-

# Copyright (c) 2017, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from thumbor.context import ContextImporter as ThumborContextImporter
from thumbor.utils import logger
from tc_core.importer import Importer


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
                init = getattr(importer, name)
                if not hasattr(init, '__call__'):
                    logger.error("Attr {attr} of object {obj} is not callable".format(
                        attr=name,
                        obj=importer,
                    ))
                instance = getattr(importer, name)(context)
                setattr(self, name, instance)
            else:
                logger.warning("Module {name} is not configured.".format(
                    name=name.upper()
                ))
                setattr(self, name, None)
