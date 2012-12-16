# -*- coding: utf-8 -*-
import urllib2
import logging


class RequestWithMethod(urllib2.Request):
    def __init__(self, method, *args, **kwargs):
        # must be type, not classobj :(
        urllib2.Request.__init__(self, *args, **kwargs)
        self._method = method

    def get_method(self):
        return self._method


class Transport(object):
    def open(self, resource):
        raise NotImplementedError


class HttpTransport(Transport):
    def __init__(self, url):
        self.url = url

    def get_url(self, resource):
        s = '/'
        return s.join([x.strip(s)
                       for x in [self.url] + resource.get_url_parts()])

    def get_headers(self, resource):
        return {
            'Content-type': resource.get_content_type()
            }

    def open(self, resource):
        url = self.get_url(resource)
        data = resource.get_payload()
        headers = self.get_headers(resource)
        request = RequestWithMethod(resource.get_method(),
                                    url, data, headers)

        try:
            res = urllib2.urlopen(request)
        except HTTPError, e:
            logging.error('HTTP error (%s):', (url, e.code))
            logging.debug(e.read())
        except URLError, e:
            logging.error('URL error:', e.reason)
        else:
            return res.read()
