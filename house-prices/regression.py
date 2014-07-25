#!/user/bin/env python3

import numpy as np

# Don't print small floating point values using scientific notation
np.set_printoptions(suppress=True)

prices = np.loadtxt('prices', delimiter=','))

# prices[:, 0] = first column
# prices[0] = first row
# len(prices) = num data rows
# len(prices[0]) = num features + 1 (= y)

x = prices[:,0:-1]
y = prices[:,-1]
m = len(x)
n = len(x[0])
