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

def minimum_costs(y,term_costs,costs,topic_num):
  e = numpy.zeros((y,y))  #論文のe(p,q)=e[p-1][q-1]
  D = numpy.zeros((y,y))  #論文のDp,q=D[p-1][q-1]
  for q in xrange(1,y+1):    #1~y
    e[0][q-1] = term_costs[q-1][y-1]
  if topic_num < 1:
    for p in xrange(2,y+1):                  #2~y
      min = 1000000000
      D_r = []
      for q in xrange(1,y-p+2):              #1~y-p+1
        for r in xrange(q+1,y-p+3):          #q+1~y-p+2
          num = term_costs[q-1][r-2]+e[p-2][r-1]
          if min > num:
            min = num
            D_r = r
        e[p-1][q-1] = min
        D[p-1][q-1] = D_r
    return [e,D]
  else:
    for p in xrange(2,y+1):                  #2~y
      min = 1000000000
      D_r = []
      for q in xrange(1,y-p+2):              #1~y-p+1
        for r in xrange(q+1,y-p+3):
          num = term_costs[q-1][r-2]+e[p-2][r-1]
          if min > num:
            min = num
            D_r = r
        e[p-1][q-1] = min
        D[p-1][q-1] = D_r
        if p == topic_num and q == 1:
          return [e,D]


