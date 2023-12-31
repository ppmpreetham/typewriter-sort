import string
import random
import sys

#blind method
def generate(length):
    characters = string.ascii_lowercase+" "
    return "".join([random.choice(characters) for i in range(length)])

def score(test_string,target_string):
    test_list = zip([i for i in test_string],[i for i in target_string])
    return (sum([1 for test_letter, target_letter in test_list if test_letter == target_letter])/len(target_string))*100

def generate_and_score(phrase):
    counter = 0
    best_score = 0
    best_attempt = None
    while best_score < 100: 
        this_attempt = generate(len(phrase))
        this_score = score(this_attempt,phrase)
        counter += 1
        if this_score > best_score:
            best_score = this_score
            best_attempt = this_attempt
        if counter % 1000 == 0:
            print("Tries: {}; Best Guess: {} with a score of {}".format(counter, best_attempt, best_score))
    print("Success in {} guesses!".format(counter))

#hill-climbing method
def improved_generate(best_attempt,phrase):
    characters = string.ascii_lowercase+" "
    return "".join([random.choice(characters) if a != p else a for a,p in zip([i for i in best_attempt],[i for i in phrase])])

def generate_and_score_improved(phrase):
    counter = 0
    best_score = 0
    best_attempt = None
    while best_score < 100:
        this_attempt = improved_generate(best_attempt,phrase) if best_attempt else generate(len(phrase))
        this_score = score(this_attempt,phrase)
        counter += 1
        if this_score > best_score:
            best_score = this_score
            best_attempt = this_attempt
        if counter % 1000 == 0:
            print("Tries: {}; Best Guess: {} with a score of {}".format(counter, best_attempt, best_score))
    print("Success in {} guesses!".format(counter))