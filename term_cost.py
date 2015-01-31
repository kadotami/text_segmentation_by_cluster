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

#論文で言うcost(i,j)はこの配列のterm_costs[i-1,j-1]で帰ってくる
def term_costs(y,vols,M,costs):
  term_costs = numpy.zeros((y,y))
  for x in xrange(1,y+1):
    term_costs[x-1][x-1] = costs[x-1]
  for i in range(1,y):                 #1~y-1
    vol_i_j_1 = vols[i-1]               #vol(i,j-1)
    M_i_j_1 = M[i-1]
    cost_i_j_1 = costs[i-1]
    for j in range(i+1,y+1):                #i+1~y
      sub = M_i_j_1-M[j-1]
      norm = numpy.linalg.norm(sub)
      vol_i_j = vol_i_j_1+vols[j-1]
      if vol_i_j == 0:
        term_costs[i-1][j-1] = 0
        M_i_j_1 =0
      else:
        term_costs[i-1][j-1] = cost_i_j_1 + costs[j-1] + ((vol_i_j_1*vols[j-1])/vol_i_j)*(norm*norm)
        M_i_j_1 = ((vol_i_j_1*M_i_j_1) + (vols[j-1]*M[j-1]))/vol_i_j
      vol_i_j_1 = vol_i_j
      cost_i_j_1 = term_costs[i-1][j-1]
  return term_costs