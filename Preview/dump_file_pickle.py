#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import pickle

dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n  ', db[key])
print(db['sue']['name'])
