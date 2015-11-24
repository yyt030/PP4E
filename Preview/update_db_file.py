#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

from Preview.make_db_file import loadDbase, storeDbase

db = loadDbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
storeDbase(db)
