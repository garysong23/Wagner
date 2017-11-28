from system.DataBuffer import DataBuffer
from system.DataStream import DataStream

data_stream = DataStream()
data_buffer = DataBuffer()
data_stream.subscribe(data_buffer.on_input)

while True:
  data_stream.broadcast(input())
