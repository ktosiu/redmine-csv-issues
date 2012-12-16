# -*- coding: utf-8 -*-
import json


class Model(object):
    def __init__(self, dict_):
        self.dict = dict_

    def _get_name(self):
        raise NotImplementedError

    def _get_content(self):
        return self.dict

    def as_json(self):
        return json.dumps({
                self._get_name(): self._get_content()
                })

    def handle_result(self, result):
        raise NotImplementedError


class IssueModel(Model):
    def _get_name(self):
        return 'issue'

    def handle_result(self, result):
        data_dict = json.loads(result)
        name = self._get_name()
        try:
            id_ = data_dict[name]['id']
        except KeyError:
            return 'UNKNOWN'
        else:
            return str(id_)
