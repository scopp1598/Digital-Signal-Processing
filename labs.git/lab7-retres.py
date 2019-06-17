import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# I kept using just pi because matlab
pi = np.pi

# Approximated sawtooth
def approx_saw(t, n, r):
	return r+(-2/pi*(np.cos(n*pi)*np.sin(n*t)))

def prob_2(x, n, r):
	return r+(4/pi*1/n*np.sin(n*pi*x/L))

def prob_3(y, n, r):
	return r+(8/pi**2*(-1**((n-1)/2))*np.sin(n*pi*y/l))

plt.style.use('dark_background')

# Problem 1
T = np.linspace(-pi, pi, 0.01)
T = np.arange(-pi, pi, 0.01)
for t in T:
	# r = 0
	for n in list(range(1, 11, 1)):
		saw = np.array([-2/pi*(np.cos(n*pi)*np.sin(n*t))])
		
	dtf = sig.dlti(saw, [1, t/pi])
	x,y = sig.dstep((dtf), n=1000)
	# plt.plot(x, y[:][0])
	plt.plot(sig.sawtooth(t))
	plt.show()
	# 	plt.plot(t, approx_saw(t, n, r))
	# 	r = approx_saw(t, n, r)
	# 	plt.title("Approximated sawtooth    n=%s"%n)
	# 	plt.savefig("./p1_redux/saw_n%s"%n)
	# 	plt.show()


# # Problem 2
# x = np.arange(-pi, pi, 0.01)
# L = 5
# r = 0
# for n in list(range(1, 21, 2)):
# 	plt.plot(x, prob_2(x, n, r))
# 	r = prob_2(x, n, r)
# 	plt.title("Problem 2    n=%s"%n)
# 	plt.savefig("./p2_redux/p2_n%s"%n)
# 	plt.show()

# # Problem 3
# y = np.arange(-pi, pi, 0.01)
# l = 5
# r = 0
# for n in list(range(1, 21, 2)):
# 	plt.plot(y, prob_3(y, n, r))
# 	r = prob_3(y, n, r)
# 	plt.title("Problem 3    n=%s"%n)
# 	plt.savefig("./p3_redux/p3_n%s"%n)
# 	plt.show()
