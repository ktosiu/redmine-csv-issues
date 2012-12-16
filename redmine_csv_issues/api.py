# -*- coding: utf-8 -*-

class Resource(object):
    def __init__(self, model):
        self.model = model

    def get_method(self):
        return 'GET'

    def get_url_parts(self):
        raise NotImplementedError

    def get_payload(self):
        raise NotImplementedError

    def get_content_type(self):
        raise NotImplementedError


class CreateResource(Resource):
    def get_method(self):
        return 'POST'
    

class Api(object):
    def create(self, model):
        raise NotImplementedError


class RestApi(object):
    def __init__(self, transport):
        self.transport = transport

    def _get_create_resource(self, model):
        raise NotImplementedError

    def create(self, model):
        return self.transport.open(
            self._get_create_resource(model))
