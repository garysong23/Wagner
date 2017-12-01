from system.signal_action_constants import SIG_ACTIONS

class SignalProcessor:
  def __init__(self):
    self.data_buffer = 5

  def on_signal(self, signal):
    print('[SignalProcessor] - Signal:', signal)
    self.data_buffer = int(signal)

  def interpret_signals(self):
    if self.data_buffer > 5:
      action = SIG_ACTIONS['increase']
    elif self.data_buffer < 5:
      action = SIG_ACTIONS['decrease']
    else:
      action = SIG_ACTIONS['maintain']

    print('[SignalProcessor] - Action:', action)
    return action
