import json
from collections import Counter
from pprint import pprint

import matplotlib.pyplot as plt
import mglearn
import numpy as np
import pandas as pd
from sklearn.datasets import load_files
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.utils.tests.test_pprint import GridSearchCV

import utils.env_utils as u


def read_json(file_name):
    with open(u.get_path_to_the_data_dir(file_name)) as f:
        return (json.loads(row) for row in f.readlines())


def get_text(file_name):
    return (status['text'] for status in read_json(file_name) if status['metadata']['iso_language_code'] == 'en')


def movie_review_dataset(t):
    """
    The datataset is taken from here http://ai.stanford.edu/~amaas/data/sentiment/
    """
    review_trains = load_files(u.get_path_to_the_data_dir(f'aclImdb/{t}'))
    text, y = review_trains.data, review_trains.target
    text = [doc.replace(b'<br />', b'') for doc in text]
    return text, y


def get_model():
    text_train, y_train = movie_review_dataset(t='train')
    vect = CountVectorizer(min_df=10)
    vect.fit(text_train)

    X_train = vect.transform(text_train)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    text_test, y_test = movie_review_dataset(t='train')
    X_test = vect.transform(text_test)
    print(model.score(X_test, y_test))

    # estimate_model(model, vect)

    return model, vect


def estimate_model(text_train, y_train):
    # page 359 - 360
    pipe = make_pipeline(TfidfVectorizer(min_df=5, norm=None), LogisticRegression())
    param_grid = {'logisticregression__C': [0.001, 0.01, 0.1, 1, 10]}
    grid = GridSearchCV(pipe, param_grid, cv=5)
    grid.fit(text_train, y_train)

    vectorizer = grid.best_estimator_.named_steps[
        "tfidfvectorizer"]  # 􏰇􏰈􏰆􏰐􏰓􏰈􏰀􏰌􏰃􏰆􏰉 􏰐􏰓􏰃􏰄􏰀􏰗􏰕􏰁􏰛 􏰍􏰀􏰓􏰐􏰈 􏰘􏰀􏰍􏰍􏰋􏰚
    X_train = vectorizer.transform(text_train)

    max_value = X_train.max(axis=0).toarray().ravel()
    sorted_by_tfidf = max_value.argsort()
    feature_names = np.array(vectorizer.get_feature_names())
    print("Lowest values of􏰌􏰍􏰀􏰄􏰆􏰍􏰁􏰔􏰉􏰁 tfidf: {}".format(feature_names[sorted_by_tfidf[:20]]))
    print("Highest values of􏰌􏰍􏰀􏰄􏰆􏰍􏰁􏰔􏰉􏰁 tfidf: {}".format(feature_names[sorted_by_tfidf[-20:]]))

    mglearn.tools.visualize_coefficients(
        grid.best_estimator_.named_steps["logisticregression"].coef_, feature_names, n_top_features=40)


def twits_bag_of_words(file):
    vect = CountVectorizer(min_df=2)
    texts = list(get_text(file))
    vect.fit(texts)
    print(vect.vocabulary_)
    bag_of_words = vect.transform(texts)
    print(repr(bag_of_words))
    df = pd.DataFrame(bag_of_words.toarray(), columns=vect.get_feature_names())
    print(df[:5])
    print(len(texts[1]))


def classify_twits(file):
    texts = list(get_text(file))
    model, vect = get_model()
    bag_of_words = vect.transform(texts)
    prediction = model.predict(bag_of_words)
    pprint(list(zip(texts, prediction))[:20])
    c = Counter(prediction)
    print(c)


def direhly_lda_extrac_topic_names(text_train):
    """
    Несмотря на то что выделение тем может быть полезным, любые выводы, которые можно сделать,
    исходя из результатов модели неконтролируемого обучения, нужно принимать с определенной долей сомнения
    и мы рекомендуем проверять выводы, анализируя документы, присвоенные определенной теме.
    Кроме того, темы, полученные с помощью метода LDA.transform,
    можно иногда использовать в качестве входного признака для машинного обучения с учителем.
    """
    vect = CountVectorizer(max_features=10000, max_df=.15)
    X = vect.fit_transform(text_train)
    n_topics = 10
    lda = LatentDirichletAllocation(n_topics, learning_method="batch", max_iter=25, random_state=0)
    document_topics = lda.fit_transform(X)
    sorting = np.argsort(lda.components_, axis=1)[:, ::-1]
    feature_names = np.array(vect.get_feature_names())
    mglearn.tools.print_topics(
        topics=range(n_topics), feature_names=feature_names, sorting=sorting, topics_per_chunk=5, n_words=10)

    print_topic_documents(text_train, document_topics, n_topics)

    show_topic_names(document_topics, feature_names, sorting)


def print_topic_documents(text, document_topics, n_topics, printed_documents=5):
    a = 1
    for i in range(n_topics):
        print('*' * 100)
        print(f'topic {i}')
        topic = np.argsort(document_topics[:, i])[::-1]
        for j in topic[:printed_documents]:
            print(f'document {j} ', '-' * 50)
            print(text[j])


def show_topic_names(document_topics, feature_names, components):
    """
    show general weight of topic through all documents
    """
    most_common_topic_words = feature_names[components[:, :2]]
    topic_names = [f'{i:>2} ' + ' '.join(words) for i, words in enumerate(most_common_topic_words)]
    weights = np.sum(document_topics, axis=0)
    draw_bar_plot(topic_names, weights, columns=2)


def draw_bar_plot(topic_names, weights, columns=1):
    max_x_number = max(weights) * 1.3
    t = len(topic_names)
    _, ax = plt.subplots(1, 2, figsize=(t, t))
    number_of_elements_in_col = t // columns
    for col in range(columns):
        start = col * number_of_elements_in_col
        end = start + number_of_elements_in_col
        ax[col].barh(np.arange(number_of_elements_in_col), weights[start:end])
        ax[col].set_yticks(np.arange(number_of_elements_in_col))
        ax[col].set_yticklabels(topic_names[start:end], ha="left", va="top")
        ax[col].invert_yaxis()
        ax[col].set_xlim(0, max_x_number)
        yax = ax[col].get_yaxis()
        yax.set_tick_params(pad=130)
    plt.tight_layout()
    plt.show()


# twits_bag_of_words('evernote_20200620_195530.json')
# classify_twits('evernote_20200620_195530.json')
# twits_bag_of_words('evernote_20200620_195530.json')
direhly_lda_extrac_topic_names(list(get_text('sonya7siii_20200812_184311.json')))
