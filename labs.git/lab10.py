import numpy as np 
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy.signal import lfilter, freqz

def signal(t):
	return np.cos(2*np.pi*10*t)+np.cos(2*np.pi*100*t)+np.cos(2*np.pi*200*t)


# Create 3 plots
f, xarr = plt.subplots(3)

# Pretify the spacing
plt.subplots_adjust(hspace = 1.25)

# Unfiltered plot
# A 2 second time measurement
t = np.linspace(0, 2, 1000) # start, stop, #element
sig = signal(t)

xarr[0].set_title("Unfiltered Plot")
xarr[0].set_xlabel("time")
xarr[0].set_ylabel("Volts")
xarr[0].plot(t, sig)

# FFT plot
freq = np.linspace(0, 500, 1000)
fft_sig = fft(sig)

xarr[1].set_title("FFT Plot")
xarr[1].set_xlabel("frequency")
xarr[1].set_ylabel("amplitude")
# essentially cutting the graph in half
xarr[1].plot(freq[0:499], np.abs(fft_sig)[0:499]) 

# IFFT plot
ifft_t = np.linspace(0, 2, 1000)
ifft_sig = ifft(fft_sig)

xarr[2].set_title("IFFT Plot")
xarr[2].set_xlabel("time")
xarr[2].set_ylabel("Volts")
xarr[2].plot(ifft_t, ifft_sig)


# Time Domain Filtering Found Below
N = 15
b = (1/N)*np.ones(N)

# Create 3 plots
f2, xarr2 = plt.subplots(3)

# Pretify the spacing
plt.subplots_adjust(hspace = 1.25)

# Unfiltered plot
# A 2 second time measurement
t = np.linspace(0, 2, 1000) # start, stop, #element
sig = signal(t)

# Unfiltered Plot Part 2, Electric Boogaloo
xarr2[0].set_title("Unfiltered Plot")
xarr2[0].set_xlabel("time")
xarr2[0].set_ylabel("Volts")
xarr2[0].plot(t, sig)

# I already had the space for this plot so felt the need to include it
xarr2[1].set_title("Ignorable Filter Impulse")
xarr2[1].set_xlabel("impulses")
xarr2[1].set_ylabel("amplitude")
xarr2[1].stem(b) # I have no idea what the red line is

# Filtered output
filterOut = lfilter(b, 1, sig)
xarr2[2].set_title("Filter Output")
xarr2[2].set_xlabel("time")
xarr2[2].set_ylabel("Volts")
xarr2[2].plot(t, filterOut)


# Frequency Domain Filtering Stuff should be found below this very line
sampleRate = 500
hz, H = freqz(b, 1, worN=freq*2*np.pi/sampleRate)
hzTrue = hz*sampleRate/(2*np.pi)

# Create 3 plots
f3, xarr3 = plt.subplots(3)

# Pretify the spacing
plt.subplots_adjust(hspace = 1.25)

# Amplitude Spectrum (real half)
xarr3[0].set_title("Amplitude spectrum")
xarr3[0].set_xlabel("frequency")
xarr3[0].set_ylabel("amplitude")
xarr3[0].plot(freq[0:499], np.abs(fft_sig)[0:499])

# Frequency Response of the Filter
xarr3[1].set_title("Frequency Response of Filter")
xarr3[1].set_xlabel("frequency")
xarr3[1].set_ylabel("amplitude")
xarr3[1].plot(hzTrue[0:499], H[0:499])

# Filter Output
wFilterOut = H*fft_sig
xarr3[2].set_title("Filter Output")
xarr3[2].set_xlabel("frequency")
xarr3[2].set_ylabel("amplitude")
xarr3[2].plot(freq[0:499], wFilterOut[0:499])

# Final round ... FIGHT (read in Street Fighter 2 Voice)
# Create 4 plots
f4, xarr4 = plt.subplots(4)

# Pretify the spacing
plt.subplots_adjust(hspace = 1.5)

# Filtered Waveform (convolution approach)
xarr4[0].set_title("Filtered Waveform (convolution approach)")
xarr4[0].set_xlabel("Volts")
xarr4[0].set_ylabel("time")
xarr4[0].plot(t, filterOut)

# FFT of convolution approach
xarr4[1].set_title("FFT of convolution approach")
xarr4[1].set_xlabel("Volts")
xarr4[1].set_ylabel("time")
xarr4[1].plot(t[0:499], fft(filterOut)[0:499])

# Filtered Waveform (FFT)
xarr4[2].set_title("Filtered Waveform (FFT)")
xarr4[2].set_xlabel("frequency")
xarr4[2].set_ylabel("amplitude")
xarr4[2].plot(freq[0:499], wFilterOut[0:499])

# IFFT of FFT Approach
xarr4[3].set_title("IFFT of FFT Approach")
xarr4[3].set_xlabel("time")
xarr4[3].set_ylabel("amplitude")
xarr4[3].plot(t, ifft(wFilterOut))

plt.show()
