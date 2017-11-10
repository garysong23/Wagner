'''
Analyzes how well song1 transitions into song2.
Value is represented by a float between 0-1. With 0 being most mashable.
'''
import librosa
import numpy as np
import scipy.spatial.distance as dst

import visualize
from utils import transition_length

def mash_pairs(songs):
  pair_mashability = {}
  if (len(songs) < 2): return pair_mashability

  for i in range(len(songs)):
    for j in range(i+1, len(songs)):
      s1, s2 = songs[i], songs[j]
      pair_mashability[(s1, s2)] = _mashability(s1, s2)

  return pair_mashability

# analysis done using cosine matrix similarity
# and FFT semitone bin approximation matrices
def _mashability(song1, song2):
  bpm_diff = abs(song1.bpm - song2.bpm)
	# don't make transition if tempo difference > 30
  if (bpm_diff > 30): return 1

  f1, f2 = 'temp1.mp3', 'temp2.mp3'
  _write_temp_transition_file(song1, f1)
  _write_temp_transition_file(song2, f2)
  chroma1 = _chroma_from_file(f1)
  chroma2 = _chroma_from_file(f2)

  # visualize.chroma_comparison(song1.name, song2.name, chroma1, chroma2)

  orthogonal_arr = []
  for i in range(min(chroma1.shape[1],chroma2.shape[1])):
  	orthogonal_arr.append(dst.cosine(chroma1[:,i],chroma2[:,i]))
  return sum(orthogonal_arr)/len(orthogonal_arr)

def _write_temp_transition_file(song, file_name):
  transition_end = song.mix_out + transition_length(song.bpm)
  beats = song.audio[song.mix_out: transition_end]
  beats.export(file_name, format='mp3')

def _chroma_from_file(file_name):
  y, sr = librosa.load(file_name)
  S = np.abs(librosa.stft(y, n_fft = 4096))
  return librosa.feature.chroma_stft(S=S, sr=sr)
