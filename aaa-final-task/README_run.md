# Запускаем 🍕.py ([задание](/aaa-final-task/README_task.md))

## Структура проекта

- **aaa-python**
  - *aaa-final-task*
    - `cli.py`
    - `pizz.py`
    - `README_run.md`
    - `README_task.md`
    - `test_cli.py`
    - `test_pizza.py`

## Запуск

Для запуска потребуется установить [зависимости](/aaa-final-task/requirements.txt)

Запуск осуществляется через библиотеку `click`

## Команды для запуска

<details>
<summary>menu</summary>

```python
python -m cli menu
```

Результат:

> - Margherita 🧀 size('L'/'XL'): tomato sauce, mozzarella, tomatoes
> - Pepperoni 🍕 size('L'/'XL'): tomato sauce, mozzarella, pepperoni
> - Hawaiian 🍍 size('L'/'XL'): tomato sauce, mozzarella, chicken, pineapple

</details>

<details>
<summary>order</summary>

Можно заказать два размера пиццы `L` и `XL`.

У `order` есть флаг `--courier`:

- при отсутствии означает "*самовывоз*"
- при наличии означает "*доставку*"

### Примеры

<details>
<summary>Заказываем пиццу Margherita:</summary>

- размер `L`
  - самовывоз

```python
python -m cli order Margherita L
```

**Результат:**

>Готовим на самовывоз 'Margherita' размер 'L'</br>
Пицца 'Margherita' приготовлена</br>
 Состав: tomato sauce, mozzarella, tomatoes</br>
🧑‍🍳 Приготовили за 2 c!</br>
Пиццу 'Margherita' забрали</br>
🏠 Забрали за 3 c!

- размер `L`
  - доставка

```python
python -m cli order Margherita L --courier
```

**Результат:**

>Готовим и доставляем 'Margherita' размер 'L'</br>
Пицца 'Margherita' приготовлена</br>
 Состав: tomato sauce, mozzarella, tomatoes</br>
🧑‍🍳 Приготовили за 5 c!</br>
Пицца 'Margherita' доставлена</br>
🛵 Доставили за 5 c!

- размер `XL`
  - самовывоз

```python
python -m cli order Margherita XL
```

**Результат:**

>Готовим на самовывоз 'Margherita' размер 'XL'</br>
Пицца 'Margherita' приготовлена</br>
 Состав: tomato sauce, mozzarella, tomatoes</br>
🧑‍🍳 Приготовили за 2 c!</br>
Пиццу 'Margherita' забрали</br>
🏠 Забрали за 2 c!

- размер `XL`
  - доставка

```python
python -m cli order Margherita XL --courier
```

**Результат:**

>Готовим и доставляем 'Margherita' размер 'XL'</br>
Пицца 'Margherita' приготовлена</br>
 Состав: tomato sauce, mozzarella, tomatoes</br>
🧑‍🍳 Приготовили за 4 c!</br>
Пицца 'Margherita' доставлена</br>
🛵 Доставили за 5 c!

</details>

<details>
<summary>Заказываем пиццу Pepperoni:</summary>

- размер `L`
  - самовывоз

```python
python -m cli order Pepperoni L
```

**Результат:**

>Готовим на самовывоз 'Pepperoni' размер 'L'</br>
Пицца 'Pepperoni' приготовлена</br>
 Состав: tomato sauce, mozzarella, pepperoni</br>
🧑‍🍳 Приготовили за 5 c!</br>
Пиццу 'Pepperoni' забрали</br>
🏠 Забрали за 2 c!

- размер `L`
  - доставка

```python
python -m cli order Pepperoni L --courier
```

**Результат:**

>Готовим и доставляем 'Pepperoni' размер 'L'</br>
Пицца 'Pepperoni' приготовлена</br>
 Состав: tomato sauce, mozzarella, pepperoni</br>
🧑‍🍳 Приготовили за 4 c!</br>
Пицца 'Pepperoni' доставлена</br>
🛵 Доставили за 5 c!

- размер `XL`
  - самовывоз

```python
python -m cli order Pepperoni XL
```

**Результат:**

>Готовим на самовывоз 'Pepperoni' размер 'XL'</br>
Пицца 'Pepperoni' приготовлена</br>
 Состав: tomato sauce, mozzarella, pepperoni</br>
🧑‍🍳 Приготовили за 5 c!</br>
Пиццу 'Pepperoni' забрали</br>
🏠 Забрали за 2 c!

- размер `XL`
  - доставка

```python
python -m cli order Pepperoni XL --courier
```

**Результат:**

>Готовим и доставляем 'Pepperoni' размер 'XL'</br>
Пицца 'Pepperoni' приготовлена</br>
 Состав: tomato sauce, mozzarella, pepperoni</br>
🧑‍🍳 Приготовили за 4 c!</br>
Пицца 'Pepperoni' доставлена</br>
🛵 Доставили за 5 c!

</details>

<details>
<summary>Заказываем пиццу Hawaiian:</summary>

- размер `L`
  - самовывоз

```python
python -m cli order Hawaiian L
```

**Результат:**

>Готовим на самовывоз 'Hawaiian' размер 'L'</br>
Пицца 'Hawaiian' приготовлена</br>
 Состав: tomato sauce, mozzarella, chicken, pineapple</br>
🧑‍🍳 Приготовили за 2 c!</br>
Пиццу 'Hawaiian' забрали</br>
🏠 Забрали за 5 c!

- размер `L`
  - доставка

```python
python -m cli order Hawaiian L --courier
```

**Результат:**

>Готовим и доставляем 'Hawaiian' размер 'L'</br>
Пицца 'Hawaiian' приготовлена</br>
 Состав: tomato sauce, mozzarella, chicken, pineapple</br>
🧑‍🍳 Приготовили за 4 c!</br>
Пицца 'Hawaiian' доставлена</br>
🛵 Доставили за 2 c!

- размер `XL`
  - самовывоз

```python
python -m cli order Hawaiian XL
```

**Результат:**

>Готовим на самовывоз 'Hawaiian' размер 'XL'</br>
Пицца 'Hawaiian' приготовлена</br>
 Состав: tomato sauce, mozzarella, chicken, pineapple</br>
🧑‍🍳 Приготовили за 2 c!</br>
Пиццу 'Hawaiian' забрали</br>
🏠 Забрали за 5 c!

- размер `XL`
  - доставка

```python
python -m cli order Hawaiian XL --courier
```

**Результат:**

>Готовим и доставляем 'Hawaiian' размер 'XL'</br>
Пицца 'Hawaiian' приготовлена</br>
 Состав: tomato sauce, mozzarella, chicken, pineapple</br>
🧑‍🍳 Приготовили за 4 c!</br>
Пицца 'Hawaiian' доставлена</br>
🛵 Доставили за 2 c!

</details>

</details>
