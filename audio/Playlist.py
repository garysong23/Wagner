from audio.Mashability import Mashability

class Playlist:
  def __init__(self, songs):
    self.playlist = self._sort_songs(songs)

  def _sort_songs(self, songs):
    pair_mashability = Mashability(songs)
