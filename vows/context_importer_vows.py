# -*- coding: utf-8 -*-

# Copyright (c) 2017, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from pyvows import Vows, expect
from tc_core import ContextImporter

class Importer(object):
    engine = False
    gif_engine = False
    storage = False
    result_storage = False
    upload_photo_storage = False
    loader = False
    url_signer = False
    detectors = []
    filters = []
    optimizers = []
    compatibility_legacy_loader = None
    compatibility_legacy_storage = None
    compatibility_legacy_result_storage = None


class Extension(object):

    def __init__(self, context): pass

@Vows.batch
class ContextImporterVows(Vows.Context):
    class AContextImporter(Vows.Context):
        def topic(self):
            ContextImporter.register('my_extension')

            importer = Importer
            return ContextImporter('context', importer)

        def should_be_context_importer(self, topic):
            expect(topic).to_be_instance_of(ContextImporter)

    class AFilledInContextImporter(Vows.Context):
        def topic(self):
            ContextImporter.register('my_extension')

            importer = Importer
            ext = Extension
            setattr(importer, 'my_extension', ext)
            return ContextImporter('context', importer)

        def should_be_context_importer(self, topic):
            expect(topic).to_be_instance_of(ContextImporter)
