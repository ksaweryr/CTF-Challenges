import numpy as np
from scipy.fft import fft, fftfreq
from scipy.io import wavfile


def bits_to_bytes(bits):
    result = []

    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i:i+8]:
            byte *= 2
            byte += bit
        result.append(byte)
    
    return bytes(result)


samplerate, data = wavfile.read('challenge.wav')
N = samplerate // 5
xf = fftfreq(N, 1/samplerate)[:N//2]
j = np.where(xf == 20_000)[0][0]

bits = []

for i in range(0, len(data), N):
    yf = fft(data[i:i+N])
    if len(yf) < j:
        break
    bits.append(abs(yf[j].imag) >= 5e5)

print(bits_to_bytes(bits).strip().decode())
