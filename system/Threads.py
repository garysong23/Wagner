import threading
import time
import sys

class Threads:
  def __init__(self, data_buffer):
    self._data_buffer = data_buffer
    self._bg_thread = self._setup_bg_thread()

  def on_input(self, val):
    if (val == 'stop') or (val == 'exit'):
      print("Terminating: I'll be back")
      sys.exit()

  def _setup_bg_thread(self):
    thread = threading.Thread(target=self._background)
    thread.daemon = True
    thread.start()
    return thread

  def _background(self):
    while True:
      time.sleep(5)
      print('Current val: ', self._data_buffer.status())
