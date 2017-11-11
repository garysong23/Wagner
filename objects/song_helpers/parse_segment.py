'''
Converts beat numbers range to timestamp range.
'''

def parse_segment(audio_beats, audio_times, begin, end):
  begin_time = _segment_begin_time(begin, audio_beats)
  end_time = _segment_end_time(end, audio_beats)
  return audio_times[begin_time: end_time]

def _segment_begin_time(b, audio_beats):
	beats = audio_beats.timings['beats']
	return beats[b].time.total_seconds() * 1000

def _segment_end_time(b, audio_beats):
	beats = audio_beats.timings['beats']
	time_begin = beats[b].time.total_seconds() * 1000
	time_dur = beats[b].duration.total_seconds() * 1000
	return (time_begin + time_dur)
