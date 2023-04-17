# https://dmoj.ca/problem/dmopc15c7p2

def count_words(word):
    word_list = word.split(sep=" ", maxsplit=-1)
    return len(word_list)

word = input()
print(count_words(word))    