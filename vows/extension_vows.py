# -*- coding: utf-8 -*-

# Copyright (c) 2017, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from pyvows import Vows, expect

from thumbor.handlers.healthcheck import HealthcheckHandler
from tc_core import Extension, Extensions
from tc_core.context_importer import ContextImporter
from tc_core.importer import Importer

@Vows.batch
class ExtensionVows(Vows.Context):
    class AnExtension(Vows.Context):
        def topic(self):
            myExt = Extension('myExtension')
            myExt.add_module(config_key='key', class_name='class', multiple=False)
            myExt.add_handler('/my_route', HealthcheckHandler)
            return myExt

        class WhenRegistered(Vows.Context):
            def topic(self, extension):
                return Extensions.register(extension)

            def should_be_stored(self, topic):
                expect(Extensions.extensions).Not.to_be_empty()

            def should_be_in_context(self, topic):
                expect(ContextImporter._community_modules).Not.to_be_empty()
                expect(ContextImporter._community_modules).to_include('key')

            def should_be_in_importer(self, topic):
                expect(Importer._community_modules).Not.to_be_empty()
                expect(Importer._community_modules).to_include(dict(
                    config_key='key',
                    class_name='class',
                    multiple=False
                ))
