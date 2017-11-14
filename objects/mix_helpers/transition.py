import librosa
import numpy as np
import pyrubberband as pyrb

from pydub import AudioSegment

out_path, in_path = './output/temp/out.wav', './output/temp/in.wav'

def normal(song_out, song_in, sr):
  librosa.output.write_wav(out_path, song_out.trans_out_audio(), sr)
  librosa.output.write_wav(in_path, song_in.trans_in_audio(), sr)
  return (out_path, in_path)

def stretch(song_out, song_in, mix_len, sr):
  incre_diff = (song_in.bpm - song_out.bpm) / mix_len
  incre_bpm = [song_out.bpm + (incre_diff * i) for i in range(1,mix_len+1)]

  out_beats = song_out.trans_out_beats()
  in_beats = song_in.trans_in_beats()
  if (len(out_beats) != len(in_beats)):
    print('Error: transition beat lengths are not equal.')
  out_samples = _stretched_audio_by_incre_bpm(song_out, out_beats, incre_bpm, sr)
  in_samples = _stretched_audio_by_incre_bpm(song_in, in_beats, incre_bpm, sr)

  librosa.output.write_wav(out_path, out_samples, sr)
  librosa.output.write_wav(in_path, in_samples, sr)

  return (out_path, in_path)

def _stretched_audio_by_incre_bpm(song, beats, incre_bpm, sr):
  samples = np.array([])
  for i in range(len(beats)-1):
    sample = librosa.frames_to_samples(beats[i:i+2])
    y_raw = song.raw_audio[sample[0]:sample[1]]

    stretch_ratio = incre_bpm[i] / song.bpm
    y_stretch = pyrb.time_stretch(y_raw, sr, stretch_ratio)
    samples = np.concatenate([samples, y_stretch])

  return samples
