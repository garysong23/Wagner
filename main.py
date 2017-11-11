import json
from data_setup import load_songs

from objects.Mix import Mix
from objects.Mashability import Mashability

from pprint import pprint

def main():
	songs = load_songs()
	mashability = Mashability(songs)

	# mix = Mix(songs)
	# mix.write_mix()

if __name__ == '__main__':
	main()
