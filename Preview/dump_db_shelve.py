#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import shelve

db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n', db[key])