import matplotlib.pyplot as plt 
import numpy as np 
import random
from scipy.fftpack import fft 
from scipy.io import wavfile


# Problem 1
t = np.arange(-1, 1, 0.001)

s = -t

plt.plot(s, t)
plt.show()

# Problem 2
k = random.randint(0, 5)
c_high = random.randint(1, 5)
c_low = -c_high
t2 = np.arange(c_low, c_high, 0.01)
s2 = np.ones(len(t2))*random.randint(1, 5)

plt.plot(t2, s2)
plt.show()

# Problem 3
t3 = np.arange(-np.pi, np.pi, 0.01)
s3 = t3-t3**2

plt.plot(s3, t3)
plt.show()