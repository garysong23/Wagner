class DataPublisher:
  def __init__(self):
    self.observers = []

  def broadcast(self, val):
    for obv in self.observers:
      obv(val)

  def subscribe(self, event):
    self.observers.append(event)
