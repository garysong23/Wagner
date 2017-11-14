from pydub import AudioSegment

# Saves a transition audio file using linear crossfade
def crossfade_files(trans_out_path, trans_in_path):
  audio_out = AudioSegment.from_file(trans_out_path)
  audio_in = AudioSegment.from_file(trans_in_path)

  dur = int(min(audio_out.duration_seconds, audio_in.duration_seconds)*1000)
  mix = audio_out.append(audio_in, crossfade=dur)

  path_name = './output/temp/mix.wav'
  mix.export(path_name, format='wav')
  return path_name
