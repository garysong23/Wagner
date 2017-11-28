import threading
import time
import sys

BUFFER_CLEAR_SPEED = 500

class DataBuffer:
  def __init__(self):
    self.buffer = None
    self._monitor_thread = self._setup_monitor_thread()

  def on_input(self, val):
    if (val == 'stop') or (val == 'exit'):
      print("Terminating: I'll be back")
      sys.exit()
    self.buffer = val

  def _setup_monitor_thread(self):
    def background():
      while True:
        time.sleep(BUFFER_CLEAR_SPEED/1000)
        print('--- Current Buffer: ', self.buffer, ' ---\n')
    thread = threading.Thread(target=background)
    thread.daemon = True
    thread.start()
    return thread
