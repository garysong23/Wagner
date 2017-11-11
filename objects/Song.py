from objects.song_helpers.parse_segment import parse_segment

class Song:
	def __init__(self, name, fname, mix_in, mix_out, unary_factor, song_id, bpm, key):
		print('Loading: ' + fname)
		self.bpm = bpm
		self.name = name

		mix_len = 32
		file_path = './data/mp3/' + fname
		self.audio_segment = parse_segment(file_path, mix_in, mix_out, mix_len)
		# self.file = fname
		# self.mix_in = mix_in
		# self.mix_out = mix_out
		# self.unary_factor = unary_factor
		# self.song_id = song_id
		# self.key = key
		# self.audio_beats = Audio('./data/mp3/' + fname)
		# self.audio_times = AudioSegment.from_file('./data/mp3/' + fname)

	def write_audio_segment(self):
		print('Writing: ' + self.name)
		self.audio_segment.export('./output/' + self.name + '.mp3', format='mp3')

	def __repr__(self):
		return self.name
