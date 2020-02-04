import json
import os
import inspect
import re

from support.Trie import Trie

di = '.'
da = '-'

alpha2morse = {
    'A': di + da          ,
    'B': da + di + di + di,
    'C': da + di + da + di,
    'D': da + di + di     ,
    'E': di               ,
    'F': di + di + da + di,
    'G': da + da + di     ,
    'H': di + di + di + di,
    'I': di + di          ,
    'J': di + da + da + da,
    'K': da + di + da     ,
    'L': di + da + di + di,             # .-..
    'M': da + da          ,
    'N': da + di          ,
    'O': da + da + da     ,
    'P': di + da + da + di,
    'Q': da + da + di + da,
    'R': di + da + di     ,             # .-.
    'S': di + di + di     ,
    'T': da               ,
    'U': di + di + da     ,
    'V': di + di + di + da,
    'W': di + da + da     ,
    'X': da + di + di + da,
    'Y': da + di + da + da,
    'Z': da + da + di + di,
}


# generatr trie from the letter -> morse list
def genTrie(dict_to_trie) -> Trie:
    trie = Trie()
    for k, v in dict_to_trie.items():
        trie.insert(v, k)
    # print('gen trie successfully')
    return trie


# distribute file.type to var
def setvariable(var, file_type) -> list:
        # print(os.getcwd())
    name = os.path.join('support', var + '.' + file_type)
    filename = os.path.join(os.getcwd(), name)
    print(filename)
    # filename = os.path.join(os.path.dirname(__name__) + name)
    if not os.path.exists(filename):
        print(filename, 'not exists')
        raise FileNotFoundError
    with open(filename, 'r+') as f:
        var = json.load(f)
        print(filename, 'has been distributed successfully')
    return var


# get the str(var) of variable called var
def varname() -> str:
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            return m.group(1)


# for .md table
def print_table():
    for k, v in alpha2morse.items():
        print('|  ' + '`' + k + '`  | `' + v + '`' + ' ' * (5 - len(v)) + '|')
# alpha2morse = 'alpha2morse'


# alpha2morse = setvariable(alpha2morse, json)
morse2alpha = genTrie(alpha2morse)

if __name__ == "__main__":
    # print_table()
    print(morse2alpha.show())
