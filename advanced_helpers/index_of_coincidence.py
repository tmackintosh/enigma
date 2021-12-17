import collections

from helpers.type_assertion import type_assertion

def index_of_coincidence(code):
    """
    Gets the index of coincidence for a string.

    @param code: the string to assess
    @returns the index of coincidence
    """
    # Method defense
    type_assertion(code, str)
    
    freqs = collections.Counter(code)

    freq_sum = 0

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        freq_sum += freqs[letter] * (freqs[letter] + 1)

    index_of_coincidence = freq_sum / (len(code) * len(code) - 1)
    return index_of_coincidence