from pydub import AudioSegment
from amen.audio import Audio

class Song(object):
	def __init__(self, name, fname, mix_in, mix_out, unary_factor, song_id, bpm, key):
		print('Loading: ' + fname)
		self.bpm = bpm
		self.name = name
		self.file = fname
		self.mix_in = mix_in
		self.mix_out = mix_out
		self.unary_factor = unary_factor
		self.song_id = song_id
		self.key = key
		self.audio_beats = Audio('./data/mp3/' + fname)
		self.audio_times = AudioSegment.from_file('./data/mp3/' + fname)

	def time_from_beat_begin(self, b):
		beats = self.audio_beats.timings['beats']
		return beats[b].time.total_seconds() * 1000

	def time_from_beat_end(self, b):
		beats = self.audio_beats.timings['beats']
		time_begin = beats[b].time.total_seconds() * 1000
		time_dur = beats[b].duration.total_seconds() * 1000
		return (time_begin + time_dur)

	def __repr__(self):
		return self.name
