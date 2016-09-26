from gensim.models import word2vec


sentences = word2vec.LineSentence('corpus.txt', max_sentence_length=3000000)
model = word2vec.Word2Vec(sentences, size=100)

model.save('vectors')
