from helpers.type_assertion import type_assertion


def n_gram_fitness(code, file):
    """
    Opens the n-gram file and counts every iteration of any n-gram
    in a given string to give the fitness value.

    @param code: the string to assess
    @returns the fitness score
    """
    # Method defense
    type_assertion(code, str)
    type_assertion(file, str)

    score = 0

    with open(file) as fp:
        # We need to iterate through the data one line at a time
        for i, line in enumerate(fp):

            # The niche format of the data means each line is separated from its score by ,
            sections = line.split(",")
            
            if sections[0] in code:
                score += float(sections[1])

    return score