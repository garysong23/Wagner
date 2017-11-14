'''
Generate sequence of songs based on the mash_index for each transition.
Minimizing for the lowest total mash value.

Current solution is implemented using brute force. O(n^n).
Generating all possible sequences.
Better solution should use techniques from the travelling salesman problem.
'''

from pprint import pprint
import itertools

def sequence_for_mash_index(songs, mash_index):
  seq_vals = _all_sequence_mash_index(songs, mash_index)
  print('All sequences:')
  pprint(seq_vals)
  sorted_vals = [(k, seq_vals[k]) for k in sorted(seq_vals, key=seq_vals.get)]
  return sorted_vals[0]

def _all_sequence_mash_index(songs, mash_index):
  num_of_songs = len(songs)
  all_perm = itertools.permutations(songs)

  all_seq_mash_index = {}
  for perm in all_perm:
    seq_index = 0
    for i in range(num_of_songs-1):
      s1, s2 = perm[i], perm[i+1]
      index = mash_index[(s1, s2)]
      seq_index += index
    all_seq_mash_index[perm] = seq_index

  return all_seq_mash_index
