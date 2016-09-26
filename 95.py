from gensim.models import word2vec
from scipy.stats import stats, spearmanr


model = word2vec.Word2Vec.load('vectors')

with open('wordsim-353-w2v.txt', encoding='utf-8') as f:
    human_sim, nlp_sim = list(zip(
        *[map(float, line.strip().split(',')[2:4]) for line in f]))

print(spearmanr(stats.rankdata(human_sim), stats.rankdata(nlp_sim)))
