#CogSci 190 
#Jin Young Jeon (23051612)
#Lab 4
import csv
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import metrics
import math
from tabulate import tabulate

#1. 
print ("data points")
data = np.genfromtxt('position-data.csv', dtype=int, delimiter=',', names=True)
print (data.tolist())
print ("\n")
print ("stimuli")
stimuli = np.genfromtxt('position-stimuli.csv', dtype=int, delimiter=',', names=True)
print (stimuli.tolist())
# 
def errors(data, stimuli, condition): 
	correct, incorrect = 0, 0 
	i = 0
	while i in range(0, len(stimuli)):
		if stimuli[i][0] == condition:
			for j in range(0, len(data)):
				if stimuli[i][1] == data[j][i]:
					correct += 1
					i += 1
					print ("correct", + correct, incorrect, i)
				else: 
					incorrect += 1
					i += 1
					print ("incorrect", + correct, incorrect, i)
		else: 
			i += 1
	return correct, incorrect
# 
def error_prob(data, stimuli, condition, trial):
#computes error probability for specific trial that satisfy condition
	correct, incorrect = 0, 0
	if stimuli[trial][0] == condition: 
		for j in range(0, len(data)):
			if stimuli[trial][1] == data[j][trial]:
				correct += 1
			else: 
				incorrect += 1
	else: 
		return "not conditionally met"
	return incorrect/(correct+incorrect) 

cond1_mean = (error_prob(data, stimuli, 1, 0)+error_prob(data, stimuli, 1, 1)+error_prob(data, stimuli, 1, 2)+error_prob(data, stimuli, 1, 3)+error_prob(data, stimuli, 1, 4)+error_prob(data, stimuli, 1, 5)+error_prob(data, stimuli, 1, 6)+error_prob(data, stimuli, 1, 7)+error_prob(data, stimuli, 1, 8)+error_prob(data, stimuli, 1, 9)+error_prob(data, stimuli, 1, 10))/11
#0.0855614973262032
cond2_mean = (error_prob(data,stimuli,2,11)+error_prob(data,stimuli,2,12)+error_prob(data,stimuli,2,13)+error_prob(data,stimuli,2,14)+error_prob(data,stimuli,2,15)+error_prob(data,stimuli,2,16))/6
#0.0196078431372549
cond3_mean = (error_prob(data,stimuli,3,17)+error_prob(data,stimuli,3,18)+error_prob(data,stimuli,3,19)+error_prob(data,stimuli,3,20)+error_prob(data,stimuli,3,21)+error_prob(data,stimuli,3,22)+error_prob(data,stimuli,3,23)+error_prob(data,stimuli,3,24)+error_prob(data,stimuli,3,25)+error_prob(data,stimuli,3,26)+error_prob(data,stimuli,3,27)+error_prob(data,stimuli,3,28)+error_prob(data,stimuli,3,29)+error_prob(data,stimuli,3,30)+error_prob(data,stimuli,3,31)+error_prob(data,stimuli,3,32)+error_prob(data,stimuli,3,33)+error_prob(data,stimuli,3,34)+error_prob(data,stimuli,3,35)+error_prob(data,stimuli,3,36)+error_prob(data,stimuli,3,37))/21
#0.1876750700280112

cond1_std = math.sqrt(((error_prob(data, stimuli, 1, 0)-cond1_mean)**2+(error_prob(data, stimuli, 1, 1)-cond1_mean)**2+(error_prob(data, stimuli, 1, 2)-cond1_mean)**2+(error_prob(data, stimuli, 1, 3)-cond1_mean)**2+(error_prob(data, stimuli, 1, 4)-cond1_mean)**2+(error_prob(data, stimuli, 1, 5)-cond1_mean)**2+(error_prob(data, stimuli, 1, 6)-cond1_mean)**2+(error_prob(data, stimuli, 1, 7)-cond1_mean)**2+(error_prob(data, stimuli, 1, 8)-cond1_mean)**2+(error_prob(data, stimuli, 1, 9)-cond1_mean)**2+(error_prob(data, stimuli, 1, 10)-cond1_mean)**2)/11)
#0.1131872218637258
cond2_std = math.sqrt(((error_prob(data,stimuli,2,11)-cond2_mean)**2+(error_prob(data,stimuli,2,12)-cond2_mean)**2+(error_prob(data,stimuli,2,13)-cond2_mean)**2+(error_prob(data,stimuli,2,14)-cond2_mean)**2+(error_prob(data,stimuli,2,15)-cond2_mean)**2+(error_prob(data,stimuli,2,16)-cond2_mean)**2)/6)
#0.0277296776935901
cond3_std = math.sqrt(((error_prob(data,stimuli,3,17)-cond3_mean)**2+(error_prob(data,stimuli,3,18)-cond3_mean)**2+(error_prob(data,stimuli,3,19)-cond3_mean)**2+(error_prob(data,stimuli,3,20)-cond3_mean)**2+(error_prob(data,stimuli,3,21)-cond3_mean)**2+(error_prob(data,stimuli,3,22)-cond3_mean)**2+(error_prob(data,stimuli,3,23)-cond3_mean)**2+(error_prob(data,stimuli,3,24)-cond3_mean)**2+(error_prob(data,stimuli,3,25)-cond3_mean)**2+(error_prob(data,stimuli,3,26)-cond3_mean)**2+(error_prob(data,stimuli,3,27)-cond3_mean)**2+(error_prob(data,stimuli,3,28)-cond3_mean)**2+(error_prob(data,stimuli,3,29)-cond3_mean)**2+(error_prob(data,stimuli,3,30)-cond3_mean)**2+(error_prob(data,stimuli,3,31)-cond3_mean)**2+(error_prob(data,stimuli,3,32)-cond3_mean)**2+(error_prob(data,stimuli,3,33)-cond3_mean)**2+(error_prob(data,stimuli,3,34)-cond3_mean)**2+(error_prob(data,stimuli,3,35)-cond3_mean)**2+(error_prob(data,stimuli,3,36)-cond3_mean)**2+(error_prob(data,stimuli,3,37)-cond3_mean)**2)/21)
#0.14133866455510213

# # error bar 
cond1 = error_prob(data, stimuli, 1, 0), error_prob(data, stimuli, 1, 1), error_prob(data, stimuli, 1, 2), error_prob(data, stimuli, 1, 3), error_prob(data, stimuli, 1, 4), error_prob(data, stimuli, 1, 5), error_prob(data, stimuli, 1, 6), error_prob(data, stimuli, 1, 7), error_prob(data, stimuli, 1, 8), error_prob(data, stimuli, 1, 9), error_prob(data, stimuli, 1, 10)
cond2 = error_prob(data,stimuli,2,11), error_prob(data,stimuli,2,12), error_prob(data,stimuli,2,13), error_prob(data,stimuli,2,14), error_prob(data,stimuli,2,15), error_prob(data,stimuli,2,16)
cond3 = error_prob(data,stimuli,3,17), error_prob(data,stimuli,3,18), error_prob(data,stimuli,3,19), error_prob(data,stimuli,3,20), error_prob(data,stimuli,3,21), error_prob(data,stimuli,3,22), error_prob(data,stimuli,3,23), error_prob(data,stimuli,3,24), error_prob(data,stimuli,3,25), error_prob(data,stimuli,3,26), error_prob(data,stimuli,3,27), error_prob(data,stimuli,3,28), error_prob(data,stimuli,3,29), error_prob(data,stimuli,3,30), error_prob(data,stimuli,3,31), error_prob(data,stimuli,3,32), error_prob(data,stimuli,3,33), error_prob(data,stimuli,3,34), error_prob(data,stimuli,3,35), error_prob(data,stimuli,3,36), error_prob(data,stimuli,3,37)

sorted_cond1 = (0, 0.29411764705882354, 0.29411764705882354, 0.17647058823529413, 0, 0, 0, 0.11764705882352941, 0.058823529411764705, 0, 0)
sorted_cond2 = (0, 0, 0, 0.058823529411764705, 0, 0.058823529411764705)
sorted_cond3 = (0, 0, 0.23529411764705882, 0.29411764705882354, 0.17647058823529413, 0.29411764705882354, 0.23529411764705882, 0.23529411764705882, 0.11764705882352941, 0.11764705882352941, 0, 0.058823529411764705, 0.23529411764705882, 0.47058823529411764, 0.23529411764705882, 0.5294117647058824, 0.29411764705882354, 0.17647058823529413, 0.11764705882352941, 0.11764705882352941, 0)

x1 = (100, 10, 70, 30, 20, 40, 90, 80, 50, 60, 0)
x2 = (0, 100, 60, 20, 80, 40)
x3 = (35, 40, 80, 65, 85, 55, 5, 45, 75, 100, 95, 10, 30, 90, 15, 0, 60, 50, 20, 70, 25)

sorted_x1 = sorted(x1)
sorted_x2 = sorted(x2)
sorted_x3 = sorted(x3)

plt.figure()
plt.errorbar(sorted_x1, sorted_cond1, xerr = None, yerr = 0.1131, marker = 'o')
plt.errorbar(sorted_x2, sorted_cond2, xerr = None, yerr = 0.0277, marker = 'o')
plt.errorbar(sorted_x3, sorted_cond3, xerr = None, yerr = 0.1413, marker = 'o') 
plt.title("Error Probability for Each Condition")
plt.xlabel("Number Presented")
plt.ylabel("P(Incorrect)")
plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
plt.show()

#2. Mutual Info
#MI of each individual condition from error probability 
MI1 = sklearn.metrics.mutual_info_score(sorted_cond1, sorted_cond1)
print(MI1)
# 1.29454516584
MI2 = sklearn.metrics.mutual_info_score(sorted_cond2, sorted_cond2)
print(MI2)
# 0.636514168295
MI3 = sklearn.metrics.mutual_info_score(sorted_cond3, sorted_cond3)
print(MI3)
# 1.91025216733

x = ("Cond2", "Cond1", "Cond3")
y = (MI2, MI1, MI3)
plt.plot(y)
plt.plot([0.5, 1, 1.5, 2.0], [0.5, 1, 1.5, 2.0])
plt.title("Mutual Info for Each Condition")
plt.xlabel("data/condition")
plt.ylabel("MI, recorded responses")
plt.show()

#3. 
#For some reason, my MI line crosses y=x. While the three MI points are supposed to take 
#the curve form of log, my MIs appear almost linear. 
#The more amount of data is shared, the more mutual information there is.
#Also, the more choices you have, ie. increments of 5 has more choices than increments of 20,
#the more randomness you have (the entropy increases). 

