import threading
import time
import sys

class DataBuffer:
  def __init__(self):
    self.val = 0
    self._bg_thread = self._setup_bg_thread()

  def on_input(self, val):
    if (val == 'stop') or (val == 'exit'):
      print("Terminating: I'll be back")
      sys.exit()
    self.val = val

  def _setup_bg_thread(self):
    thread = threading.Thread(target=self._background)
    thread.daemon = True
    thread.start()
    return thread

  def _background(self):
    while True:
      time.sleep(5)
      print('Current val: ', self.val)
