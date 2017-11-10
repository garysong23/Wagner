from mix.transition import transition_segment

MIX_LEN = 32

def mix_songs(songs):
  mix_two_songs(songs[1], songs[0])

def mix_two_songs(s1, s2):
  print('Mixing: ' + s1.name + ' + ' + s2.name)
  seg_1 = full_segment(s1)
  seg_2 = transition_segment(s1, s2, MIX_LEN)
  seg_3 = segment_post_transition(s2, MIX_LEN)

  mix = seg_1.append(seg_2).append(seg_3)
  seg_1.export('./output/seg_1.mp3', format='mp3')
  seg_2.export('./output/seg_2.mp3', format='mp3')
  seg_3.export('./output/seg_3.mp3', format='mp3')
  mix.export('./output/mix.mp3', format='mp3')

# get beats between mix_in-mix_out, used for first song
def full_segment(song):
  seg_begin = song.time_from_beat_begin(song.mix_in)
  seg_end = song.time_from_beat_begin(song.mix_out)
  segment = song.audio_times[seg_begin: seg_end]
  return segment

def segment_post_transition(song, mix_len):
  seg_begin = song.time_from_beat_end(song.mix_in + mix_len)
  seg_end = song.time_from_beat_begin(song.mix_out)
  segment = song.audio_times[seg_begin: seg_end]
  return segment
