'''
Mix object creates a mix from an array of songs.
'''
import numpy as np
import librosa
from audio.Transition import Transition

sr = 44100
mix_len = 32

class Mix:
  def __init__(self, songs):
    print('Mix sequence: ')
    for i in range(len(songs)):
      print(songs[i].name)

    self.out_path = './output/full.wav'
    self._mix_songs(self.out_path, songs)

  # Writes the full mix to out_path
  def _mix_songs(self, path, songs):
    s1 = songs[0]
    # builds first song
    mix_full = np.concatenate([s1.trans_in_audio(), s1.body_audio()], axis=1)
    for i in range(0, len(songs)-1):
      out_song, in_song = songs[i], songs[i+1]
      transition = Transition(out_song, in_song, mix_len)
      trans_audio = transition.merged_audio
      mix_full = np.concatenate([mix_full, trans_audio, in_song.body_audio()], axis=1)
    librosa.output.write_wav(path, mix_full, sr)
