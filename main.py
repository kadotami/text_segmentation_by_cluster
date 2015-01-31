# -*- coding: utf-8 -*-
import nltk
import sys
import re
import math
import MeCab
import codecs
import numpy
import scipy
import gensim
reload(sys)
sys.setdefaultencoding('utf-8')
import vol
import center_of_g
import cost
import term_cost
import minimum_cost
import diff
import search
import f_measure


def divide_sentence_comp(text):
  lines = text.split('\n')
  sentences=[]
  for line in lines:
    parentheses = 0
    tagger=MeCab.Tagger("-Ochasen")
    encoded_text = line.encode('utf-8')
    node = tagger.parseToNode(encoded_text)
    sentence = ''
    while node:
      surface = node.surface
      feature = node.feature
      speech = feature.split(",")[0]
      figure_kind = feature.split(",")[1]
      if re.match(r'.*。.*',surface) and parentheses == 0:
        sentence += surface
        sentences.append(sentence)
        sentence = ''
        parentheses = 0
        node = node.next
        continue
      if re.match(r'.*「.*',surface):
        parentheses = parentheses + 1
      if re.match(r'.*」.*',surface):
        parentheses = parentheses - 1
      sentence += surface
      node = node.next
  return sentences

def make_word_array(paragraph):
  paragraph_array = []
  for line in paragraph:
    sentence_array = []
    tagger=MeCab.Tagger("-Ochasen -b 800000000")
    node = tagger.parseToNode(line)
    while node:
      surface = node.surface
      feature = node.feature
      source = feature.split(",")[6]
      speech = feature.split(",")[0]
      word_kind = feature.split(",")[1]
      if word_kind in [r'接尾',r'副詞可能',r'代名詞',r'数',r'非自立']:
        pass
      elif speech in [r'名詞',r'動詞',r'形容詞']:
        if source == "*":
          word = surface
        else:
          word = source
        word = unicode(word,'utf-8')
        try:
          model[word]# ここで単語ベクトル内にwordがあるかどうかみる
          sentence_array.append(word)
        except:
          pass
      node = node.next
    paragraph_array.append(sentence_array)
  return paragraph_array

def print_document(sentences,output):
  i = 0
  for v in sentences:
    words = ''
    for word in v:
      words = words + word
    print words
    if i in output:
      print "\n\n----------------------キリトリセン-----------------------\n\n"
    i += 1


if __name__ == "__main__":
  alpha = 1.2 # 論文のパラメータです
  argvs = sys.argv
  model_name = argvs[1]
  model_dimention = argvs[2]
  input_file = argvs[3]
  model = gensim.models.Word2Vec()
  model = model.load_word2vec_format('../data/jawiki-nonum.bin', binary=True)
  text = codecs.open(input_file,'r','utf-8').read()
  sentences = divide_sentence_comp(text)
  word_array = make_word_array(sentences)
  vols = vol.vols(word_array)
  M = center_of_g.M(word_array,model)
  costs = cost.costs(word_array,M,model)
  sent_len = len(word_array)

  term_costs = term_cost.term_costs(sent_len,vols,M,costs)
  if len(argvs) > 4:
    minimum_costs = minimum_cost.minimum_costs(sent_len,term_costs,costs,int(argvs[4]))
    e = minimum_costs[0]
    D = minimum_costs[1]
    p = int(argvs[4])
  else:
    minimum_costs = minimum_cost.minimum_costs(sent_len,term_costs,costs,0)
    e = minimum_costs[0]
    D = minimum_costs[1]
    p = diff.diffs(sent_len,e,alpha)
  sid = numpy.zeros(p)
  output = search.search(p,p,1,D,sid)
  print_document(sentences,output)



