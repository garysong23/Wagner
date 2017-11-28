import time
import pyaudio
import librosa
import threading
import numpy as np

SR = 44100

class AudioController:
  def __init__(self):
    self._audio_stream = np.array([], dtype='float32')
    self.append_streaming_audio('in')

    self._pyaudio = pyaudio.PyAudio()
    self._stream = self._pyaudio.open(
      format=pyaudio.paFloat32,
      channels=1,
      rate=SR,
      output=True,
      stream_callback=self._stream_callback,
    )

  def append_streaming_audio(self, audio_name):
    file_path = './data/wav/'+audio_name+'.wav'
    raw_audio, _ = librosa.load(file_path, sr=SR, mono=True)
    self._audio_stream = np.concatenate([self._audio_stream, raw_audio])

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

  def _stream_callback(self, in_data, frame_count, time_info, status):
    data = self._audio_stream[:frame_count]
    self._audio_stream = self._audio_stream[frame_count:]
    return (data, pyaudio.paContinue)

  def start_stream(self):
    def background():
      print('[AudioStream] - Starting Stream')
      self._stream.start_stream()
      while self._stream.is_active():
        time.sleep(1)

    thread = threading.Thread(target=background)
    thread.daemon = True
    thread.start()
    return thread

  def stop_stream(self):
    self._stream.stop_stream()
    self._stream.close()
    self._pyaudio.terminate()
