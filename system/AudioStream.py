import time
import pyaudio
import librosa
import threading

SR = 44100

class AudioStream:
  def __init__(self):
    self.cur_audio = []
    file_path = './data/wav/out.wav'
    self.audio, _ = librosa.load(file_path, sr=SR, mono=True)

    self._pyaudio = pyaudio.PyAudio()
    self._stream = self._pyaudio.open(
      format=pyaudio.paFloat32,
      channels=1,
      rate=SR,
      output=True,
      stream_callback=self._stream_callback,
    )

  def _stream_callback(self, in_data, frame_count, time_info, status):
    data = self.audio[:frame_count]
    self.audio = self.audio[frame_count:]
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
