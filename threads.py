import time
from system.DataBuffer import DataBuffer
from system.DataStream import DataStream
from system.AudioStream import AudioStream

data_stream = DataStream()
data_buffer = DataBuffer()
data_stream.subscribe(data_buffer.on_input)

stream = AudioStream()
stream.start_stream()

print('[Threads] - Waiting for user input')
while True:
  data_stream.broadcast(input())
