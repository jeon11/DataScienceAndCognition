import numpy as np
import matplotlib.pyplot as plt
import math
from tabulate import tabulate
import scipy as sc

mu1, sigma1 = 0, 1
mu2, sigma2 = 10, 1
mu3, sigma3 = 0, 10
mu4, sigma4 = 10, 10

s1 = np.random.normal(mu1, sigma1, 100000)
s2 = np.random.normal(mu2, sigma2, 100000)
s3 = np.random.normal(mu3, sigma3, 100000)
s4 = np.random.normal(mu4, sigma4, 100000)

hist1 = np.histogram(s1, bins=100, range=(-20,20), density=True)
# print(hist1) #lists array of data that adds up to 1
data1 = np.trim_zeros(hist1[0]) #trims out the zero values
ent1 = -(data1*np.log(np.abs(data1))).sum() 
print("entropy for example 1 is:", ent1) #3.56108941738

hist2 = np.histogram(s2, bins=100, range=(-20,20), density=True)
# print(hist2) #lists array of data that adds up to 1
data2 = np.trim_zeros(hist2[0]) #trims out the zero values
ent2 = -(data2*np.log(np.abs(data2))).sum() 
print("entropy for example 2 is:", ent2) #3.55136926537

hist3 = np.histogram(s3, bins=100, range=(-20,20), density=True)
# print(hist3) #lists array of data that adds up to 1
data3 = np.trim_zeros(hist3[0]) #trims out the zero values
ent3 = -(data3*np.log(np.abs(data3))).sum() 
print("entropy for example 3 is:", ent3) #8.90450371361

hist4 = np.histogram(s4, bins=100, range=(-20,20), density=True)
# print(hist4) #lists array of data that adds up to 1
data4 = np.trim_zeros(hist4[0]) #trims out the zero values
ent4 = -(data4*np.log(np.abs(data4))).sum() 
print("entropy for example 4 is:", ent4) #8.49200221924

table1 = [["example1",ent1],["example2",ent2],["example3",ent3], ["example4",ent4]]
print (tabulate(table1))
#--------  -------
#example1  3.56109
#example2  3.55137
#example3  8.9045
#example4  8.492
#--------  -------
#We can conclude that the greater the standard deviation, the greater the entropy.
#Because STD is big, the range of assumption becomes greater and thus entropy rises.
#Example 3 and 4 are both higher than example 1 and 2 because their standard deviations are greater.
#It seems example 3 has greater entropy because example 4 has expected mean of 10 and 
#because the upper boundary is limited to 20, the standard deviation of example 4 is limited upwards.
 

