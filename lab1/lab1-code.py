# Analysis of regression towards the mean using box plots and permutation test
# Data from Schall and Smith (2000)

# Email your solution in a single PDF to the instructor within 1 week (before the next upcoming session)

import numpy as np
import matplotlib.pyplot as plt

# Data
d1998=[363,354,339,337,336,331,328,328,327,327]; # batting average of top 10 playes in 1998
d1999=[379,298,342,281,249,298,297,303,257,332]; # batting average of top 10 playes in 1999

# Boxplot difference in batting average between the two years (include axes-labeled figure in report) [1pt]
d1998.sort()
d1999.sort()
diff = [d1998[i] - d1999[i] for i in range(min(len(d1998), len(d1999)))]
print("sorted batting average difference:", diff)
diff.sort()
median_diff = (diff[4] + diff[5]) // 2
print ("median for batting average difference:", median_diff) #33
lower_diff = diff[2]
upper_diff = diff[7]
print ("Q1:", lower_diff) #12
print ("Q3:", upper_diff) #47

plt.boxplot(diff)
plt.xticks([1], ['1998 - 1999'])
plt.title('Batting Average Difference Between 1998 and 1999')
plt.ylabel('# of Batting Average')
plt.xlabel('Year Difference')
plt.show()

# Boxplot batting averages for each year (include axes-labeled figure in report) [1pt]
years = [d1998, d1999]
plt.boxplot(years)
plt.xticks([1, 2], ['1998', '1999'])
plt.title('Batting Averages for Each Year')
plt.ylabel('# of Batting Average')
plt.xlabel('Year')
plt.show()

# Compute and report inter-quartile (75% - 25%) range and median in batting averages for each year [1pt]

# Finding Median for each year
median_1998 = (d1998[4] + d1998[5]) // 2
median_1999 = (d1999[4] + d1999[5]) // 2
print("median for 1998:", median_1998) #333
print("median for 1998:", median_1999) #298

# Finding interquartile range for each year
lower_1998 = d1998[2]
upper_1998 = d1998[7]
lower_1999 = d1999[2]
upper_1999 = d1999[7]
iqr_1998 = upper_1998 - lower_1998
iqr_1999 = upper_1999 - lower_1999
print("IQR for 1998:", iqr_1998) #11
print("IQR for 1999:", iqr_1999) #51

# Permutation test

# Implement a function that performs permutation test for group difference (group B, 1999, mean - group A, 1998, mean)
# datGrpA is data (e.g. an array) from group A
# datGrpB is data (e.g. an array) from group B
# nperm is number of permutations 
# pvalue is the empirical p-value computed from data
# permdiff is the vector of differences between permuted group means
# d is the actual difference between group means

# Include your Python implementation for this function in the report (appendix) [1pt]
datGrpA = np.array([363,354,339,337,336,331,328,328,327,327])
datGrpB = np.array([379,298,342,281,249,298,297,303,257,332]) 

def permtest(datGrpA, datGrpB, nperm):
	d = np.abs(np.mean(datGrpA) - np.mean(datGrpB))
	i = 0
	n = len(datGrpA)
	sets = np.concatenate([datGrpA, datGrpB])
	lst_permdiff = []
	for k in range(nperm):
		np.random.shuffle(sets)
		permdiff = np.abs(np.mean(sets[:n]) - np.mean(sets[n:]))
		i += d < permdiff
		lst_permdiff.append(permdiff)
	pvalue = i / nperm
	#Histogram from the collected 10000 # of nperm for permdiff
	plt.hist(lst_permdiff, bins = 20, normed=True)
	plt.title('Permuted Differences in Data')
	plt.xlabel('Permuted Difference')
	plt.ylabel('counts')
	plt.show()
	return pvalue, permdiff, d

permtest(datGrpA, datGrpB, 10000)
# pvalue < 0.05
# d = 33.40

# Construct a histogram based on permuted differences "permdiff" [1pt]
# Show where "d" is with respect to the permuted difference (e.g. by drawing a vertical line)
# Include this figure in the report

#See above for histogram code 
#See pdf 

# Report p-value from the permutation test and state your conclusion in 1 sentence [1pt]

# pvalue is approximately 0.01 which is significantly less than 0.05. 
# Because pvalue is small, we can reject the null hypothesis that states the batting 
# averages of the two years are not significantly different. We can assume that 
# there is statistical difference in batting averages of two years. 
# 

