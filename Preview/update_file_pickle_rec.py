#!/usr/bin/env python
# coding: utf8
__author__ = 'yueyt'
import pickle

suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()

sue['pay'] *= 1.10
suefile = open('sue.pkl', 'wb')
pickle.dump(sue, suefile)