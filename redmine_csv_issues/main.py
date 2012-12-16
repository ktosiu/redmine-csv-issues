# -*- coding: utf-8 -*-
import sys
from redmine import Redmine, RedmineHttpTransport
from source import CsvSource
from model import IssueModel
from importer import Importer


def main():
    try:
        url, key = sys.argv[1:]
    except (IndexError, ValueError):
        sys.stderr.write('Usage: %s <redmine_url> <auth_key>\n'
                         % sys.argv[0])
        sys.exit(1)

    transport = RedmineHttpTransport(url, key)
    api = Redmine(transport)
    importer = Importer(api)
    source = CsvSource.from_buffer(sys.stdin.readlines(),
                                   IssueModel)
    results = importer.import_from_source(source)
    print 'Created issue ids:', ', '.join(results)


if __name__ == '__main__':
    main()
