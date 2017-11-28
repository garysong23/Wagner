import librosa
from pprint import pprint
import numpy as np

SR = 44100

file_path = './data/mp3/Alive.mp3'
f1, _ = librosa.load(file_path, sr=SR, mono=False)
f2, _ = librosa.load(file_path, sr=SR, mono=True)
_, b = librosa.beat.beat_track(y=f2, sr=SR)

begin, end = 64, 128
s = librosa.frames_to_samples(b[begin: end])

print(s[0], s[-1])
r1 = f1[:,s[0]:s[-1]]
r2 = f2[s[0]:s[-1]]
print(f1.shape, r1.shape)
print(f2.shape, r2.shape)

librosa.output.write_wav('./output/try.wav', r1, SR)
