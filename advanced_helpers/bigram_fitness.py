file = open("data/bigrams.txt")

def bigram_fitness(code):
    score = 0

    with open("data/bigrams.txt") as fp:
        for i, line in enumerate(fp):
            sections = line.split(",")
            
            if sections[0] in code:
                score += float(sections[1])

    return score