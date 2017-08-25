#lab 5.2 
#JinYoungJeon (SID: 23051612)
#CogSci190
import pickle 
import codecs
#Distribution 1 & Uniform: 
#Here we see only the 0th quartile to be on the y = x graph,
#while both extremes are off y = x. If a normal distribution has all the
#data point on y = x, the two extremes here show that each end of the distribution
#has many data unlike the tips of the normal curve. 

#Distribution 2 & Normal: 
#When the two distribution are from same population, 
#we see a distribution in qq plot to fit on the y = x plot. 
#Even though some points are off at the low tip of the graph, 
#most of the points are on y =x, telling that it is a normal distribution.

#Distribution 3 & Beta:
#Here the distribution generally appears to have a bell shape, yet the tail is 
#on the right with a shape skewed right. This can be shown that on the right tail
#part of the distribution, it matches more like the normal distribution, while the 
#left part of the distribution is unusually higher than it should be in a normal distributino.
#Such change is shown as the left tail of Distribution 3 is off the y = x. 

#Distribution 4 & t:
#While both normal and t distribution show a normal curve, the t distribution has a 
#fatter tail than the normal distribution. Therefore, each tail of the QQ plot is a little
#off from y = x as shown in Distribution 4. 

# with open('gau1d.pickle', 'rb') as f:
# 	pickle.load(f)

# file = open('gau1d.pickle', 'rb').read()
# pickle.load('file')

file_gau1d = open('gau1d.pickle', 'rb')
gau1d = file_gau1d.read()
text1 = gau1d.decode("utf8")

# file_gau1d = codecs.open('gau1d.pickle', 'rb')
# file_gau1d = 
# gau1d = pickle.load(file_gau1d)
# gau1d 

# with open('gau1d.pickle', 'rb') as f: 



