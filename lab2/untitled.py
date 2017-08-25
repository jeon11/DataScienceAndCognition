import numpy as np
import matplotlib.pyplot as plt

mu1, sigma1 = 0, 1
mu2, sigma2 = 10, 1
mu3, sigma3 = 0, 10
mu4, sigma4 = 10, 10

s1 = np.random.normal(mu1, sigma1, 100000)
abs(mu1 - np.mean(s1)) < 0.01
# True
abs(sigma1 - np.std(s1, ddof=1)) < 0.01
# True

# hist1 = np.histogram(s1, bins=10, range=-20,20)
# count, bins, ignored = plt.hist(s1, 100, normed=True)
count, bins = plt.hist(s1, 100)
plt.plot(bins, 1/(sigma1 * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mu1)**2 / (2 * sigma1**2) ),
          linewidth=2, color='r')
plt.show()