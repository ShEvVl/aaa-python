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

        raw_documents, feature_names, doc_term_matrix, fmt_pattern = vars(
            self
        ).values()

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


if __name__ == "__main__":
    raw_documents = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(raw_documents)

    print(vectorizer.get_feature_names())
    # Out: ["crock", "pot", "pasta", "never", "boil", "again",
    # "pomodoro", "fresh", "ingredients", "parmesan", "to", "taste"]

    print(count_matrix)
    # Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    # [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
