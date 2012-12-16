# -*- coding: utf-8 -*-
from api import RestApi, CreateResource
from transport import HttpTransport


class RedmineHttpTransport(HttpTransport):
    def __init__(self, url, key):
        super(RedmineHttpTransport, self).__init__(url)
        self.key = key

    def get_headers(self, resource):
        headers = super(RedmineHttpTransport, self).get_headers(resource)
        headers.update({
                'X-Redmine-API-Key': self.key
                })
        return headers


class CreateIssueResource(CreateResource):
    def get_url_parts(self):
        return ['issues.json']

    def get_payload(self):
        return self.model.as_json()

    def get_content_type(self):
        return 'application/json'


class Redmine(RestApi):
    def _get_create_resource(self, model):
        return CreateIssueResource(model)
