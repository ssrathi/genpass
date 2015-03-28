#!/usr/bin/env python
"""
Generate secure, random and memorable passwords of a specified length (default = 24).

Includes various options to generate different combinations. Use "-h" to view all of them.
"""

from __future__ import print_function

__author__ = "Shyamsunder Rathi"
__year__ = "2015"

import argparse
import random
import os
import string
import sys

DEFAULT_LENGTH = 16
DEFAULT_COUNT = 30
MAX_LENGTH = 64
MAX_COUNT = 1000
DEFAULT_WORD_FILE = 'words-en.txt'

parser = argparse.ArgumentParser(description='Generate Secure Passwords.')
parser.add_argument('-m', '--memorable', dest='memorable',
                    help='memorable passphrase using common words (http://xkcd.com/936)',
                    action='store_true')
parser.add_argument('-A', '--no-capitalize', dest='cap',
                    help='do not include CAPITAL letters', action='store_false')
parser.add_argument('-N', '--no-numerals', dest='num',
                    help='do not include NUMBERS', action='store_false')
parser.add_argument('-S', '--no-symbols', dest='sym',
                    help='do not include SYMBOLS', action='store_false')
parser.add_argument('-C', '--no-columns', dest='column',
                    help='print one password per line', action='store_false')
parser.add_argument('-l', '--length', type=int, metavar='PW_LENGTH',
                    default=DEFAULT_LENGTH, dest='length',
                    help='length of each password (1-%d, default=%d)' % (MAX_LENGTH, DEFAULT_LENGTH))
parser.add_argument('-n', '--num-passwords', type=int, metavar='NUM_PW',
                    default=DEFAULT_COUNT, dest='count',
                    help='total number of passwords (1-%d, default=%d)' % (MAX_COUNT, DEFAULT_COUNT))


def gen_passwd(length=DEFAULT_LENGTH, capitals=True, numerals=True, symbols=True):
    """
    Generate a random password of specified length

    :param length: Length of generated password
    :param capitals: Include CAPITAL letters in the password
    :param numerals: Include NUMERALS in the password
    :param symbols: Include SYMBOLS in the password
    """

    chars = string.lowercase
    if capitals:
        chars += string.uppercase
    if numerals:
        chars += string.digits
    if symbols:
        chars += "@#$%^&?*():;-="

    password = []
    for i in xrange(length):
        index = random.SystemRandom().randrange(len(chars))
        password.append(chars[index])
    return "".join(password)


def __get_words():
    words = []
    try:
        with open(DEFAULT_WORD_FILE, 'rb') as fd:
            words = [line.strip() for line in fd.readlines()]
    except (IOError, OSError):
        parser.error('%s file is not found. Abort!' % DEFAULT_WORD_FILE)
    return words


def __print_columns(passwords, is_column=1):
    # Print in columns
    spaces = 4  # Space between two passwords
    max_length = len(max(passwords, key=len))  # Maximum length of a password
    print_per_line = (100 / (max_length + spaces)) if is_column else 1

    printed = 0
    for pw in passwords:
        print(pw, end='')
        printed += 1
        if printed < print_per_line:
            print(' ' * (spaces + (max_length - len(pw))), end='')
        else:
            print('')  # newline
            printed = 0

    if printed != 0:
        print('')  # Put a newline at the end


def gen_passphrase(words, num_words=5):
    """
    Generate a memorable passphrase using common words

    :param words: list of words to choose from
    :param num_words: number of words in each passwords (joined by '-')
    """

    passphrase = []
    for i in xrange(num_words):
        index = random.SystemRandom().randrange(len(words))
        passphrase.append(words[index])
    return "-".join(passphrase)


def main():
    args = parser.parse_args()

    if not 1 <= args.length <= MAX_LENGTH:
        parser.error('Password length must be between 1 to %d' % MAX_LENGTH)
    if not 1 <= args.count <= MAX_COUNT:
        parser.error('Number of passwords must be between 1 to %d' % MAX_COUNT)

    if args.memorable:
        words = __get_words()
        passwords = [gen_passphrase(words) for i in xrange(args.count)]
    else:
        passwords = [gen_passwd(args.length, args.cap, args.num, args.sym)
                     for i in xrange(args.count)]

    __print_columns(passwords, args.column)
    return 0


if __name__ == "__main__":
    sys.exit(main())
