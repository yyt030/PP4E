#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'
from initdata import bob, sue, tom

import pickle

for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()
