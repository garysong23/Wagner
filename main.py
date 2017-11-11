import json
from data_setup import load_songs
from objects.Mix import Mix

from pprint import pprint

def main():
	songs = load_songs()
	mix = Mix(songs)
	mix.write_mix()
	# pair_mashability = mash_pairs(songs)

if __name__ == '__main__':
	main()
