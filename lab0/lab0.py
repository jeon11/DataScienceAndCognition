# Cog Sci 190 lab0
# Jin-Young Jeon
# Yannie Yip

import csv
import numpy as np

csv_data = np.genfromtxt('lab0-data.csv', dtype=int, delimiter=',', names=True)
print(csv_data)
print(len(csv_data))
all_mean_std = []
for i in range(0, 15):
	sum = 0
	for j in range(len(csv_data)):
		sum += csv_data[j][i]
	mean = sum/(float(len(csv_data)))

	std = []
	for k in range(len(csv_data)):
		std.append((csv_data[k][i] - mean)**2)

	sum_of_std = 0
	for num in range(len(std)):
		sum_of_std += std[num]
	mean_std = float(sum_of_std/len(std))

	all_mean_std.append(mean_std)

actual_target_numbers = [3, 8, 40, 2, 5, 30, 7, 35, 6, 15, 10, 20, 9, 25, 4]

sort_indices = np.argsort(actual_target_numbers)
# [3  0 14  4  8  6  1 12 10  9 11 13  5  7  2]

sorted_target_numbers = np.array(actual_target_numbers)[sort_indices]
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40]
# used for graphing x-axis

sorted_result = np.array(all_mean_std)[sort_indices]
# [0.0302734375, 0.0, 0.0625, 0.1474609375, 0.1474609375, 2.3349609375, 0.5693359375, 3.6943359375, 5.1630859375, 7.8740234375, 24.046875, 32.375, 48.3115234375, 36.921875, 56.6474609375]
# used for graphing y-axis

