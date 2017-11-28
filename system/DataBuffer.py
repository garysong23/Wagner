class DataBuffer:
  def __init__(self):
    self.val = 0

  def on_input(self, val): self.val = val
  def status(self): return self.val
