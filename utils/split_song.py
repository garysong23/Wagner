'''
Split audio file into three chunks based on provided DATA_SET
  trans_in | body | trans_out
data saved at ./data/chopped/
'''
import json
import librosa

SR, MIX_LEN = 44100, 32
DATA_SET = './data/json/diff_bpm.json'

def main():
  with open(DATA_SET) as data_file:
    data = json.load(data_file)

  songs = []
  for song in data:
    mix_in = song['MixIn']
    mix_out = song['MixOut']
    file_name = song['File']
    bpm = song['BPM']
    split_song(mix_in, mix_out, bpm, file_name)

def split_song(mix_in, mix_out, bpm, file_name):
  file_path = './data/mp3/' + file_name
  audio, _ = librosa.load(file_path, sr=SR)
  _, beats = librosa.beat.beat_track(y=audio, sr=SR, bpm=bpm)

  body = librosa.frames_to_samples(beats[mix_in+MIX_LEN:mix_out])
  trans_in = librosa.frames_to_samples(beats[mix_in:mix_in+MIX_LEN])
  trans_out = librosa.frames_to_samples(beats[mix_out:mix_out+MIX_LEN])

  body_audio = audio[body[0]: body[-1]]
  in_audio = audio[trans_in[0]: trans_in[-1]]
  out_audio = audio[trans_out[0]: trans_out[-1]]

  file_name = file_name.split('.')[0]
  librosa.output.write_wav('./data/chopped/body/'+file_name+'.wav', body_audio, SR)
  librosa.output.write_wav('./data/chopped/trans_in/'+file_name+'.wav', in_audio, SR)
  librosa.output.write_wav('./data/chopped/trans_out/'+file_name+'.wav', out_audio, SR)

if __name__ == '__main__':
	main()
