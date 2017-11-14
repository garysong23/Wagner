import numpy as np
import librosa
import objects.mix_helpers.transition as transition
from objects.mix_helpers.cross_fade import crossfade_files

sr = 44100
mix_len = 32

class Mix:
  def __init__(self, songs):
    print('Mix sequence: ')
    for i in range(len(songs)):
      print(songs[i].name)

    self.mix_path = self._mix_songs(songs)

  def _mix_songs(self, songs):
    cur_bpm = songs[0].bpm
    mix_full = np.concatenate([songs[0].trans_in_audio(), songs[0].body_audio()])
    for i in range(0, len(songs)-1):
      out_song, in_song = songs[i], songs[i+1]
      trans_audio = self._transition_segment(out_song, in_song)
      mix_full = np.concatenate([mix_full, trans_audio, in_song.body_audio()])
    out_path = './output/full.wav'
    librosa.output.write_wav(out_path, mix_full, sr)
    return out_path

  def _transition_segment(self, out_song, in_song):
    if (out_song.bpm == in_song.bpm):
      out_path, in_path = transition.normal(out_song, in_song, sr)
    else:
      out_path, in_path = transition.stretch(out_song, in_song, mix_len, sr)

    trans_path = crossfade_files(out_path, in_path)
    trans, _ = librosa.load(trans_path, sr=sr)
    return trans
