import pyaudio
import librosa
import threading
import time
import numpy as np

SR = 44100
file_path = './output/temp/in.wav'
stream_data, _ = librosa.load(file_path, sr=SR, mono=False)

def stream_callback(in_data, frame_count, time_info, status):
  global stream_data
  data = stream_data[:, :frame_count]
  stream_data = stream_data[:, frame_count:]
  waved_data = np.vstack((data[0],data[1])).reshape((-1,),order='F')
  return (waved_data, pyaudio.paContinue)

p = pyaudio.PyAudio()
stream = p.open(
  format=pyaudio.paFloat32,
  channels=2,
  rate=SR,
  output=True,
  stream_callback=stream_callback,
)

stream.start_stream()

while stream.is_active():
  time.sleep(0.1)
