from gensim.models import word2vec


model = word2vec.Word2Vec.load('vectors')

with open('questions-family.txt', encoding='utf-8') as r, \
        open('analogy-family-w2v.txt', 'w', encoding='utf-8') as w:
    next(r)
    for line in r:
        words = line.split()
        analogs = model.most_similar(
            positive=[words[1], words[2]],
            negative=[words[0]],
            topn=1)
        w.write(line.strip() + ' {} {}\n'.format(*analogs[0]))
