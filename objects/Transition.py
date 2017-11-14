'''
Songs transition by crossfading song_out with song_in.
Songs with different BPMs are time stretched to sync beats.
'''
import librosa
import objects.transition_helpers.segment as segment
from objects.transition_helpers.cross_fade import crossfade_files

SR = 44100

class Transition:
  def __init__(self, out_song, in_song, mix_len):
    self.mix_len = mix_len
    self.out_path, self.in_path = self._transition_segments(out_song, in_song)
    self.merged_path = self._merged_segment_path(self.out_path, self.in_path)
    self.merged_audio = self._merged_segment_audio(self.merged_path)

  # Returns the raw audio of the transition segment
  def _transition_segments(self, out_song, in_song):
    if (out_song.bpm == in_song.bpm):
      out_path, in_path = segment.normal(out_song, in_song, SR)
    else:
      out_path, in_path = segment.stretch(out_song, in_song, self.mix_len, SR)
    return (out_path, in_path)

  def _merged_segment_path(self, out_path, in_path):
    return crossfade_files(out_path, in_path)

  def _merged_segment_audio(self, merged_path):
    trans, _ = librosa.load(merged_path, sr=SR)
    return trans
