from amen.synthesize import synthesize

from utils import transition_length
from pprint import pprint

MIX_LEN = 32

def blend_song(song_list):
  _make_transition(song_list[0], song_list[1])
  return

def _make_transition(song_in, song_out):
  times = _get_transition_timestamps(song_in, song_out)
  # TODO: this could be adjusted by bpm and transition seconds
  trans_length = int(times['in'][0] - times['in'][1]) - 1
  in_seg = song_in.audio_times[times['in'][0]: times['in'][1]]
  out_seg = song_out.audio_times[times['out'][0]: times['out'][1]]
  if (song_in.bpm == song_out.bpm):
    _make_same_bpm_transition(in_seg, out_seg, trans_length)
  else:
    pass

def _get_transition_timestamps(song_in, song_out):
  in_beat_begin = song_in.mix_in
  in_beat_end = song_in.mix_in + MIX_LEN
  in_begin, in_end = _begin_end_time(song_in, in_beat_begin, in_beat_end)

  out_beat_begin = song_out.mix_out
  out_beat_end = song_out.mix_out + MIX_LEN
  out_begin, out_end = _begin_end_time(song_out, out_beat_begin, out_beat_end)
  return { 'in': (in_begin, in_end), 'out': (out_begin, out_end) }

def _begin_end_time(song, beat_begin, beat_end):
  beats = song.audio_beats.timings['beats']
  begin_time = beats[beat_begin].time.total_seconds() * 1000
  end_time_begin = beats[beat_end].time.total_seconds() * 1000
  end_time_dur = beats[beat_end].duration.total_seconds() * 1000
  end_time = end_time_begin + end_time_dur

  return (begin_time, end_time)

def _make_same_bpm_transition(in_seg, out_seg, trans_length):
  in_seg.export('./output/trans_in.mp3', format='mp3')
  out_seg.export('./output/trans_out.mp3', format='mp3')

  print('Transtion Length: ' + str(trans_length/1000))
  trans_comb = out_seg.append(in_seg, crossfade=trans_length)
  trans_comb.export('./output/trans_comb.mp3', format='mp3')
