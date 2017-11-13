import json
import librosa

SR, MIX_LEN = 44100, 32
DATA_SET = './data/json/diff_bpm.json'

def split_song(mix_in, mix_out, file_name):
  file_path = './data/mp3/' + file_name
  audio, _ = librosa.load(file_path, sr=SR)
  _, beats = librosa.beat.beat_track(y=audio, sr=SR)

  main = librosa.frames_to_samples(beats[mix_in:mix_out])
  trans_in = librosa.frames_to_samples(beats[mix_in:mix_in+MIX_LEN])
  trans_out = librosa.frames_to_samples(beats[mix_out:mix_out+MIX_LEN])

  main_audio = audio[main[0]: main[-1]]
  in_audio = audio[trans_in[0]: trans_in[-1]]
  out_audio = audio[trans_out[0]: trans_out[-1]]

  file_name = file_name.split('.')[0]
  librosa.output.write_wav('./output/'+file_name+'_main.wav', main_audio, SR)
  librosa.output.write_wav('./output/'+file_name+'_in.wav', in_audio, SR)
  librosa.output.write_wav('./output/'+file_name+'_out.wav', out_audio, SR)

with open(DATA_SET) as data_file:
  data = json.load(data_file)

songs = []
for song in data:
  mix_in = song['MixIn']
  mix_out = song['MixOut']
  file_name = song['File']
  split_song(mix_in, mix_out, file_name)
