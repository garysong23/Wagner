'''
Returns two transition segments by performing the following
1. Cut songs at specific time points
  Out song: mix_out -> mix_out + mix_len
  In song: mix_in -> mix_in + mix_len
2. Perform mutation if necessary
  Time stretching if songs have different BPMs
3. Write raw audio files to temp folder
4. Return path for transition segments
'''

import librosa
import numpy as np
import pyrubberband as pyrb

out_path, in_path = './output/temp/out.wav', './output/temp/in.wav'

# Same BPM transitions - Just write raw audio for crossfading
def normal(song_out, song_in, sr):
  librosa.output.write_wav(out_path, song_out.trans_out_audio(), sr)
  librosa.output.write_wav(in_path, song_in.trans_in_audio(), sr)
  return (out_path, in_path)

# Different BPM transitions - linear time stretch at each beat
# Done to prevent audio distortion
def stretch(song_out, song_in, mix_len, sr):
  # linear BPM increase at each beat
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
  samples = np.array([]).reshape(2,0)
  for i in range(len(beats)-1):
    # strech all samples between beat i to the begining of the next beat
    sample = librosa.frames_to_samples(beats[i:i+2])
    y_raw = song.raw_audio_duo[:, sample[0]:sample[1]]

    stretch_ratio = incre_bpm[i] / song.bpm
    # transpose here twice because pyrb takes (n,2) while librosa takes (2,n)
    t_y_raw = y_raw.transpose()
    t_y_stretch = pyrb.time_stretch(t_y_raw, sr, stretch_ratio)
    samples = np.concatenate([samples, t_y_stretch.transpose()], axis=1)

  return samples
