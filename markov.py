import random
import itertools
from collections import defaultdict


def build_markov_chains(quotes):
    word_chains = defaultdict(list)

    for quote in quotes:
        split_quote = quote.split()
        for index in range(len(split_quote) - 1):
            word_chains[split_quote[index]].append(split_quote[index+1])
        
    return word_chains


def generate_text(word_chains, start_word=None, length=10):

    def get_backup_word(word_chains):
        start_words_to_choose_from = itertools.chain.from_iterable(list(word_chains.values()))
        start_word = random.choice(start_words_to_choose_from)
        return start_word
    
    if not start_word or start_word not in word_chains:
        start_word = get_backup_word(word_chains)    

    new_text = [start_word]
    while len(new_text) < length:
        if start_word not in word_chains:
            break
        
        next_word = random.choice(word_chains.get(start_word))
        new_text.append(next_word)
        start_word = next_word

    return ' '.join(new_text)
    

    
