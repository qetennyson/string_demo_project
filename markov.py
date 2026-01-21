import random
import itertools
from quotes import QUOTES

from collections import defaultdict

## Generate a random set of starter words the user can try.
def get_random_starter_words(quotes=QUOTES):
    quotes = random.sample(quotes, k=15)
    words = [quote.split()[0] for quote in quotes]
    return list(set(words[:10]))

def build_markov_chains(quotes=QUOTES):
    word_chains = defaultdict(list)

    for quote in quotes:
        split_quote = quote.split()
        for index in range(len(split_quote) - 1):
            word = split_quote[index].strip('.!?').lower()
            next_word = split_quote[index+1].strip('.!?').lower()
            word_chains[word].append(next_word)
        
    return word_chains


def generate_text(word_chains, start_word=None, length=10):

    def get_backup_word(word_chains):
        start_words_to_choose_from = list(itertools.chain.from_iterable(list(word_chains.values())))
        start_word = random.choice(start_words_to_choose_from)
        return start_word
    
    if start_word is None:
        start_word = get_backup_word(word_chains) 
    elif start_word.lower() not in word_chains:
        start_word = get_backup_word(word_chains) 

    new_text = [start_word]
    while len(new_text) < length:
        if start_word.lower() not in word_chains:
            break

        next_word = random.choice(word_chains.get(start_word.lower()))
        new_text.append(next_word)
        start_word = next_word

    return ' '.join(new_text)
    

    
