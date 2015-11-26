#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

from initdata import db
import pickle

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
