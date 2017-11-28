import time
import pyaudio
import librosa
import numpy as np

SR = 44100
BUFFER_SIZE = 44100*4

file_path = './data/wav/out.wav'
audio, _ = librosa.load(file_path, sr=SR, mono=True)

def callback(in_data, frame_count, time_info, status):
  global audio
  data = audio[:frame_count]
  audio = audio[frame_count:]
  return (data, pyaudio.paContinue)

p = pyaudio.PyAudio()
stream = p.open(
  format=pyaudio.paFloat32,
  channels=1,
  rate=44100,
  output=True,
  stream_callback=callback,
)

stream.start_stream()

while stream.is_active():
  print('sleeping')
  time.sleep(0.1)

stream.stop_stream()
stream.close()
p.terminate()
