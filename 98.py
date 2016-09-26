from gensim.models import word2vec
from matplotlib import pyplot as plt
import pycountry
from scipy.cluster.hierarchy import ward, dendrogram


model = word2vec.Word2Vec.load('vectors')

n = 15
names = [name for name in 
    [c.name.replace(' ', '_') for c in pycountry.countries] if name in model][:n]
X = [model[name] for name in names]

dendrogram(ward(X), labels=names, leaf_rotation=45)
plt.show()
