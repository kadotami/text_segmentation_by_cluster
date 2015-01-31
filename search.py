# -*- coding: utf-8 -*-
import nltk
import sys
import re, pprint
import math
import MeCab
import codecs
import numpy
import scipy
import gensim
reload(sys)
sys.setdefaultencoding('utf-8')


#diff(p) = diff[p-1]
def search(p,s,t,Dst,sid):
  if s == 1:
    sid = numpy.delete(sid,0,0)
    sid = sid-2
    return sid
  else:
    D = Dst[s-1][t-1]
    k = D
    sid[p-s+1]=k
    return search(p,s-1,k,Dst,sid)