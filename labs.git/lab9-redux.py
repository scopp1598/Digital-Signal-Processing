# Sean Copp
# Digitial Signal Processing
# lab 9
# A DFT of My Very Own

# TODO:
# 1.	for a summation just do a for loop that keeps a running total of 
# 	of the loop you are going through
# 2.	Make nested for loop: one for each output value and one for each 
# 	input value
# 		I dont entirely know what this means
# 3.	Make sure to use complex numbers by using 1j

import numpy as np 
import matplotlib.pyplot as plt 
import time
from scipy.io import wavfile

# Performs a slow fourier transform.
# u: This argument is the input array
def myOwnDFT(u):
	Un = np.array([])
	# The outer loop takes the answer from the inner and adds it to a
	# list of results
	for N in np.arange(0, len(u)):
		# Inner loop finds the particular value of the equation
		# It does the summation as defined by THE PROF for the given
		# value of n
		sum = 0
		for k in np.arange(0, len(u)):
			sum += u[k]*np.exp(1j*(-2)*np.pi*k*N/len(u))

		# HERE IS THE ACTUAL CODE FOR THE OUTER LOOP
		# Tacks the value from the summation in the inner loop to the 
		# end of the output array
		Un = np.append(Un, sum)
	# This returns Un. This is the Fourier Transform Output
	return np.abs(Un)


# t = np.arange(0, 200, 1)
t = np.linspace(0, 1, 200)
wave10 = np.sin(2*np.pi*10*t)
wave20 = np.sin(2*np.pi*20*t)
wave30 = np.sin(2*np.pi*30*t)

# 1337 programmers use dark background
plt.style.use('dark_background')
# Make a new figure
# plt.figure(1)
# plt.subplot(511)
# plt.plot(t, wave10)
# plt.title("Sine Wave 10Hz")

# plt.subplot(513)
# plt.plot(t, wave20)
# plt.title("Sine Wave 20Hz")

# plt.subplot(515)
# plt.plot(t, wave30)
# plt.title("Sine Wave 30Hz")

# plt.figure(2)
# plt.subplot(511)
# start = time.time()
# plt.plot(t, myOwnDFT(wave10))
# end = time.time()
# elapsed_time = end-start
# plt.title("DFT of 10Hz Sine, elapsed time = %s"%elapsed_time)

# plt.subplot(513)
# start = time.time()
# plt.plot(t, myOwnDFT(wave20))
# end = time.time()
# elapsed_time = end-start
# plt.title("DFT of 20Hz Sine, elapsed time = %s"%elapsed_time)

# plt.subplot(515)
# start = time.time()
# plt.plot(t, myOwnDFT(wave30))
# end = time.time()
# elapsed_time = end-start
# plt.title("DFT of 30Hz Sine, elapsed time = %s"%elapsed_time)

# sizes = [200,	400,	600,	800,	1000, 	2000]
# times = [0, 	0, 		0, 		0, 		0, 		0	]
# start = time.time()
# myOwnDFT(np.sin(np.arange(0, sizes[0], 1)))
# end = time.time()
# times[0] = end-start

# start = time.time()
# myOwnDFT(np.sin(np.arange(0, sizes[1], 1)))
# end = time.time()
# times[1] = end-start

# start = time.time()
# myOwnDFT(np.sin(np.arange(0, sizes[2], 1)))
# end = time.time()
# times[2] = end-start

# start = time.time()
# myOwnDFT(np.sin(np.arange(0, sizes[3], 1)))
# end = time.time()
# times[3] = end-start

# start = time.time()
# myOwnDFT(np.sin(np.arange(0, sizes[4], 1)))
# end = time.time()
# times[4] = end-start

# start = time.time()
# myOwnDFT(np.sin(np.arange(0, sizes[5], 1)))
# end = time.time()
# times[5] = end-start

# plt.figure(3)
# plt.stem(sizes, times)
# plt.title("myOwnDFT Performance")


# frequency sample, data of .wav file
fs, data = wavfile.read("./kpt1note2k.wav")
song_time = len(data)/fs
# print(song_time)
song_length = len(data)
# print(song_length)
# print("If something of length 600 takes about 1.5 seconds and something of length 1000 takes about 4.5 seconds I'd guess that something of length 2000 will take 12 seconds")
start = time.time()
plt.figure(4)
plt.plot(np.linspace(0, 1, fs), myOwnDFT(data))
end = time.time()
elapsed_time = end-start
print("It actually took %s"%elapsed_time) # about 30 seconds



plt.show()