import random
from collections import defaultdict

def build_markov_chains(quotes):
    word_chains = defaultdict(list)

    for quote in quotes:
        split_quote = quote.split()
        for index in range(len(split_quote) - 1):
            word_chains[split_quote[index]].append(word_chains[index+1])
        
    return word_chains
