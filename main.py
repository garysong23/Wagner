import json
from data_setup import load_songs
from mashability import mash_pairs
from mix.generate import mix_songs

from pprint import pprint

def main():
	songs = load_songs()
	mix_songs(songs)
	# pair_mashability = mash_pairs(songs)

if __name__ == '__main__':
	main()
