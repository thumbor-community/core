# -*- coding: utf-8 -*-

# Copyright (c) 2017, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

import sys


from pyvows import Vows, expect
from tc_core import Extension, Extensions
from tc_core.app import App
from tc_core.context import Context
from thumbor.config import Config
from thumbor.importer import Importer
from thumbor.handlers.imaging import ImagingHandler


@Vows.batch
class AppVows(Vows.Context):
    class AnApp(Vows.Context):
        def topic(self):
            config   = Config()
            importer = Importer(config)

            context = Context(None, config, importer)
            return App(context)

        def should_be_App(self, topic):
            expect(topic).to_be_instance_of(App)

    class AnAppWithExtensions(Vows.Context):
        def topic(self):
            config   = Config()
            importer = Importer(config)
            config.__setitem__('COMMUNITY_EXTENSIONS', ['tc_core'])

            ext = Extension('tc_core')
            ext.add_handler('/my_handler', ImagingHandler)
            Extensions.register(ext)

            context = Context(None, config, importer)
            return App(context)

        def should_be_App(self, topic):
            expect(topic).to_be_instance_of(App)

        def should_load_core(self, topic):
            expect(sys.modules.keys()).to_include('tc_core')
