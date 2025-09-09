import numpy as np
from scipy.io import wavfile

FLAG = b'justCTF{The-track-name-is-Coldness-and-the-artist-is-The-Wanderer}'


def bytes_to_bits(bs):
    for b in bs:
        for i in reversed(range(8)):
            yield (b >> i) & 1


def tone(freq, duration, samplerate):
    data = np.arange(0, duration, 1 / samplerate)
    return np.sin(freq * 2 * np.pi * data)


# https://freemusicarchive.org/music/stranger/seven-elements/coldness/
samplerate, music = wavfile.read('music.wav')

N = samplerate // 5

music = np.concatenate([np.repeat(0, 8 * N).astype(np.int16), music])

partials = [bit * .005 * 32767 * tone(20_000, 1/5, samplerate) for bit in bytes_to_bits(FLAG)]
partials.append(np.repeat(0, len(music) - len(partials) * N))

secret = np.concatenate(partials).astype(np.int16)
data = secret + music[:len(secret)]
wavfile.write('challenge.wav', samplerate, data)
