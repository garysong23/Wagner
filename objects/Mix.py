'''
Mix object creates a mix from an array of songs.
'''
import numpy as np
import librosa
from objects.Transition import Transition

sr = 44100
mix_len = 32

class Mix:
  def __init__(self, songs):
    print('Mix sequence: ')
    for i in range(len(songs)):
      print(songs[i].name)

    self.mix_path = self._mix_songs(songs)

  # Writes the full mix to out_path
  def _mix_songs(self, songs):
    cur_bpm = songs[0].bpm
    # builds first song
    mix_full = np.concatenate([
      songs[0].trans_in_audio(),
      songs[0].body_audio(),
    ])

    for i in range(0, len(songs)-1):
      out_song, in_song = songs[i], songs[i+1]
      transition = Transition(out_song, in_song, mix_len)
      trans_audio = transition.merged_audio
      mix_full = np.concatenate([mix_full, trans_audio, in_song.body_audio()])
    out_path = './output/full.wav'
    librosa.output.write_wav(out_path, mix_full, sr)
    return out_path
