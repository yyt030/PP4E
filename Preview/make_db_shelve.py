#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'
from initdata import bob, sue

import shelve

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()
