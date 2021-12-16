import collections

def index_of_coincidence(code):
    freqs = collections.Counter(code)

    freq_sum = 0

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        freq_sum += freqs[letter] * (freqs[letter] + 1)

    index_of_coincidence = freq_sum / (len(code) * len(code) - 1)
    return index_of_coincidence