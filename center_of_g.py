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

def M(sentences,model):
  array = []
  for sentence in sentences:
    m = numpy.zeros(200)
    for word in sentence:
      vec = model[word]
      m += vec
    if len(sentence) == 0:
      array.append(numpy.zeros(200))
    else:
      array.append(m/len(sentence))
  return array