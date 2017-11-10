from data_setup import load_songs
from pprint import pprint

from amen.utils import example_audio_file
from amen.audio import Audio
from amen.synthesize import synthesize

audio_file = './data/mp3/Jealous.mp3'
audio = Audio(audio_file)

print('reversing')
# beats = audio.timings['beats'][64:96]
pprint(audio.timings['beats'][128].duration)
pprint(audio.timings['beats'][128].time.total_seconds())
pprint(audio.timings['beats'][128].time.microseconds)
pprint(beats)

# out = synthesize(beats)
# out.output('reversed2.wav')
# print('outted')
