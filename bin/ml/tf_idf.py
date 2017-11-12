import copy
from collections import Counter

import numpy
import pandas
from gensim.utils import simple_preprocess
from sklearn.base import TransformerMixin


class TfIdf():
    # Based on partially on https://lizrush.gitbooks.io/algorithms-for-webdevs-ebook/content/chapters/tf-idf.html
    def __init__(self):
        self.vocab_counter = Counter()
        self.document_count = 0

    def fit(self, X, y=None):
        """

        :param X: Pandas dataframe, with columns: ['document', 'text']
        :param y: Unused, required by SKLearn API
        :return:
        """
        X = copy.deepcopy(X)

        X['token_set'] = X['text'].apply(lambda x: set(self.preprocess_text(x)))

        self.document_count = self.document_count + len(X.index)
        for token_set in X['token_set']:
            self.vocab_counter.update(token_set)
        return self

    def transform(self, X):
        """

        :param X: Pandas dataframe, with columns: ['document', 'token', 'tfidf_score']
        :return:
        """

        if len(X.index) >=1:
            X = copy.deepcopy(X)

            X['token_list'] = X['text'].apply(self.preprocess_text)

            tokens = self.explod_tokens(X)

            tokens['tfidf_score'] = tokens.apply(lambda observation: self.tfidf_score(observation, tokens), axis=1)

            return tokens
        else:
            return pandas.DataFrame(columns=['document', 'token', 'tfidf_score'])

    def fit_transform(self, X, y=None):
        X = copy.deepcopy(X)
        self.fit(X)
        return self.transform(X)

    def preprocess_text(self, text):
        tokens = simple_preprocess(text, min_len=1)
        return tokens

    def explod_tokens(self, X):

        # Reference variables
        result_agg = list()

        for index, document_observation in X.iterrows():
            document = document_observation['document']
            for token in document_observation['token_list']:
                local_dict = dict()
                local_dict['document'] = document
                local_dict['token'] = token
                result_agg.append(local_dict)

        tokens = pandas.DataFrame(result_agg)

        return tokens

    def tfidf_score(self, observation, tokens):
        """
        This uses document frequency smoothing, which includes one 'meta document', which contains all tokens. This also
        has the added value of avoiding divide by zero errors.
        :param observation:
        :param tokens:
        :return:
        """
        token = observation['token']
        document = observation['document']

        # Number of times token occurred in document, divided by number of token occurrences in document
        tf = len(tokens[(tokens['token'] == token) & (tokens['document'] == document)].index) / float(len(tokens[tokens['document'] == document].index))

        # Number of documents with term. Default to 1, to represent meta document with all words
        df_numerator = max(self.vocab_counter.get(token), 1)

        # Number of documents seen. Add one, to represent meta document with all words
        df_denom = float(self.document_count + 1)
        df = df_numerator / df_denom

        log_idf = numpy.log(1/df)

        tifidf_score = tf * log_idf
        return tifidf_score
