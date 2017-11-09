from pydub import AudioSegment

class Song(object):
	def __init__(self, name, fname, mix_in, mix_out, unary_factor, song_id, bpm, key):
		self.name = name
		self.file = fname
		self.mix_in = mix_in
		self.mix_out = mix_out
		self.unary_factor = unary_factor
		self.song_id = song_id
		self.bpm = bpm
		self.key = key
		self.audio = AudioSegment.from_mp3('./data/mp3/' + fname)

	def __repr__(self):
		return self.name
