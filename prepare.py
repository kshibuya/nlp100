import pycountry


# 80
with open('enwiki-20150112-400-r10-105752.txt', encoding='utf-8') as r, \
        open('tokens.txt', 'w', encoding='utf-8') as w:
    for line in r:
        w.write(' '.join(
            [token.strip('.,!?;:()[]\'\"') for token in line.split()]
        ) + '\n')

# 81
with open('tokens.txt', encoding='utf-8') as r, \
        open('corpus.txt', 'w', encoding='utf-8') as w:
    text = r.read()
    for country in pycountry.countries:
        text = text.replace(country.name, country.name.replace(' ', '_'))
    w.write(text)
