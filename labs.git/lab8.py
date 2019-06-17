import matplotlib.pyplot as plt 
import numpy as np 
from scipy.fftpack import fft 
from scipy.io import wavfile

def fun(wav):
	# Code goes here
	# frequency sample, data of .wav file
	fs, data = wavfile.read(wav)
	# fast fourier transform of the wav file
	fftOut = fft(data)
	# length of the recording
	time = len(data)/fs
	# get a list of sample indices
	n = np.arange(len(data))
	# a list of frequencies contained in the recording
	freqLabel = n*(1/time)
	# plot stuff
	plt.plot(freqLabel, np.abs(fftOut))
	plt.title("Piano Note Analysis %s"%wav)
	plt.xlabel("Frequency (Hz)")
	plt.ylabel("Amplitude")
	plt.xlim(200, 1000)
	plt.show()


if __name__ == "__main__":
	# This is the main function
	fun("./hkp.wav") # A4
	fun("./kpt.wav") # C4

	

