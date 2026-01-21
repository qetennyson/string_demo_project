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


def generate_text(word_chains, start_word=None, length=10, favor_letter=None, user_frequency_weighting=False, verbose=True):

    def get_backup_word(word_chains):
        start_words_to_choose_from = list(itertools.chain.from_iterable(list(word_chains.values())))
        start_word = random.choice(start_words_to_choose_from)
        return start_word
    
    if start_word is None:
        start_word = get_backup_word(word_chains) 
    elif start_word.lower() not in word_chains:
        start_word = get_backup_word(word_chains) 

    new_text = [start_word]

    steps = []

    while len(new_text) < length:
        if start_word.lower() not in word_chains:
            break

        # Letter Favoring Algorithm
        candidates = word_chains[start_word.lower()]

        if favor_letter:
            filtered = [word for word in candidates if word.lower().startswith(favor_letter.lower())]

            if filtered:
                candidates = filtered
        

        if verbose:
            probabilities = get_next_word_probabilities(candidates)
            steps.append({
                'selected_word': start_word,
                'next_options': probabilities,
            })
        
        if user_frequency_weighting:
            unique_words = list(set(candidates))
            weights = [candidates.count(word) for word in unique_words]
            next_word = random.choices(unique_words, weights=weights, k=1)[0]
        else:
            next_word = random.choice(candidates)
        
        new_text.append(next_word)
        start_word = next_word

    final_text = ' '.join(new_text)

    if verbose:
        return {
            'text' : final_text,
            'steps': steps,
        }
    else:
        return final_text

def get_next_word_probabilities(candidates):
    """
    Returns a dictionary of {word : percentage} that reflects the 
    likelihood of a word being suggested for the next word.
    """
    word_counts = {}
    for word in candidates:
        word_counts[word] = word_counts.get(word, 0) + 1

    total = len(candidates)
    probabilities = {}
    for word, count in word_counts.items():
        probabilities[word] = (count / total) * 100

    return probabilities # {word: percent, word: percent}


    
