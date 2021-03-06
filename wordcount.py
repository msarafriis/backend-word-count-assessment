#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import re

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.


def ver_check():
    if sys.version_info[0] < 3:
        raise Exception('Python 2 is unsupported. Python 3 is required.')


def word_finder(word_list):
    found_words = {}
    for word in word_list:
        try:
            found_words[word.lower()]
        except:
            found_words[word.lower()] = 0
        found_words[word.lower()] += 1
    return found_words


def print_words(filename):
    with open(filename, 'r') as text:
        words = re.sub("[^\w]", " ", text.read()).split()
        # use of regex inspired by https://stackoverflow.com/a/6181784
        found_words = word_finder(words)
        for word in found_words:
            print("{}: {}".format(word, found_words[word]))


def print_top(filename):
    with open(filename, 'r') as text:
        words = re.sub("[^\w]", " ", text.read()).split()
        # use of regex inspired by https://stackoverflow.com/a/6181784
        found_words = word_finder(words)
        top_words = [(word, count) for word, count in sorted(
            found_words.items(), key=lambda item: item[1])][::-1][:20]
        # above inspired by https://stackoverflow.com/a/613218
        print("Top 20 words in {}\n".format(filename))
        for pair in top_words:
            print("{}: {}".format(pair[0], pair[1]))

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def main():
    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    ver_check()
    main()
