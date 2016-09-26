import re


with open('questions-words.txt', encoding='utf-8') as r, \
        open('questions-family.txt', 'w', encoding='utf-8') as w:
    w.write(re.search('(: family.*?):', r.read(), re.DOTALL).group(1))
