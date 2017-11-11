class Mix:
  def __init__(self, songs):
    self.mix = self._mix_songs(songs)

  def _mix_songs(self, songs):
    mix = songs[0].audio_segment
    for i in range(1, len(songs)):
      new_seg = songs[i].audio_segment
      mix = mix.append(new_seg, crossfade=15000)
    return mix

  def write_mix(self):
    print('Writing Mix')
    self.mix.export('./output/mix.mp3', format='mp3')
