from pydub import AudioSegment
from amen.audio import Audio
from objects.song_helpers.parse_segment import parse_segment
import librosa

SR = 44100

class Song:
	def __init__(self, name, fname, mix_in, mix_out, unary_factor, song_id, bpm, key):
		print('Loading: ' + fname)
		self.bpm = bpm
		self.name = name

		self._mix_in = mix_in
		self._mix_out = mix_out
		self._mix_len = 32

		file_path = './data/mp3/' + fname
		self._lib_audio, _ = librosa.load(file_path, sr=SR)
		_, self._lib_beats = librosa.beat.beat_track(y=self._lib_audio, sr=SR)

	def audio_segment(self):
		begin, end = self._mix_in, self._mix_out + self._mix_len
		sample = librosa.frames_to_samples(self._lib_beats[begin:end])
		return self._lib_audio[sample[0]: sample[-1]]

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
