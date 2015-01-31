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

#diff(p) = diff[p-2]
def diffs(sent_len,e,alpha):
  diff = numpy.zeros(sent_len-1)
  array = []
  sum = 0
  sum_2 = 0
  for p in xrange(2,sent_len+1):
    num = e[p-2][0]-e[p-1][0]
    diff[p-2] = num
    sum += num
  ave = float(sum/(len(diff)))
  sigma = numpy.std(diff)
  num = 1000000000
  p = 0
  diff_standard = []
  for i,x in enumerate(diff):
    diff_a  = ((x-ave)/sigma)
    diff_standard.append(diff_a)
    if math.fabs(num-alpha) > math.fabs(diff_a-alpha):
      num = diff_a
      p = i #分割数−2
  return p+2
  #pは2から始めっているのでdiff[0]はp=2の値
  #よって、インデックスの+2が本当のpの値