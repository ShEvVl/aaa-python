# aaa-python

## Условие

Реализуйте класс `CountVectorizer`, имеющий
- метод `fit_transform`
- метод `get_feature_names`

Условия:
- пользоваться внешними пакетами запрещено
- решение должно быть в *.py файлах
- не должно быть замечаний PEP8
- решение загружено на github
- если умеешь, то напиши проверки/тесты

Далее на слайдах пример получения [терм-документной матрицы](https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%80%D0%BC-%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BD%D0%B0%D1%8F_%D0%BC%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0)

## Исходные тексты

> **Crock Pot Pasta** </br>
Never boil pasta again

> **Pasta Pomodoro** </br>
Fresh ingredients Parmesan to taste

## Подсчитываем кол-во слов

> **Crock Pot Pasta** </br>
Never boil pasta again

> **Pasta Pomodoro** </br>
Fresh ingredients Parmesan to taste

### Список слов

| <!-- --> | <!-- --> | <!-- --> | <!-- --> |
|----------|----------|----------|----------|
| 0    | crock   | 6   | pomodoro   |
| 1    | pot   | 7   | fresh   |
| 2    | pasta   | 8   | ingredients   |
| 3    | never   | 9   | parmesan   |
| 4    | boil   | 10   | to   |
| 5    | again   | 11   | taste   |

## Строим матрицу
> **Crock Pot Pasta** </br>
Never boil pasta again

> **Pasta Pomodoro** </br>
Fresh ingredients Parmesan to taste

### Список слов
| <!-- --> | <!-- --> | <!-- --> | <!-- --> |
|----------|----------|----------|----------|
| 0    | crock   | 6   | pomodoro   |
| 1    | pot   | 7   | fresh   |
| 2    | pasta   | 8   | ingredients   |
| 3    | never   | 9   | parmesan   |
| 4    | boil   | 10   | to   |
| 5    | again   | 11   | taste   |

### Вектора

| <!-- --> | <!-- --> |
|----------|----------|
| 1    | [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0]   |
| 2    | [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]   |

## Пример использования

> Реализуйте класс `CountVectorizer`, имеющий метод `fit_transform`

```python
corpus = [
 'Crock Pot Pasta Never boil pasta again',
 'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
      'fresh', 'ingredients', 'parmesan', 'to', 'taste']

print(count_matrix)
Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
 ```