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

	def __repr__(self):
		return self.name
