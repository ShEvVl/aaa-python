# [Инструменты тестирования](https://github.com/siauPatrick/mai-python/blob/master/03-instrumenty-testirovaniya-v-python/issues.md)

## Issue-01

Для запуска исполняемого [файла](tests_issues\issue_01\morse.py) выполнить:

```python
python -m doctest -o NORMALIZE_WHITESPACE -v testing_tools\tests_issues\issue_01\morse.py
```

Полученный [результат](tests_issues\issue_01\result.txt).

<details>

```python
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('SOS!')
Expecting:
    Traceback (most recent call last):
    ...
    KeyError: '!'
ok
2 items had no tests:
    morse
    morse.decode
1 items passed all tests:
   2 tests in morse.encode
2 tests in 3 items.
2 passed and 0 failed.
Test passed.
```

</details>

## Issue-02

Для запуска исполняемого [файла](tests_issues\issue_02\test_morse.py) выполнить:

```python
pytest -v testing_tools\tests_issues\issue_02\test_morse.py
```

Полученный [результат](tests_issues\issue_02\result.txt).

<details>

```python
============================= test session starts =============================
platform win32 -- Python 3.11.2, pytest-7.4.2, pluggy-1.3.0 -- D:\AAA\tasks\aaa-python\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\AAA\tasks\aaa-python
collecting ... collected 4 items

testing_tools/tests_issues/issue-02/test_morse.py::test_decode[... --- ...-SOS] PASSED [ 25%]
testing_tools/tests_issues/issue-02/test_morse.py::test_decode[... - --- .-. -.-- -....- - .- .-.. .-STORY-TALE] PASSED [ 50%]
testing_tools/tests_issues/issue-02/test_morse.py::test_decode[.--. .. --.. --.. .- -..-. ... ..- ... .... ..-PIZZA/SUSHI] PASSED [ 75%]
testing_tools/tests_issues/issue-02/test_morse.py::test_decode[-. . -..- - -.--. .---- ----- -.--.--NEXT(10)] PASSED [100%]

============================== 4 passed in 0.02s ==============================

```

</details>

## Issue-03

Для запуска исполняемого [файла](tests_issues\issue_03\test_one_hot_encoder.py) выполнить:

```python
python -m unittest -v testing_tools\tests_issues\issue_03\test_one_hot_encoder.py
```

Полученный [результат](tests_issues\issue_03\result.txt):

<details>

```python
test_cities (testing_tools.tests_issues.issue-03.test_one_hot_encoder.TestFitTransform.test_cities) ... ok
test_empty (testing_tools.tests_issues.issue-03.test_one_hot_encoder.TestFitTransform.test_empty) ... ok
test_non_inclusion_empty_input (testing_tools.tests_issues.issue-03.test_one_hot_encoder.TestFitTransform.test_non_inclusion_empty_input) ... ok
test_non_inclusion_multiple (testing_tools.tests_issues.issue-03.test_one_hot_encoder.TestFitTransform.test_non_inclusion_multiple) ... ok
test_uniqueness (testing_tools.tests_issues.issue-03.test_one_hot_encoder.TestFitTransform.test_uniqueness) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.003s

OK
```

</details>

## Issue-04

Для запуска исполняемого [файла](tests_issues\issue_04\test_one_hot_encoder.py) выполнить:

```python
pytest -v testing_tools\tests_issues\issue_04\test_one_hot_encoder.py
```

Полученный [результат](tests_issues\issue_04\result.txt).

<details>

```python
============================= test session starts =============================
platform win32 -- Python 3.11.2, pytest-7.4.2, pluggy-1.3.0 -- D:\AAA\tasks\aaa-python\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\AAA\tasks\aaa-python
collecting ... collected 6 items

testing_tools/tests_issues/issue-04/test_one_hot_encoder.py::test_single_argument PASSED [ 16%]
testing_tools/tests_issues/issue-04/test_one_hot_encoder.py::test_multiple_arguments PASSED [ 33%]
testing_tools/tests_issues/issue-04/test_one_hot_encoder.py::test_repeated_arguments PASSED [ 50%]
testing_tools/tests_issues/issue-04/test_one_hot_encoder.py::test_no_arguments PASSED [ 66%]
testing_tools/tests_issues/issue-04/test_one_hot_encoder.py::test_empty_string_argument PASSED [ 83%]
testing_tools/tests_issues/issue-04/test_one_hot_encoder.py::test_numerical_argument PASSED [100%]

============================== 6 passed in 0.02s ==============================

```

</details>

## Issue-05

Для запуска исполняемого [файла](tests_issues\issue_05\test_what_is_year_now.py) выполнить:

```python
pytest -v testing_tools\tests_issues\issue_05\test_what_is_year_now.py
```

Генерация html

```python
pytest . -q --cov=. --cov-report html:html_dir
```

Полученный [результат](tests_issues\issue_05\result.txt).

<details>

```python
============================= test session starts =============================
platform win32 -- Python 3.11.2, pytest-7.4.2, pluggy-1.3.0
rootdir: D:\AAA\tasks\aaa-python\testing_tools\tests_issues\issue-05
plugins: cov-4.1.0
collected 3 items

test_what_is_year_now.py ...                                             [100%]

============================== 3 passed in 0.08s ==============================
```

![html](tests_issues\issue_05\cov.png)

</details>
