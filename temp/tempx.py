from itertools import chain
import numpy as np
import librosa
import soundfile as sf
import pyrubberband as pyrb
from pprint import pprint

song_out, song_in = './output/temp/temp1.wav', './output/temp/temp2.wav'
output_file = './output/temp/sf_4.wav'

MIX_LEN = 32
SAMPLE_RATE = 44100

y_out, _ = librosa.load(song_out, sr=SAMPLE_RATE)
y_in, _ = librosa.load(song_in, sr=SAMPLE_RATE)

out_bpm, beats_out = librosa.beat.beat_track(y=y_out, sr=SAMPLE_RATE)
in_bpm, beats_in = librosa.beat.beat_track(y=y_in, sr=SAMPLE_RATE)

incre_diff = (out_bpm - in_bpm) / MIX_LEN
incre_bpm = [in_bpm + (incre_diff * i) for i in range(1,MIX_LEN+1)]

out_samples, in_samples = np.array([]), np.array([])
for i in range(0,31):
  out_sample = librosa.frames_to_samples(beats_out[i:i+2])
  in_sample = librosa.frames_to_samples(beats_in[i:i+2])
  y_beat_out = y_out[out_sample[0]:out_sample[1]]
  y_beat_in = y_in[in_sample[0]:in_sample[1]]

  out_stretch_ratio = incre_bpm[i] / out_bpm
  in_stretch_ratio = incre_bpm[i] / in_bpm
  y_out_stretch = pyrb.time_stretch(y_beat_out, SAMPLE_RATE, out_stretch_ratio)
  y_in_stretch = pyrb.time_stretch(y_beat_in, SAMPLE_RATE, in_stretch_ratio)

  pprint(out_samples)
  pprint(y_out_stretch)
  out_samples = np.concatenate([out_samples, y_out_stretch])
  in_samples = np.concatenate([in_samples, y_in_stretch])

out_file = './output/temp/out.wav'
in_file = './output/temp/in.wav'

sf.write(out_file, out_samples, SAMPLE_RATE)
sf.write(in_file, in_samples, SAMPLE_RATE)
# file_name = './output/temp/' + str(i) + 'in.wav'
# sf.write(file_name, in_sample, SAMPLE_RATE)

#
#
# # Play back at double speed
# # y_stretch = pyrb.time_stretch(y2, sr_2, 0.904761904762)
# # sf.write(output_file, y_stretch, sr_2)
#
# # #mono=True, loads in a mono waveform
# # y1, sr_1 = librosa.load(f1, sr=44100)
# # y2, sr_2 = librosa.load(f2, sr=44100)
# #
# # tempo_1, _ = librosa.beat.beat_track(y=y1, sr=sr_1)
# # tempo_2, _ = librosa.beat.beat_track(y=y2, sr=sr_2)
# # new_tempo = tempo_1 / tempo_2
# # #
# # # print(new_tempo)
# # # print(sr_1)
# # # print(sr_2)
# # result = librosa.effects.time_stretch(y2, new_tempo)
# #
# # sf.write(output_file, result, 44100)
# # #
# # # output_file = './output/temp/lib_1.wav'
# # # librosa.output.write_wav(output_file, y1, sr_1)
