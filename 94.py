from gensim.models import word2vec


model = word2vec.Word2Vec.load('vectors')

with open('combined.csv', encoding='utf-8') as r, \
        open('wordsim-353-w2v.txt', 'w', encoding='utf-8') as w:
    next(r)
    for line in r:
        w1, w2, _ = line.split(',')
        sim = model.similarity(w1, w2)
        w.write(line.strip() + ',{}\n'.format(sim))
