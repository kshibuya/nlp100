from gensim.models import word2vec
import pycountry
from sklearn.cluster import k_means


model = word2vec.Word2Vec.load('vectors')

X = [model[name] for name in
    [c.name.replace(' ', '_') for c in pycountry.countries] if name in model]
cluster = k_means(X, 5)
