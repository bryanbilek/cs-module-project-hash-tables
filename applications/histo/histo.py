# Your code here
with open('applications/histo/robin.txt') as f:
    words = f.read()

words = words.split(' ')

def histo(robin):
    cache = {}
    for i in robin:
        cache[i] = cache.get(i, 0) + 1
    return cache

totals = histo(words)
print(totals)
