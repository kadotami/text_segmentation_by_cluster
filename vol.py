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

def vols(sentences):
  array = []
  for sentence in sentences:
    array.append(len(sentence))
  return array