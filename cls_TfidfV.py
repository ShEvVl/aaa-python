import math


class CountVectorizer:
    """Convert a collection of text list to a matrix of token counts.

    Methods
    -------
    fit_transform : (raw_documents: list[str]) -> list[list[int]]
        Learn the vocabulary dictionary and return document-term matrix.

    get_feature_names : (None) -> list[str]
        Get output feature names for transformation.
    """

    def __init__(self) -> None:
        self.raw_documents: list[str] | None = None
        self.feature_names: list = []
        self.doc_term_matrix: list = []
        self.fmt_pattern = lambda x: x.lower().split(" ")

    def fit_transform(self, raw_documents: list[str]) -> list[list[int]]:
        """Learn the vocabulary dictionary and return document-term matrix.

        Parameters
        ----------
        raw_documents : (list[str])
            An iterable which generates str objects.

        Returns
        -------
        self.doc_term_matrix : (list[list[int]])
            Document-term matrix.
        """
        if isinstance(raw_documents, str):
            raise ValueError(
                "Iterable documents expected, string object received."
            )

        self.raw_documents = raw_documents

        feature_names = self.feature_names
        doc_term_matrix = self.doc_term_matrix
        fmt_pattern = self.fmt_pattern

        for el in raw_documents:
            feature_names.extend(fmt_pattern(el))
            seen: set = set()
            seen_add = seen.add
            feature_names = [
                x for x in feature_names if not (x in seen or seen_add(x))
            ]
            self.feature_names = feature_names

        for el in raw_documents:
            names = dict().fromkeys(feature_names, 0)
            raw_str = fmt_pattern(el)
            for val in raw_str:
                names[val] = 1 + names.get(val, 0)
            doc_term_matrix.append(list(names.values()))

        return doc_term_matrix

    def get_feature_names(self) -> list[str]:
        """Get output feature names for transformation.

        Returns
        -------
        self.feature_names : (list[str])
            Transformed feature names.
        """
        return self.feature_names


class TfidfTransformer:
    """Convert a matrix of token counts to TF-IDF values.

    Methods
    -------
    tf_transform (staticmetod): (count: list[list[int]]) -> list[list[float]]
        Compute Term Frequency (TF) for a given count matrix.

    idf_transform (staticmetod): (count: list[list[int]]) -> list[float]
        Compute Inverse Document Frequency (IDF) for a given count matrix.

    fit_transform : (count: list[list[int]]) -> list[list[float]]
        Fit and transform a count matrix to TF-IDF values.
    """

    @staticmethod
    def tf_transform(count: list[list[int]]) -> list[list[float]]:
        """
        Compute Term Frequency (TF) for a given count matrix.
        Parameters
        ----------
        count : list[list[int]]
            A list of lists containing term counts.
        Returns
        -------
        tf_count : list[list[float]]
            A list of lists containing TF values (rounded to 3 decimal places).
        """
        tf_count = [
            [round(item / sum(doc), 3) for item in doc] for doc in count
        ]
        return tf_count

    @staticmethod
    def idf_transform(matrix: list[list[int]]) -> list[float]:
        """
        Compute Inverse Document Frequency (IDF) for a given count matrix.

        Parameters
        ----------
        matrix : list[list[int]]
            A list of lists containing term counts.
        Returns
        -------
        result : list[list[float]]
            A list of IDF values (rounded to 3 decimal places).
        """
        result = []
        total = len(matrix)
        words_count = len(matrix[0])
        for word_num in range(words_count):
            count = 0
            for doc in matrix:
                if doc[word_num] > 0:
                    count += 1
            result.append(round(math.log((total + 1) / (count + 1)), 3) + 1)
        return result

    def fit_transform(self, count: list[list[int]]) -> list[list[float]]:
        """
        Fit and transform a count matrix to TF-IDF values.

        Parameters
        ----------
        matrix : list[list[int]]
            A list of lists containing term counts.
        Returns
        -------
        list[list[float]]
            A list of lists containing TF-IDF values
            (rounded to 3 decimal places).
        """
        tf_corp = self.tf_transform(count)
        idf_corp = self.idf_transform(count)
        return [
            [round(tf * idf, 3) for tf, idf in zip(tf_line, idf_corp)]
            for tf_line in tf_corp
        ]


class TfidfVectorizer(CountVectorizer):
    """
    Convert a collection of text list to TF-IDF values.

    Methods
    -------

    fit_transform : (corpus: list[str]) -> list[list[float]]
        Learn the vocabulary dictionary and return document-term matrix.
        Fit and transform a document-term matrix to TF-IDF values.
    """

    def __init__(self) -> None:
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, corpus: list[str]) -> list[list[float]]:
        """
        Fit and transform a corpus into TF-IDF values.

        Parameters
        ----------
        corpus : list[str]
            A list of strings representing documents.

        Returns
        -------
        list[list[float]]
            A list of lists containing TF-IDF values
            (rounded to 3 decimal places).
        """
        count_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix)


if __name__ == "__main__":
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    ]
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    transformer = TfidfVectorizer()
    tfidf_matrix = transformer.fit_transform(corpus)
    print(tfidf_matrix)
    # [[0.201, 0.201, 0.286, 0.201, 0.201, 0.201,
    #   0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    # [0.0, 0.0, 0.143, 0.0, 0.0, 0.0,
    #   0.201, 0.201, 0.201, 0.201, 0.201, 0.201]]

    tfidf_names = transformer.get_feature_names()
    print(tfidf_names)
    # ['crock', 'pot', 'pasta', 'never', 'boil', 'again',
    # 'pomodoro', 'fresh', 'ingredients', 'parmesan', 'to', 'taste']
