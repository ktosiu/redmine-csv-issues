redmine-csv-issues
==================

This library helps with bulk issue creating in Redmine. By default utilizes CSV data source.


Sample usage of command line script:
$ cat input.csv | redimport http://127.0.0.1:3000 4f02a1415bc0ba4290b239ecaea9b3cfc0602c0e

for local Redmine instance with sample auth key.


Input CSV file can look like below.

subject,description
Some issue,This is very important issue
Other issue,Very difficult issue

where CSV heading column names are mapped to issue fields in Redmine.
