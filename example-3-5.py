# -*- coding:utf-8 -*-

"""Build an index mapping word -> list of occurrences."""

import re
import time
from collections import defaultdict

python_zen = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''


def count_occurrences_v0(content):
    index = dict()
    word_re = re.compile('\w+')
    content_list = content.split('\n')

    for line_no, line in enumerate(content_list, 1):
        for match in word_re.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

    for word in sorted(index, key=str.upper):
        print(word, index[word])


def count_occurrences_v1(content):
    index = dict()
    word_re = re.compile('\w+')
    content_list = content.split('\n')

    for line_no, line in enumerate(content_list, 1):
        for match in word_re.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

    for word in sorted(index, key=str.upper):
        print(word, index[word])


def count_occurrences_v2(content):
    index = defaultdict(list)
    word_re = re.compile('\w+')
    content_list = content.split('\n')

    for line_no, line in enumerate(content_list, 1):
        for match in word_re.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)

    for word in sorted(index, key=str.upper):
        print(word, index[word])


if __name__ == '__main__':
    st = time.time()
    count_occurrences_v0(python_zen)
    print('run count_occurrences_v0 cost {}s.'.format(time.time() - st))
    st = time.time()
    count_occurrences_v1(python_zen)
    print('run count_occurrences_v1 cost {}s.'.format(time.time() - st))
    st = time.time()
    count_occurrences_v2(python_zen)
    print('run count_occurrences_v2 cost {}s.'.format(time.time() - st))
