import random

# Read in all the words in one go
with open('applications/markov/input.txt') as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
split = words.split()
cache = {}

for i in range(len(split) - 1):
    word = split[i]
    next_word = split[i+1]

    if word not in cache:
        cache[word] = [next_word]
    cache[word].append(next_word)

# TODO: construct 5 random sentences
# Your code here
start = []

for key in cache.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start.append(key)

word = random.choice(start)

stop = False
stop_chars = '?.!'

while not stop:
    print(word)
    if word[-1] in stop_chars or len(word) > 1 and word[-2] in stop_chars:
        stop = True
        
    following_words = cache[word]
    word = random.choice(following_words)
    

