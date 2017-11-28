import librosa
import numpy as np

from system.AudioStream import AudioStream

SR = 44100

class AudioController:
  def __init__(self):
    self._stream_data = np.array([], dtype='float32')
    self.append_streaming_audio('in')
    self._audio_stream = AudioStream(self._on_stream_callback)

  def _on_stream_callback(self, frame_count):
    data = self._stream_data[:frame_count]
    self._stream_data = self._stream_data[frame_count:]
    return data

  def append_streaming_audio(self, audio_name):
    file_path = './data/wav/'+audio_name+'.wav'
    raw_audio, _ = librosa.load(file_path, sr=SR, mono=True)
    self._stream_data = np.concatenate([self._stream_data, raw_audio])

  def on_signal_input(self, msg):
    if (msg == '1'):
      self._audio_buffer = self.append_streaming_audio('in')
    if (msg == '2'):
      self._audio_buffer = self.append_streaming_audio('out')
    elif (msg == 'stop') or (msg == 'exit'):
      print("Terminating: I'll be back")
      self.stop_stream()
      sys.exit()
    else:
      return

  def start_stream(self): self._audio_stream.start_stream()
  def stop_stream(self): self._audio_stream.stop_stream()
