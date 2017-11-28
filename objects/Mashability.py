'''
Analyzes how well song1 transitions into song2.
Value is represented by a float between 0-1. With 0 being most mashable.
'''
import librosa
import numpy as np
import scipy.spatial.distance as dst
from pprint import pprint

from objects.Transition import Transition
import objects.mashability_helpers.visualize as visualize
from objects.mashability_helpers.sequence import sequence_for_mash_index

class Mashability:
  def __init__(self, songs):
    self.mash_index = self._generate_mashability_index(songs)
    self.seq, self.val = sequence_for_mash_index(songs, self.mash_index)
    print('Selected sequence: ')
    pprint(self.seq)

  def _generate_mashability_index(self, songs):
    pair_mashability = {}
    if (len(songs) < 2): return pair_mashability
    for i in range(len(songs)):
      for j in range(len(songs)):
        if (i == j): continue
        s1, s2 = songs[i], songs[j]
        pair_mashability[(s1, s2)] = self._get_mashability(s1, s2)
    return pair_mashability

  # Analysis done using cosine matrix similarity
  #   and FFT semitone bin approximation matrices
  def _get_mashability(self, song1, song2):
    print('Mashability between: ' + song1.name + ' - ' + song2.name)
    bpm_diff = abs(song1.bpm - song2.bpm)
  	# Don't make transition if tempo difference > 30
    if (bpm_diff > 30): return 1

    mix_len = 32
    transition = Transition(song1, song2, mix_len)
    chroma1 = self._chroma_from_file(transition.out_path)
    chroma2 = self._chroma_from_file(transition.in_path)

    # visualize.chroma_comparison(song1.name, song2.name, chroma1, chroma2)

    orthogonal_arr = []
    for i in range(min(chroma1.shape[1],chroma2.shape[1])):
    	orthogonal_arr.append(dst.cosine(chroma1[:,i],chroma2[:,i]))
    return sum(orthogonal_arr)/len(orthogonal_arr)

  def _chroma_from_file(self, file_name):
    y, sr = librosa.load(file_name)
    S = np.abs(librosa.stft(y, n_fft = 4096))
    return librosa.feature.chroma_stft(S=S, sr=sr)
