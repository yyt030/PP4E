#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

from Preview.make_db_file import loadDbase

db = loadDbase()

for key in db:
    print(key, '=>\n ', db[key])

print(db['sue']['name'])
