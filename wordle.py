# create a wordle game solver using PY sets and list comprehensions

import string
from random import choices
from pathlib import Path

# set some constants
PATH_TO_FULL_DICT = '/usr/share/dict/web2'
ALLOWED_CHARS = set(string.ascii_letters.lower())
ALLOWED_ATTEMPTS = 6
WORD_LENGTH = 5

# print(len(ALLOWED_CHARS))  # 52 (upper and lower case a-z)

# generate a set of words that match the wordle rules
WORDS = {
    word.lower()
    for word in Path(PATH_TO_FULL_DICT).read_text().splitlines()
    if len(word) == WORD_LENGTH and set(word) < ALLOWED_CHARS
}

# print(len(WORDS))  # 8497
print(type(WORDS))  # a set
# 10 random words
random_words = choices(list(WORDS), k=3)
for word in random_words:
    print(word)
