from amen.synthesize import synthesize

from utils import transition_length
from pprint import pprint

def blend_song(song_list):
  _make_transition(song_list[0], song_list[1])
  return

def _make_transition(song_in, song_out):
  mix_len = 32
  in_beats_begin = song_in.mix_in
  in_beats_end = song_in.mix_in + mix_len
  in_begin, in_end = _begin_end_time(song_in, in_beats_begin, in_beats_end)

  out_beats_begin = song_out.mix_out
  out_beats_end = song_out.mix_out + mix_len
  out_begin, out_end = _begin_end_time(song_out, out_beats_begin, out_beats_end)

  trans_in = song_in.audio_times[in_begin: in_end]
  trans_out = song_out.audio_times[out_begin: out_end]
  trans_in.export('trans_in.mp3', format='mp3')
  trans_out.export('trans_out.mp3', format='mp3')

  # TODO: this could be adjusted by bpm and transition seconds
  trans_length = int(in_end - in_begin) - 1
  print('Transtion Length: ' + str(trans_length/1000))
  trans_comb = trans_out.append(trans_in, crossfade=trans_length)
  trans_comb.export('trans_comb.mp3', format='mp3')
