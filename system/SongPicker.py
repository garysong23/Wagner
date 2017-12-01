import librosa
import numpy as np
from system.signal_action_constants import SIG_ACTIONS

SR = 44100

class SongPicker:
  def pick_song(self, sig_action):
    audio_name = 'in'
    file_path = './data/wav/'+audio_name+'.wav'
    raw_audio, _ = librosa.load(file_path, sr=SR, mono=True)
    return raw_audio
