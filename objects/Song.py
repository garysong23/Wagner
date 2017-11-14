'''
Song is divided into three sections. IN -> BODY -> OUT.
Sections IN and OUT are areas with overlap with other songs.
Length of these sections are determined by mix_len.
'''
import librosa

SR = 44100

class Song:
	def __init__(self, fname, mix_in, mix_out, bpm):
		self.bpm = bpm
		self.name = fname

		self._mix_in = mix_in
		self._mix_out = mix_out
		self._mix_len = 32

		file_path = './data/mp3/' + fname
		self.raw_audio, _ = librosa.load(file_path, sr=SR)
		_, self._beats = librosa.beat.beat_track(y=self.raw_audio, sr=SR, bpm=bpm)

	def body_audio(self):
		begin, end = self._mix_in + self._mix_len, self._mix_out
		samples = librosa.frames_to_samples(self._beats[begin: end])
		return self.raw_audio[samples[0]: samples[-1]]

	def trans_in_audio(self):
		begin, end = self._mix_in, self._mix_in + self._mix_len
		samples = librosa.frames_to_samples(self._beats[begin: end])
		return self.raw_audio[samples[0]: samples[-1]]

	def trans_out_audio(self):
		begin, end = self._mix_out, self._mix_out + self._mix_len
		samples = librosa.frames_to_samples(self._beats[begin: end])
		return self.raw_audio[samples[0]: samples[-1]]

	def trans_in_beats(self):
		begin, end = self._mix_in, self._mix_in + self._mix_len
		return self._beats[begin: end]

	def trans_out_beats(self):
		begin, end = self._mix_out, self._mix_out + self._mix_len
		return self._beats[begin: end]

	def __repr__(self):
		return self.name.split('.')[0]
