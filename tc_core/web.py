# -*- coding: utf-8 -*-

# Copyright (c) 2017, thumbor-community
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

import re
from libthumbor.url import Url
import tornado.web

if hasattr(tornado.web, '_unquote_or_none'):
    from tornado.web import _unquote_or_none
else:
    from tornado.routing import _unquote_or_none

class RequestParser(object):

    _url_regex = None

    @classmethod
    def path_to_parameters(cls, path):
        '''
        :param path: url path
        :return: A dictionary of parameters to be used with
                ImagingHandler instances
        '''
        if not cls._url_regex:
            cls._url_regex = re.compile(Url.regex())

        if cls._url_regex.groups:
            match = cls._url_regex.match(path)

            # See https://github.com/tornadoweb/tornado/blob/01c78ebfcc993ff4f1d8336c2c45844fe9dab60e/tornado/web.py#L1951
            # Pass matched groups to the handler.  Since
            # match.groups() includes both named and
            # unnamed groups, we want to use either groups
            # or groupdict but not both.
            if cls._url_regex.groupindex:
                parameters = dict(
                    (str(k), _unquote_or_none(v))
                    for (k, v) in match.groupdict().items())
            else:
                parameters = [
                    _unquote_or_none(s)
                    for s in match.groups()
                ]
        else:
            parameters = dict()

        return parameters
