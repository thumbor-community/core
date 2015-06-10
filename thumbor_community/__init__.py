# -*- coding: utf-8 -*-

import importlib

from thumbor_community.context_importer import ContextImporter
from thumbor_community.importer import Importer


class Extensions(object):

    extensions = []

    @classmethod
    def load(cls, name):
        '''Load the given extension

        :param name: The extension package name.
        '''

        importlib.import_module(name)

    @classmethod
    def register(cls, extension):
        cls.extensions.append(extension)

        for module in extension.modules:
            cls.register_module(**module)

    @classmethod
    def register_module(cls, config_key, class_name, multiple=False):
        ContextImporter.register(config_key.lower())
        Importer.register_module(config_key, class_name, multiple)


class Extension(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.handlers = []

    def add_module(self, config_key, class_name, multiple):
        self.modules.append(dict(
            config_key=config_key,
            class_name=class_name,
            multiple=multiple
        ))

    def add_handler(self, route, handler):
        self.handlers.append((route, handler))
