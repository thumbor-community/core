# -*- coding: utf-8 -*-

# Copyright (c) 2017, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from thumbor.utils import logger
from thumbor.importer import Importer as ThumborImporter


class Importer(object):

    _community_modules = []

    @classmethod
    def register_module(cls, config_key, class_name, multiple=False):
        cls._community_modules.append(dict(
            config_key=config_key,
            class_name=class_name,
            multiple=multiple
        ))

    @classmethod
    def import_community_modules(cls, instance):
        for module in cls._community_modules:
            setattr(instance, module['config_key'].lower(), None)

        # Autoload
        for module in cls._community_modules:
            config_key = module['config_key']

            if hasattr(instance.config, config_key):
                instance.import_item(config_key, module['class_name'])
            else:
                logger.info(
                    "Configuration `{config_key}` not found for module (using default value: `{class_name}`)".format(
                        config_key=config_key,
                        class_name=module['class_name']
                    )
                )
