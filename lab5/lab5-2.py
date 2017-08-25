#lab 5.2 
#JinYoungJeon (SID: 23051612)
#CogSci190
import pickle 
from tabulate import tabulate
with open('prototype_data.pickle', 'rb') as f: 
	birdnames, F, goodness = pickle.load(f)

#2================================
def average_of_all(F): #finding averages of all data/features
	# sum = 0
	lst = []
	i = 0 
	while i in range(0, len(F[0])):
		a = sum(list(zip(*F))[i])
		# print(a)
		i += 1
		lst.append(a)

	averages = []
	for i in range(0, len(lst)):
		averages.append(lst[i]/17)
	return averages

averaged = average_of_all(F)
# print(averaged)
#averaged is the average of all data features

def euclidean_distance(F, n): #average distance for nth animal
	lst = []
	for i in range(0, len(F[0])):
		a = (F[n][i] - averaged[i])**2
		lst.append(a)
	distance = (sum(lst))**0.5
	return distance 

def find_prototype():
	minimum = []
	for i in range(0, 17):
		a = euclidean_distance(F, i)
		minimum.append(a)
	print(minimum)
	return min(minimum)
print("prototypical bird is Falcon with distance: ", + find_prototype()) #returns 20.71 which is equivalent to distance of Falcon

print(F[5][0:10]) #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#3================================
falcon = F[5]

# print(euclidean_distance(F, 0))
def prototype_distance(F, n): #average distance for nth animal
	lst1 = []
	for i in range(0, len(F[0])):
		a = (F[n][i] - falcon[i])**2
		lst1.append(a)
	distance = sum(lst1)**0.5
	return distance 

lst2 = []
for i in range(0, 17):
	lst2.append(prototype_distance(F, i))
print(sorted(lst2))

table1 = [["1.eagle",1526.40],["2.blackbird",1538.85],["3.crow",1540.17],["4.sparrow",1561.46],["5.sparrow",1561.46],["6.peacock",1620.38],["7.robin",1622.45],["8.woodpecker",1660.90],["9.owl",1662.11],["10.seagull",1681.89],["11.bat",1715.12],["12.penguin",1716.11],["13.canary",1717.90],["14.ostrich",1718.62],["15.parrot",1738.50],["16.chicken",1772.60],["17.swan",1788.98]]
print(tabulate(table1))

#------------  -------
#1.eagle       1526.4
#2.blackbird   1538.85
#3.crow        1540.17
#4.sparrow     1561.46
#5.sparrow     1561.46
#6.peacock     1620.38
#7.robin       1622.45
#8.woodpecker  1660.9
#9.owl         1662.11
#10.seagull    1681.89
#11.bat        1715.12
#12.penguin    1716.11
#13.canary     1717.9
#14.ostrich    1718.62
#15.parrot     1738.5
#16.chicken    1772.6
#17.swan       1788.98
#------------  -------

