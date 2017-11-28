import threading
import time
import sys

from system.DataBuffer import DataBuffer
from system.Threads import Threads
from system.DataStream import DataStream

data_stream = DataStream()
data_buffer = DataBuffer()
threads = Threads(data_buffer)

data_stream.subscribe(threads.on_input)
data_stream.subscribe(data_buffer.on_input)

while True:
  data_stream.broadcast(input())
