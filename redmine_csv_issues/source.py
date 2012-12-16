# -*- coding: utf-8 -*-
import csv


class Source(object):
    def __init__(self, dict_iter, model_class):
        self.dict_iter = dict_iter
        self.model_class = model_class

    def __iter__(self):
        for dict_ in self.dict_iter:
            yield self.model_class(dict_)

    @classmethod
    def from_buffer(cls, buffer_, model_class):
        lines = cls.get_lines(buffer_)
        headers = cls.get_headers(lines)
        return cls((cls.line2dict(x, headers) for x in lines),
                   model_class)

    @classmethod
    def get_headers(cls, lines):
        raise NotImplementedError

    @classmethod
    def get_lines(cls, buffer_):
        raise NotImplementedError

    @classmethod
    def line2dict(cls, line, headers):
        raise NotImplementedError


class CsvSource(Source):
    @classmethod
    def get_headers(cls, lines):
        line_gen = (x for x in lines)
        try:
            first_line = line_gen.next()
        except StopIteration:
            return []
        return first_line

    @classmethod
    def get_lines(cls, buffer_):
        return csv.reader(buffer_)

    @classmethod
    def line2dict(cls, line, headers):
        return dict(zip(headers, line))
