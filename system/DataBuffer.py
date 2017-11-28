import threading
import time
import sys

import pygame

BUFFER_CLEAR_SPEED = 500

class DataBuffer:
  def __init__(self):
    self.buffer = []
    self._monitor_thread = self._setup_monitor_thread()
    title = './data/chopped/body/Outside.wav'

  def on_input(self, val):
    if (val == 'stop') or (val == 'exit'):
      print("Terminating: I'll be back")
      sys.exit()
    elif (val == 'mix'):
      print('mixing')
      title = './data/chopped/body/SafeSound.wav'

    self.buffer.append(val)

  def _setup_monitor_thread(self):
    def background():
      while True:
        time.sleep(BUFFER_CLEAR_SPEED/1000)
        if self.buffer: self.buffer.pop(0)
        print('--- Current Buffer: ', self.buffer, '\n')
    thread = threading.Thread(target=background)
    thread.daemon = True
    thread.start()
    return thread
