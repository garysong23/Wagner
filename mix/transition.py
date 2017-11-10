'''
Produces a transition mix between song_out and song_in.
Transition happens at the end of song_out.
Duration is equal to mix_len in the number of beats.
'''
from amen.synthesize import synthesize

from utils import transition_length
from pprint import pprint


# make a transition at song_out.mix_out and song_in.mix_in.
# crossfading for mix_len beats
def transition_segment(song_out, song_in, mix_len):
  times = _get_transition_timestamps(song_in, song_out, mix_len)

  # TODO: this could be adjusted by bpm and transition seconds
  trans_length = int(times['in'][1] - times['in'][0]) - 1
  in_seg = song_in.audio_times[times['in'][0]: times['in'][1]]
  out_seg = song_out.audio_times[times['out'][0]: times['out'][1]]
  if (song_in.bpm == song_out.bpm):
    return _make_same_bpm_transition(in_seg, out_seg, trans_length)
  else:
    pass

def _get_transition_timestamps(song_in, song_out, mix_len):
  in_begin = song_in.time_from_beat_begin(song_in.mix_in)
  in_end = song_in.time_from_beat_end(song_in.mix_in + mix_len)

  out_begin = song_out.time_from_beat_begin(song_out.mix_out)
  out_end = song_out.time_from_beat_end(song_out.mix_out + mix_len)

  res = { 'in': (in_begin, in_end), 'out': (out_begin, out_end) }
  return res

def _make_same_bpm_transition(in_seg, out_seg, trans_length):
  in_seg.export('./output/trans_in.mp3', format='mp3')
  out_seg.export('./output/trans_out.mp3', format='mp3')

  print('Transtion Length: ' + str(trans_length/1000))
  trans_comb = out_seg.append(in_seg, crossfade=trans_length)
  # trans_comb.export('./output/trans_comb.mp3', format='mp3')
  return trans_comb
