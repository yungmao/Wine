import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
import eli5
from scipy.sparse import hstack
import numpy as np
from AnalizaSentymentow.dataService import dataframe


df = dataframe()
category = []
for point in df['points']:
    if point > 90 : category.append(2)
    if point >= 85 and point <= 90: category.append(1)
    if point < 85: category.append(0)
df['category'] = pd.Series(category)

def SGD():
    train_text, test_text, ytrain, ytest = train_test_split(
        df['description'], df['category'], random_state=42)

    word_vectorizer = TfidfVectorizer(
        sublinear_tf=True,
        strip_accents='unicode',
        analyzer='word',
        token_pattern=r'\w{1,}',
        ngram_range=(1, 8))
    word_vectorizer.fit(train_text)

    char_vectorizer = TfidfVectorizer(
        sublinear_tf=True,
        strip_accents='unicode',
        analyzer='char',
        ngram_range=(1, 5))
    char_vectorizer.fit(train_text)

    sgd_cls = SGDClassifier(max_iter=2)
    sgd_cls.fit(word_vectorizer.transform(train_text), ytrain)

    print(eli5.format_as_text(eli5.explain_weights(sgd_cls, vec=word_vectorizer)))

    print(eli5.format_as_text(eli5.explain_prediction(
        sgd_cls,
        df['description'][df['points'] <= 81].values[0],
        vec=word_vectorizer)))

    X = hstack([word_vectorizer.transform(train_text), char_vectorizer.transform(train_text)])

    sgd_cls = SGDClassifier(max_iter=2)
    sgd_cls.fit(X, ytrain)
    predict = sgd_cls.predict(
        hstack([word_vectorizer.transform(test_text), char_vectorizer.transform(test_text)]))
    acc = np.mean(ytest == np.around(predict))
    print('Dokladnosc: {0:.3}'.format(acc))

SGD()