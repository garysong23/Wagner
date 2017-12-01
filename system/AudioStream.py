import time
import pyaudio

SR = 44100

class AudioStream:
  def __init__(self, on_stream_callback):
    self._on_stream_callback = on_stream_callback
    self._stream = None

  def start_stream(self):
    print('[AudioStream] - Start stream')
    self._stream = pyaudio.PyAudio().open(
      format=pyaudio.paFloat32,
      channels=2,
      rate=SR,
      output=True,
      stream_callback=self._stream_callback,
    )

  def pause_stream(self):
    if not self._stream: return
    print('[AudioStream] - Pausing stream')
    self._stream.stop_stream()

  def stop_stream(self):
    if not self._stream: return
    print('[AudioStream] - Stopping stream')
    self._stream.close()

  def _stream_callback(self, in_data, frame_count, time_info, status):
    data = self._on_stream_callback(frame_count)
    return (data, pyaudio.paContinue)
