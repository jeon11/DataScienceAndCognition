import numpy as np
import matplotlib.pyplot as plt

# Analysis: Simulate librarian-farmer example via Bayes rule (with fixed likelihood ratio)

# Consider T&K 1979 example on Farmer vs Librarian where choices are made on which occupation fits the description or the vignette better.

# Suppose that the likelihood for librarian p(description|librarian) is twice as much as that for farmer p(description|farmer)
# e.g. p(description|librarian) = .8 and p(description|farmer) = .4

# Allow prior p(librarian) to vary from 0.01 to 100 with an incremental step size of 1, i.e. prior_libr = np.linspace(0.01,1,100) 

# Task 1: Simulate and plot the posterior probability that one would choose librarian, p(librarian|description), via the Bayes rule, for the specified range of prior values. [1.5pt]
# NOTE: Your plot should have the x-axis showing *prior ratio* "p(farmer) / p(librarian)", such that p(farmer)+p(librarian)=1, and y-axis showing the posterior p(librarian|description).

des1lib = 0.8
des1farm = 0.4
prior_lib = np.linspace(0.01,1,100) #prior_lib = p(lib) and p(farm) = 1 - p(lib)
prior_ratio = (1-prior_lib)/(prior_lib)
#given Bayes Theorem: 
posterior_prob = ((des1lib)*(prior_lib))/((des1lib)*(prior_lib)+(des1farm)*(1-prior_lib))
plt.plot(prior_ratio, posterior_prob, 'o')
plt.show()

# Task 2: Indicate and explain where on this plot would be considered "rational" if one chooses librarian over farmer. [.5pt]
# Initially, neglecting the base rate, people confirm the person is more likely to be a librarian. 
# However, the posterior probability, the belief that the person is a librarian given the description, decreases the more data there is.
# It would only seem rational to choose librarian over farmer around approximately where x < 5, in which posterior probability is above 0.5.


