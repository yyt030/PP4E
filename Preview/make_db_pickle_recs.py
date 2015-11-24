#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'
from Preview.initdata import bob, sue, tom

import pickle

for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()
