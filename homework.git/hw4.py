import numpy as np 
import matplotlib.pyplot as plt 

def f1(w):
	return np.abs(2/(w**3)*(20*w*np.cos(5*w)+1j*(25*(w**2)-2*np.sin(5*w))))

def f2(a, w):
	return np.abs(np.sin(4*np.pi*(a-w))/(a-w)+np.sin(4*np.pi*(a+w))/(a+w))

# Problem 1
plt.figure(1)
w1 = np.arange(-5, 5, 0.01)
fr1 = np.linspace(-10, 0.01, 10)
plt.plot(w1, f1(w1))

# Problem 2
plt.figure(2)
w2 = np.arange(-4*np.pi, 4*np.pi, 0.01)
fr2 = np.linspace(-10, 0.01, 10)
a2 = 2
plt.plot(w2, f2(a2, w2))

# Problem 3 varying a
plt.figure(3)
w3 = np.arange(-4*np.pi, 4*np.pi, 0.01)
fr3 = np.linspace(-10, 0.01, 10)
a3 = 2
plt.plot(w3, f2(a3, w3))

a4 = 1
plt.plot(w3, f2(a4, w3))

a5 = 4
plt.plot(w3, f2(a5, w3))

# Problem 3 varying window size
plt.figure(4)
w4 = np.arange(-4*np.pi, 4*np.pi, 0.01)
fr4 = np.linspace(-10, 0.01, 10)
a6 = 2
plt.plot(w4, f2(a6, w4))

w5 = np.arange(-4, 4, 0.01)
plt.plot(w5, f2(a6, w5))

w6 = np.arange(-10, 10, 0.01)
plt.plot(w6, f2(a6, w6))

# Problem 3 varying pi coef
plt.figure(5)
w7 = np.arange(-4*np.pi, 4*np.pi, 0.01)
fr5 = np.linspace(-10, 0.01, 10)
a7 = 2
plt.plot(w7, f2(a7, w7))

w8 = np.arange(-1*np.pi, 1*np.pi, 0.01)
plt.plot(w8, f2(a7, w8))

w9 = np.arange(-6*np.pi, 6*np.pi, 0.01)
plt.plot(w9, f2(a7, w9))

plt.show()
