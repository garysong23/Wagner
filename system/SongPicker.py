import librosa
import numpy as np

SR = 44100

class SongPicker:
  def pick_song(vals):
    audio_name = 'in'
    file_path = './data/wav/'+audio_name+'.wav'
    raw_audio, _ = librosa.load(file_path, sr=SR, mono=True)
    print('[SongPicker] - Picked:', audio_name)
    return raw_audio
