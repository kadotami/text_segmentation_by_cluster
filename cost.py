# -*- coding: utf-8 -*-
import nltk
import sys
import re, pprint
import math
import codecs
import numpy
import scipy
import gensim
reload(sys)
sys.setdefaultencoding('utf-8')

def costs(sentences,M,model):
  array = []
  for sentence,m in zip(sentences,M):
    sum = 0
    for word in sentence:
      sub = model[word] - m
      norm = numpy.linalg.norm(sub)
      sum += (norm*norm)
    array.append(sum)
  return array