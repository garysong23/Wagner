'''
Analyzes how well song1 transitions into song2.
Value is represented by a float between 0-1. With 0 being most mashable.
'''
import librosa
import numpy as np
import scipy.spatial.distance as dst
from pprint import pprint

import objects.mashability_helpers.visualize as visualize

class Mashability:
  def __init__(self, songs):
    mashability_index = self._generate_mashability_index(songs)

  def _generate_mashability_index(self, songs):
    pair_mashability = {}
    if (len(songs) < 2): return pair_mashability

    for i in range(len(songs)):
      for j in range(len(songs)):
        if (i == j): continue
        s1, s2 = songs[i], songs[j]
        pair_mashability[(s1, s2)] = self._get_mashability(s1, s2)

    pprint(pair_mashability)
    return pair_mashability

  # analysis done using cosine matrix similarity
  # and FFT semitone bin approximation matrices
  def _get_mashability(self, song1, song2):
    print('Mashability between: ' + song1.name + ' - ' + song2.name)
    bpm_diff = abs(song1.bpm - song2.bpm)
  	# don't make transition if tempo difference > 30
    if (bpm_diff > 30): return 1

    f1, f2 = './output/temp/temp1.mp3', './output/temp/temp2.mp3'
    song1.trans_out_segment().export(f1, format='mp3')
    song2.trans_in_segment().export(f2, format='mp3')
    chroma1 = self._chroma_from_file(f1)
    chroma2 = self._chroma_from_file(f2)

    # visualize.chroma_comparison(song1.name, song2.name, chroma1, chroma2)

    orthogonal_arr = []
    for i in range(min(chroma1.shape[1],chroma2.shape[1])):
    	orthogonal_arr.append(dst.cosine(chroma1[:,i],chroma2[:,i]))
    return sum(orthogonal_arr)/len(orthogonal_arr)

  def _chroma_from_file(self, file_name):
    y, sr = librosa.load(file_name)
    S = np.abs(librosa.stft(y, n_fft = 4096))
    return librosa.feature.chroma_stft(S=S, sr=sr)
