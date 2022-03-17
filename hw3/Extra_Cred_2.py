from sklearn.datasets import fetch_20newsgroups
from pprint import pprint
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

# (1) Load data
newsgroups_train = fetch_20newsgroups(subset='train')['data']
pprint(list(newsgroups_train.target_names))

tokens = to_list(tokenize(newsgroups_train))

# (2) Clean the text
# (a) To lower
lower = to_list(to_lower(tokens))
# (b) No punctuation / number
no_punct = to_list(remove_punct(lower))
no_digits = to_list(remove_digits(no_punct))

# (c)	Words which occur in less than 5 documents are removed.
no_sparse = CountVectorizer(newsgroups_train, min_df=0.2)

# (d) No stopwords
no_stopwords = to_list(remove_stopwords(no_sparse))

# (e) Stemming words (root words)
lem_docs = to_list(lemmatize(no_stopwords))

# (3) Report the number of words you are left with in total (over all documents
count_vect = CountVectorizer()
word_counts = count_vect.fit_transform(lem_docs)
word_counts.shape

# (4) Calculate TF-IDF vectors for each document
tf_transformer = TfidfTransformer(use_idf=False).fit(word_counts)
x_train_tf = tf_transformer.transform(word_counts)
x_train_tf.shape

tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(word_counts)
x_train_tfidf.shape

# (5) For each class, find and report the top 10 words with highest TF-IDF values averaged over all documents belonging to that class.

tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(newsgroups_train).toarray()
vocab = tfidf.vocabulary_
reverse_vocab = {v:k for k,v in vocab.items()}

feature_names = tfidf.get_feature_names()
df_tfidf = pd.DataFrame(X_tfidf, columns = feature_names)

idx = X_tfidf.argsort(axis=1)

tfidf_max10 = idx[:,-10:]

df_tfidf['top10'] = [[reverse_vocab.get(item) for item in row] for row in tfidf_max10 ]

#df_tfidf['top10']

global_top10_idx = X_tfidf.max(axis=0).argsort()[-10:]
np.asarray(feature_names)[global_top10_idx]

# Top 10 words
# 'sy', 'carlos', 'duran', 'zeos', 'clubbing', 'damico', 'toner', 'osburn', 'echo', 'lakshman'



