from itertools import islice

from gensim.models import word2vec
import pycountry


model = word2vec.Word2Vec.load('vectors')

for c in islice(pycountry.countries, 5, 10):
    print(c.name, model[c.name.replace(' ', '_')][:5])
