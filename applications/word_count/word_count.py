def word_count(s):
    # Your code here
    words = s.lower().split()
    cache = {}

    for word in words:
        cache[word] = words.count(word)
    return cache



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))