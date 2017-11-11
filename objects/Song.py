from pydub import AudioSegment
from amen.audio import Audio
from objects.song_helpers.parse_segment import parse_segment

class Song:
	def __init__(self, name, fname, mix_in, mix_out, unary_factor, song_id, bpm, key):
		print('Loading: ' + fname)
		self.bpm = bpm
		self.name = name

		self._mix_in = mix_in
		self._mix_out = mix_out
		self._mix_len = 32

		file_path = './data/mp3/' + fname
		self._audio_beats = Audio(file_path)
		self._audio_times = AudioSegment.from_file(file_path)

		# self.file = fname
		# self.mix_in = mix_in
		# self.mix_out = mix_out
		# self.unary_factor = unary_factor
		# self.song_id = song_id
		# self.key = key
		# self.audio_beats = Audio('./data/mp3/' + fname)
		# self.audio_times = AudioSegment.from_file('./data/mp3/' + fname)

	def audio_segment(self):
		begin, end = self._mix_in, self._mix_out + self._mix_len
		segment = parse_segment(self._audio_beats, self._audio_times, begin, end)
		return segment

	def trans_in_segment(self):
		begin, end = self._mix_in, self._mix_in + self._mix_len
		segment = parse_segment(self._audio_beats, self._audio_times, begin, end)
		return segment

	def trans_out_segment(self):
		begin, end = self._mix_out, self._mix_out + self._mix_len
		segment = parse_segment(self._audio_beats, self._audio_times, begin, end)
		return segment

	def write_audio_segment(self, file_path=None):
		print('Writing: ' + self.name)
		if not file_path:
			file_path = './output/' + self.name + '.mp3'
		self.audio_segment.export(file_path, format='mp3')

	def __repr__(self):
		return self.name
