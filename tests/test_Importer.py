# -*- coding: utf-8 -*-
import unittest
import mocker
import StringIO
from redmine_csv_issues.importer import Importer
from redmine_csv_issues.model import IssueModel
from redmine_csv_issues.source import CsvSource
from redmine_csv_issues.redmine import RedmineHttpTransport, Redmine


class TestImporter(unittest.TestCase):
    INPUT = """\
subject,description
some subject,some description
another subject,another description
"""
    EXPECTED_IDS = ['2', '3']
    MODEL = IssueModel

    def setUp(self):
        self.mocker = mocker.Mocker()
        transport = RedmineHttpTransport('http://fake.url', 'not-important')
        api = Redmine(transport)
        self.importer = Importer(api)

    def _match_request(self, request):
        return request.get_method() == 'POST'

    def testImportFromSource(self):
        urlopen_mock = self.mocker.replace('urllib2.urlopen')
        for id_ in self.EXPECTED_IDS:
            urlopen_mock(mocker.MATCH(self._match_request))
            self.mocker.result(StringIO.StringIO(
                    '{"issue": {"id": %s}}' % id_))
        self.mocker.replay()

        source = CsvSource.from_buffer(StringIO.StringIO(self.INPUT),
                                       self.MODEL)
        results = self.importer.import_from_source(source)
        self.assertEqual(
            list(results),
            self.EXPECTED_IDS)

    def testCsvSource(self):
        source = CsvSource.from_buffer(StringIO.StringIO(self.INPUT),
                                       self.MODEL)
        models = list(source)
        self.assertEqual(models[0]._get_content(),
                         {'description': 'some description',
                          'subject': 'some subject'})
        self.assertEqual(models[1]._get_content(),
                         {'description': 'another description',
                          'subject': 'another subject'})

    def tearDown(self):
        self.mocker.verify()
        self.mocker.restore()


if __name__ == '__main__':
    unittest.main()
