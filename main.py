import json
from objects.Mix import Mix
from objects.Song import Song
from pprint import pprint

name = 'seq'
DATA_SET = './data/json/' + name + '.json'

def load_songs():
	with open(DATA_SET) as data_file:
		data = json.load(data_file)

	songs = []
	for song in data:
		new_song = Song(
			fname=song['File'],
			mix_in=song['MixIn'],
			mix_out=song['MixOut'],
			bpm=song['BPM'],
		)
		songs.append(new_song)
	return songs

def main():
	songs = load_songs()
	mix = Mix(songs)
	# sf.write('test.wav', audio_segment, 44100)
	# playlist = Playlist(songs)

	# mix.write_mix()

if __name__ == '__main__':
	main()
