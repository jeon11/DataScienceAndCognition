# Analysis: Calculate marginal, conditional, and joint probabilities

# Suppose there are two 6-sided dices that were tossed simultaneously for 20 times 
# The data below record which side showed up for each toss, for each dice
x = [4,2,5,5,6,2,4,3,2,1,5,1,3,2,6,1,2,6,1,4]; # dice 1
y = [6,1,5,5,3,2,4,3,1,1,1,2,6,1,1,1,1,3,1,1]; # dice 2

# Task 1: Compute marginal probabilities p(X=1), p(X=2), ..., p(X=6); ditto for p(Y) 
x.sort()
print (x)
y.sort()
print (y)


# Task 2: Construct and report a 6-by-6 contingency table C where C[i,j] records #instances that X=i and Y=j over the 20 tosses 
# such that i and j each can take one of 6 possible values {1,2,3,4,5,6} [1pt]


# Task 3: Based on 2, compute and report the following conditional and joint probabilites
# a) p(X=1|Y=2) [.5pt]
# b) p(X=5,Y=5) [.5pt]


# Task 4: Compute the expected value for dice 1 [.5pt]


# Task 5: Compute the variance for dice 1 [.5pt]


# Task 6: Compute a hypothetical contingency table assuming X and Y were independent - explain how you did it [1pt]

