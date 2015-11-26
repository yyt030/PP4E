#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'

import shelve
from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager(name='Tom Doe', age=50, pay=50000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

db.close()
