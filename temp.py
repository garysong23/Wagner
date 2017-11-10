from data_setup import load_songs
from pprint import pprint

from amen.utils import example_audio_file
from amen.audio import Audio
from amen.synthesize import synthesize

audio_file = './data/mp3/UptownFunk.mp3'
audio = Audio(audio_file)

beats = audio.timings['beats'][96:128]
pprint(audio.timings['beats'][96].time.total_seconds())

out = synthesize(beats)
out.output('temp.wav')
# print('outted')
