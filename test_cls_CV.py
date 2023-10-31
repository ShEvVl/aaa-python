import pytest
from cls_CV import CountVectorizer


@pytest.fixture
def vectorizer_instance():
    return CountVectorizer()


# Test the fit_transform method
def test_fit_transform(vectorizer_instance):
    raw_documents = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    count_matrix = vectorizer_instance.fit_transform(raw_documents)

    assert len(count_matrix) == 2
    assert count_matrix[0] == [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    assert count_matrix[1] == [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]


# Test the get_feature_names method
def test_get_feature_names(vectorizer_instance):
    raw_documents = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]

    vectorizer_instance.fit_transform(raw_documents)
    feature_names = vectorizer_instance.get_feature_names()

    assert len(feature_names) == 12
    assert "crock" in feature_names
    assert "pot" in feature_names
    assert "pasta" in feature_names
    # Add more assertions as needed


# Test that an exception is raised when passing a string to fit_transform
def test_fit_transform_with_string(vectorizer_instance):
    with pytest.raises(ValueError):
        vectorizer_instance.fit_transform(
            "This is a string, not a list of documents"
        )


# Run the tests
if __name__ == "__main__":
    pytest.main()
