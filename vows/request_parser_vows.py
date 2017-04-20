# -*- coding: utf-8 -*-

# Copyright (c) 2017, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from pyvows import Vows, expect
from tc_core.web import RequestParser

@Vows.batch
class RequestParserVows(Vows.Context):
    class AnyRequestParser(Vows.Context):
        def topic(self):
            return "/image/unsafe/200x300/image.jpg"

        def should_parse_parameters(self, topic):
            parameters = RequestParser.path_to_parameters(topic)
            expect(parameters).to_include('image')
            expect(parameters).to_include('width')
            expect(parameters).to_include('height')
