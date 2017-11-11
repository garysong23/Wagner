from pydub import AudioSegment
from amen.audio import Audio

def parse_segment(file_path, mix_in, mix_out, mix_len):
  audio_beats = Audio(file_path)
  audio_times = AudioSegment.from_file(file_path)

  begin_time = _segment_begin_time(mix_in, audio_beats)
  end_time = _segment_end_time(mix_out + mix_len, audio_beats)

  return audio_times[begin_time: end_time]

def _segment_begin_time(b, audio_beats):
	beats = audio_beats.timings['beats']
	return beats[b].time.total_seconds() * 1000

def _segment_end_time(b, audio_beats):
	beats = audio_beats.timings['beats']
	time_begin = beats[b].time.total_seconds() * 1000
	time_dur = beats[b].duration.total_seconds() * 1000
	return (time_begin + time_dur)
