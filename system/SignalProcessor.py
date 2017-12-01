class SignalProcessor:
  def __init__(self):
    self.data_buffer = []

  def on_signal(self, signal):
    print('[SignalProcessor] - Signal:', signal)
    self.data_buffer.append(signal)

  def extract_last(self):
    return self.data_buffer[-1]
