from gensim.models import word2vec
from matplotlib import pyplot as plt
import pycountry
from sklearn.manifold import TSNE


model = word2vec.Word2Vec.load('vectors')

n = 100
names = [name for name in 
    [c.name.replace(' ', '_') for c in pycountry.countries] if name in model][:n]
X = [model[name] for name in names]
tsne = TSNE(n_components=2, random_state=0)
Y = tsne.fit_transform(X)

_, ax = plt.subplots()
ax.scatter(Y[:, 0], Y[:, 1])
for i, name in enumerate(names):
    ax.annotate(name, (Y[i, 0],Y[i, 1]))
plt.show()
