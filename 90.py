from gensim.models import word2vec


model = word2vec.Word2Vec.load('vectors')

# 86
print(model['United_States'][:5])

# 87
print(model.similarity('United_States', 'U.S'))

# 88
for r in model.most_similar(positive=['England'], topn=10):
    print(r)

# 89
for r in model.most_similar(
        positive=['Spain', 'Athens'],
        negative=['Madrid'],
        topn=10):
    print(r)
