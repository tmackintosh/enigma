def n_gram_fitness(code, file):
    score = 0

    with open(file) as fp:
        for i, line in enumerate(fp):
            sections = line.split(",")
            
            if sections[0] in code:
                score += float(sections[1])

    return score