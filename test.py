import median_filter
import numpy as np
import scipy.signal
from time import time

a = np.random.rand(1000000)

numpy_start = time()
b = scipy.signal.medfilt2d( a.reshape(1, -1), [1, 13] )
numpy_end = time()

swig_start = time()
c = np.array(a)
median_filter.filter( c, 13 )
swig_end = time()

print "Scipy took ", (numpy_end-numpy_start)
print "median_filter took ", (swig_end-swig_start)
