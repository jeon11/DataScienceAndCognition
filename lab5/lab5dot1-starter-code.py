import matplotlib.pyplot as plt
import collections
import re
import numpy as np
import scipy.stats as ss #scipy
from itertools import tee, islice

# Code for obtaining ngram counts with inputs of "lst" = a list and "n" = n-gram order, e.g. n=2 -> digram counts
def ngrams(lst, n):
  tlst = lst
  while True:
    a, b = tee(tlst)
    l = tuple(islice(a, n))
    if len(l) == n:
      yield l
      next(b)
      tlst = b
    else:
      break

#########################
# Load file (data from Project Gutenberg)
novelfile = "ulysses.txt";
with open(novelfile, 'r') as f:
    alltext = f.read()

# Take out all non-letters and remove spaces
regex = re.compile('[^a-zA-Z]')
alltext = regex.sub('', alltext)

# Lower case all letters
lowtext = alltext.lower();


#########################
# Compute 1-gram entropy based on the preprocessed text file "lowtext" (hint: use 'collections.Counter()' function):
# H(i) = - sum_i p(i) log2 p(i), where i is a letter in the English alphabet

# Your code here
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def entropy1(txt, alphabets):
  k, prob_i = 0, 0 
  lst = collections.Counter(txt)
  length = len(txt)
  while k in range(0,len(alphabets)):
    prob_i = lst[alphabets[k]]/length
    k += 1
    H = - prob_i*((prob_i)**0.5)
  return H #entropy 

H = entropy1(lowtext, alphabets)
#-7.010627085477864e-05
print('One-gram entropy of letters is estimated to be ',H,'bits.')

#########################
# Compute di-gram entropy based on the preprocessed text file "lowtext" and "ngrams()" function:
# H(i|i-1) = H(i,i-1) - H(i-1)

# Your code here
def digram_entropy(txt, alphabets):
  k, prob_i = 0, 0
  lst = collections.Counter(txt)
  length = len(txt)
  while k in range(0, len(alphabets)):
    prob_x = lst[alphabets[k]]/length
    prob_y = lst[alphabets[k-1]]/length
    prob_cond = ((prob_y)*(prob_x))/(prob_x)
    prob_joint = prob_x*prob_cond
    k += 1
    H = - prob_joint*((prob_cond)**0.5)
  return H #entropy 

digram_H = digram_entropy(lowtext,alphabets)
#-6.174101451477135e-06
print('Di-gram entropy of letters is estimated to be ',digram_H,'bits.')


