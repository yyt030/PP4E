#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import shelve

db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n', db[key].name, db[key].pay)