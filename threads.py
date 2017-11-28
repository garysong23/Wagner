import time
from system.DataPublisher import DataPublisher
from system.AudioStream import AudioStream

data_publisher = DataPublisher()
audio_stream = AudioStream()
data_publisher.subscribe(audio_stream.on_input)

audio_stream.start_stream()

print('[Threads] - Waiting for user input')
while True:
  data_publisher.broadcast(input())
