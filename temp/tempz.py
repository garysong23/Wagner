from pydub import AudioSegment
out_audio = AudioSegment.from_file('./output/temp/out.wav')
in_audio = AudioSegment.from_file('./output/temp/in.wav')

mix = out_audio.append(in_audio, crossfade=14000)
mix.export('./output/temp/mix.wav', format='mp3')
