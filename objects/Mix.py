from objects.mix_helpers.time_stretch import time_stretch

class Mix:
  def __init__(self, songs):
    self.mix = self._mix_songs(songs)

  def _mix_songs(self, songs):
    cur_bpm = songs[0].bpm
    mix = songs[0].audio_segment()
    for i in range(1, len(songs)):
      if (cur_bpm == songs[i].bpm):
        new_seg = songs[i].audio_segment()
      mix = mix.append(new_seg, crossfade=15000)
    return mix

  def write_mix(self):
    print('Writing Mix')
    self.mix.export('./output/mix.mp3', format='mp3')
