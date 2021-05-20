import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft # fourier transform
from scipy.io import wavfile # scipy library to read wav files

# read wav
nameOfSample = "sample_1.wav"
AudioName = nameOfSample
fs, Audiodata = wavfile.read(AudioName)

# time
length = Audiodata.shape[0] / fs
t = np.linspace(0., length, Audiodata.shape[0])

# time domain
fig, f1 = plt.subplots()
f1.plot(t, Audiodata)
f1.set(xlabel = 't(s)', ylabel='Signal', title = nameOfSample)

# Frequency domain
AudioFreq = fft(Audiodata)
bits = np.zeros((64, ))
bits = '0b'
i = 300000
while (300000 <= i and i < 300640):
    if (AudioFreq[i] <= 0) :
        bits += '0'
    if (AudioFreq[i] > 0) :
        bits += '1'
    i += 10
code = int(bits , 2).to_bytes((len(bits)-3 + 7) // 8, 'big').decode()
fig, f2 = plt.subplots()
f2.plot(np.arange(0, len(Audiodata)), np.real(AudioFreq))
f2.set(xlabel = 'Frequency(Hz)', ylabel='Signal', title = nameOfSample + " --> " + code)

plt.show()

