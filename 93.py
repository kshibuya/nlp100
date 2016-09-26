from gensim.models import word2vec


model = word2vec.Word2Vec.load('vectors')

accuracies = model.accuracy('questions-family.txt')
for acc in accuracies:
    if acc['section'] == 'total':
        cor = len(acc['correct'])
        incor = len(acc['incorrect'])
        print(cor / (cor + incor))
