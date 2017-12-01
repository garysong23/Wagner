from system.signal_action_constants import SIG_ACTIONS

class SignalProcessor:
  def __init__(self):
    self.data_buffer = []

  def on_signal(self, signal):
    print('[SignalProcessor] - Signal:', signal)
    self.data_buffer.append(signal)

  def interpret_signals(self):
    action = SIG_ACTIONS['maintain']

    print('[SignalProcessor] - Action:', action)
    return action
