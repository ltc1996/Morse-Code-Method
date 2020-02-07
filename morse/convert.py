from engine import di, da, morse2alpha, alpha2morse

import re


def morse_alpha(string_from):
    res = ''
    regex = '([{}|{}]+|/+)'.format(di, da)
    p = re.findall(regex, string_from)
    # print(p)
    down = False
    for tmp in p:
        if tmp == '/':
            res += ' '
            down = False
            continue
        try:
            char = morse2alpha.search(tmp)
            if char:
                if down:
                    char = char.lower()
                res += char
                down = True
            else:
                res += '?'
        except:
            res += '?'

    return res


def alpha_morse(string_from):
    res = ''
    p = re.findall(r'\S+|\s', string_from)
    # print(p)
    for word in p:
        # print(word)
        if word[0] == ' ':
            res += '/'
            continue
        for char in word:
            char_u = char.upper()
            if char_u in alpha2morse:
                try:
                    res += alpha2morse[char_u]
                except KeyError:
                    res += '?'
            else:
                res += '?'
            res += ' '
    return res

