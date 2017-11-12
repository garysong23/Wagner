import librosa

f1, f2 = './output/temp/temp1.mp3', './output/temp/temp2.mp3'
x, sr_x = librosa.load(f1)
y, sr_y = librosa.load(f2)

y_harmonic, y_percussive = librosa.effects.hpss(y)
x_harmonic, x_percussive = librosa.effects.hpss(x)

tempo_x, beats_x = librosa.beat.beat_track(y=x_percussive, sr=sr_x, trim=True)
tempo_y, beats_y = librosa.beat.beat_track(y=y_percussive, sr=sr_y, trim=True)

print(tempo_x)
print(tempo_y)


f1, f2 = './output/temp/mix1.mp3', './output/temp/mix2.mp3'
x, sr_x = librosa.load(f1)
y, sr_y = librosa.load(f2)

y_harmonic, y_percussive = librosa.effects.hpss(y)
x_harmonic, x_percussive = librosa.effects.hpss(x)

tempo_x, beats_x = librosa.beat.beat_track(y=x_percussive, sr=sr_x, trim=True)
tempo_y, beats_y = librosa.beat.beat_track(y=y_percussive, sr=sr_y, trim=True)

print(tempo_x)
print(tempo_y)



f1, f2 = './output/temp/out1.mp3', './output/temp/out2.mp3'
x, sr_x = librosa.load(f1)
y, sr_y = librosa.load(f2)

y_harmonic, y_percussive = librosa.effects.hpss(y)
x_harmonic, x_percussive = librosa.effects.hpss(x)

tempo_x, beats_x = librosa.beat.beat_track(y=x_percussive, sr=sr_x, trim=True)
tempo_y, beats_y = librosa.beat.beat_track(y=y_percussive, sr=sr_y, trim=True)

print(tempo_x)
print(tempo_y)
