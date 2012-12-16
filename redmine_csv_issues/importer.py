# -*- coding: utf-8 -*-

class Importer(object):
    def __init__(self, api):
        self.api = api

    def import_from_source(self, source):
        for model in source:
            result = self.api.create(model)
            if result:
                yield model.handle_result(result)
