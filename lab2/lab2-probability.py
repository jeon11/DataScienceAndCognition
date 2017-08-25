# Analysis: Calculate marginal, conditional, and joint probabilities

# Suppose there are two 6-sided dices that were tossed simultaneously for 20 times 
# The data below record which side showed up for each toss, for each dice
x = [4,2,5,5,6,2,4,3,2,1,5,1,3,2,6,1,2,6,1,4]; # dice 1
y = [6,1,5,5,3,2,4,3,1,1,1,2,6,1,1,1,1,3,1,1]; # dice 2

# Task 1: Compute marginal probabilities p(X=1), p(X=2), ..., p(X=6); ditto for p(Y) 
# x.sort()
# print (x) # [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
# y.sort()
# print (y) # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6]
def marginal_probability(x, n): #computes marginal probability of n in list x
	k, total = 0, 0
	while k < len(x):
		if n == x[k]: 
			k += 1
			total += 1
		else: 
			k += 1
	return total/len(x)

print (marginal_probability(x, 1))# p(X=1)=4/20=0.20
print (marginal_probability(x, 2))# p(X=2)=5/20=0.25
print (marginal_probability(x, 3))# p(X=3)=2/20=0.10
print (marginal_probability(x, 4))# p(X=4)=3/20=0.15
print (marginal_probability(x, 5))# p(X=5)=3/20=0.15
print (marginal_probability(x, 6))# p(X=6)=3/20=0.15

print (marginal_probability(y, 1))# p(Y=1)=10/20=0.50
print (marginal_probability(y, 2))# p(Y=2)=2/20=0.10
print (marginal_probability(y, 3))# p(Y=3)=3/20=0.15
print (marginal_probability(y, 4))# p(Y=4)=1/20=0.05
print (marginal_probability(y, 5))# p(Y=5)=1/20=0.05
print (marginal_probability(y, 6))# p(Y=6)=2/20=0.10

# Task 2: Construct and report a 6-by-6 contingency table C where C[i,j] records #instances that X=i and Y=j over the 20 tosses 
# such that i and j each can take one of 6 possible values {1,2,3,4,5,6} [1pt]

import pandas as pd
x_1 = [3, 1, 0, 0, 0, 0, 4]
x_2 = [4, 1, 0, 0, 0, 0, 5]
x_3 = [0, 0, 1, 0, 0, 1, 2]
x_4 = [1, 0, 0, 1, 0, 1, 3]
x_5 = [1, 0, 0, 0, 2, 0, 3]
x_6 = [1, 0, 2, 0, 0, 0, 3]
total = [10, 2, 3, 1, 2, 2, 20]

cont_table = pd.DataFrame({'1': x_1, '2': x_2, '3': x_3, '4': x_4, '5':x_5, '6':x_6, 'total':total}, index = ['1', '2', '3', '4', '5', '6', 'total'])
print (cont_table)
#       1  2  3  4  5  6  total
#1      3  4  0  1  1  1     10
#2      1  1  0  0  0  0      2
#3      0  0  1  0  0  2      3
#4      0  0  0  1  0  0      1
#5      0  0  0  0  2  0      2
#6      0  0  1  1  0  0      2
#total  4  5  2  3  3  3     20

def c(i, j, x, y): #returns total number of pairs that corresponds to C(i,j)
	k, total = 0, 0
	while k < len(x):
		if i == x[k]:
			if j == y[k]:
				total += 1
			k += 1
		else:
			k += 1
	return total
c(1, 3, x, y) #0
c(1, 2, x, y) #1
c(5, 5, x, y) #2

# Task 3: Based on 2, compute and report the following conditional and joint probabilites
# a) p(X=1|Y=2) [.5pt]
# 1/2 = 0.5
# b) p(X=5,Y=5) [.5pt]
# p(x=5)p(y=5|x=5) = 3/20 * 2/3 = 0.1


# Task 4: Compute the expected value for dice 1 [.5pt]
ev = 0.2*4+0.25*5+0.1*2+0.15*3+0.15*3+0.15*3
print (ev) #3.6

# # Task 5: Compute the variance for dice 1 [.5pt]
# all_mean_std = []
def variance(x):
	sum, var = 0, 0
	for j in range(len(x)):
		sum += x[j]
	mean = sum/(float(len(x)))
	print(mean)
	for i in range(len(x)):
		var += (x[i] - mean)**2
	return var
print (variance(x)) #61.75

# Task 6: Compute a hypothetical contingency table assuming X and Y were independent - explain how you did it [1pt]
# If X and Y were independent, P(x,y)=P(x)P(y).
# By product rule, P(x,y)=P(x)P(y|x)=P(y)P(x|y).
# Now we can infer that P(x)=P(x|y) and P(y)=P(y|x). 
# For the hypothetical table created below, P(x,y)=P(x)P(y) is satisfied.  
hx_1 = [1, 1, 1, 1, 1, 1, 6]
hx_2 = [1, 1, 1, 1, 1, 1, 6]
hx_3 = [1, 1, 1, 1, 1, 1, 6]
hx_4 = [1, 1, 1, 1, 1, 1, 6]
hx_5 = [1, 1, 1, 1, 1, 1, 6]
hx_6 = [1, 1, 1, 1, 1, 1, 6]
total = [6, 6, 6, 6, 6, 6, 36]

hypo_table = pd.DataFrame({'1': hx_1, '2': hx_2, '3': hx_3, '4': hx_4, '5':hx_5, '6':hx_6, 'total':total}, index = ['1', '2', '3', '4', '5', '6', 'total'])
print (hypo_table)
#       1  2  3  4  5  6  total
#1      1  1  1  1  1  1      6
#2      1  1  1  1  1  1      6
#3      1  1  1  1  1  1      6
#4      1  1  1  1  1  1      6
#5      1  1  1  1  1  1      6
#6      1  1  1  1  1  1      6
#total  6  6  6  6  6  6     36

