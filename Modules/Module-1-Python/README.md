# Python

## Содержание

- [Visual Studio Code](#visual-studio-code)
  - [Урок](#урок-11)
  - [Домашнее задание](#домашнее-задание-11)
- [Типы данных](#типы-данных)
  - [Урок](#урок-12)
  - [Домашнее задание](#домашнее-задание-12)
- [Функции](#функции)
  - [Урок](#урок-13)
  - [Домашнее задание](#домашнее-задание-13)
- [Классы](#классы)
  - [Урок](#урок-14)
  - [Домашнее задание](#домашнее-задание-14)
- [Наследование](#наследование)
  - [Урок](#урок-15)
  - [Домашнее задание](#домашнее-задание-15)
- [Импорты](#импорты)
  - [Урок](#урок-16)
  - [Домашнее задание](#домашнее-задание-16)

---

### Visual Studio Code

#### Урок 1.1

#### Домашнее задание 1.1

- **Обязательная часть**

  - Установить [Visual Studio Code](https://visualstudio.microsoft.com/ru/downloads/)
  - Настроить VS, то есть создать папочку, где будете делать домашние работы, установить интерпретатор (Python 3.11 в Microsoft Store), запустить файл `.py`
  - Зарегистрироваться на [GitHub](https://github.com/)

- **Дополнительная часть**

  - Почитать про типы данных: [ссылка]( https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-3-tipy-dannyh-preobrazovanie-i-bazovye-operacii-2022-10-14)

- **Статьи и видео**

  - Видео про установку VS: [ссылка](https://www.youtube.com/watch?v=ryosJYNOTjI)

---

### Типы данных

#### Урок 1.2

- Материалы урока: [ссылка](./Lesson-2-types.ipynb)

#### Домашнее задание 1.2

- **Обязательная часть**

  - Создать файл `main.py` создать list и dict с различными переменными, написать цикл с выводом каждого элемента/ключ-значения в терминал

- **Дополнительная часть**

  - Почитать про функции: [ссылка](https://pythonworld.ru/tipy-dannyx-v-python/vse-o-funkciyax-i-ix-argumentax.html)

- **Статьи и видео**

  - Типы данных в `python`: [ссылка]( https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-3-tipy-dannyh-preobrazovanie-i-bazovye-operacii-2022-10-14)

---

### Функции

#### Урок 1.3

- Материалы урока: [ссылка](./Lesson-3-functions.ipynb)

#### Домашнее задание 1.3

- **Обязательная часть**

  - Создать файл `main.py`. Написать три функции:
    - Принимает два аргумента и возвращает целую часть от деления a/b
    - Принимает три аргумента и возвращает среднее минимального и максимального числа
    - Принимает бесконечное количество аргументов и возвращает максимум из них (посмотрите в интернете как делать, если не найдете, то подскажу)

- **Дополнительная часть**

  - Прочитать про классы: [ссылка](https://python-scripts.com/python-class)

- **Статьи и видео**

  - Функции в `python`: [ссылка](https://pythonworld.ru/tipy-dannyx-v-python/vse-o-funkciyax-i-ix-argumentax.html)

---

### Классы

На следующий урок обязательно принести логин и пароль для входа в ваш аккаунт GitHub на компьютерах Coddy

#### Урок 1.4

- Материалы урока: [ссылка](./Lesson-4-class.ipynb)

#### Домашнее задание 1.4

- **Обязательная часть**

  Создать файл `main.py`. Написать класс Enemy. Что должно быть в классе Enemy:

  - Минимум три характеристики, например, дамаг/здоровье/уровень
  - Функция класса:

  ```python
  @classmethod
  def move(cls):
    pass
  ```

  - Функция экземпляра:

  ```python
  def move(self):
    pass
  ```

- С помощью `print` проверить, что все работает как надо:

  ```python
  print(Enemy.hp)
  ```

- Создать конструктор класса:

  ```python
  def __init__(self, x):
   self.x = x
   ...
  ```

- **Дополнительная часть**

  - Прочитать про наследование классов: [ссылка](https://metanit.com/python/tutorial/7.3.php)
  - Посмотреть видео про наследование: [ссылка](https://www.youtube.com/watch?v=7WVYqjdMa6U)
  - Прочитать про git: [ссылка](https://habr.com/ru/articles/541258/)

- **Статьи и видео**

  - Классы в `python`: [ссылка](https://python-scripts.com/python-class)
  - Видео про классы: [ссылка](https://www.youtube.com/watch?v=XmCAGUo5k70)
  - Видео про конструкторы классов: [ссылка](https://www.youtube.com/watch?v=m4Dc8S_S-I8)

---

### Наследование

На следующий урок обязательно принести логин и пароль для входа в ваш аккаунт GitHub на компьютерах Coddy

#### Урок 1.5

- Материалы урока: [ссылка](./Lesson-5-class-inheritance.ipynb)

#### Домашнее задание 1.5

- **Обязательная часть**

  - Создать файл `main.py`. Создать класс `NPC`. Он нам в дальнейшем понадобится, будем использовать в игре `Runner`, поэтому аргументы и методы должны быть с этим связаны.

  - В нашей игре будут самолеты, так что сделайте два класса, которые наследуются от `NPC`, берут от предка, например, функцию создания экземпляра (`__init__`). Отличаются от родителя логикой передвижения или чем то ещё
  
  - Подумайте, что вы хотите, чтобы делали ваши `NPC`, какие аргументы и методы для этого нужны
  - С помощью `print` проверить, что все работает как надо:

- **Дополнительная часть**

  - Прочитать про пакеты и модули: [ссылка](https://habr.com/ru/articles/718828/)
  - Посмотреть видео про пакеты и модули: [ссылка](https://www.youtube.com/watch?v=VCRxOdCueqM)
  - Прочитать про git: [ссылка](https://habr.com/ru/articles/541258/)

- **Статьи и видео**

  - Наследование в `python`: [ссылка](https://metanit.com/python/tutorial/7.3.php)
  - Видео про классы: [ссылка](https://www.youtube.com/watch?v=7WVYqjdMa6U)

---

### Импорты

#### Урок 1.6

- Материалы урока: [ссылка](./Lesson-6-import.ipynb)

#### Домашнее задание 1.6

- **Обязательная часть**

  - Создать файл `main.py`. Создать папку 'npc', туда положить файл с родительским классом и папки с файлами под ваши созданные в прошлом дз классы и настроить импорты так, чтобы в main.py был доступ ко всем классам

  **Пример:**
  
  Допустим у меня два типа `npc`:
  1. `Runner`
  2. `Shooter`

  Тогда структура папок будет выглядеть следующим образом:

  ${\color{green}\text{main.py}}$ \
  ${\color{silver}\text{npc}}$ \
  $\hookrightarrow\color{green}{\text{npc.py}}$ \
  $\hookrightarrow\color{green}{\text{\_\_init\_\_.py}}$ \
  $\hookrightarrow\color{silver}{\text{runner}}$ \
  $\qquad\hookrightarrow\color{green}{\text{runner.py}}$ \
  $\qquad\hookrightarrow\color{green}{\text{\_\_init\_\_.py}}$ \
  $\hookrightarrow\color{silver}{\text{shooter}}$ \
  $\qquad\hookrightarrow\color{green}{\text{shooter.py}}$ \
  $\qquad\hookrightarrow\color{green}{\text{\_\_init\_\_.py}}$

- **Дополнительная часть**

  - Прочитать про git: [ссылка](https://habr.com/ru/articles/541258/)

- **Статьи и видео**

  - Пакеты и модули в `python`: [ссылка](https://habr.com/ru/articles/718828/)
  - Видео про пакеты и модули: [ссылка](https://www.youtube.com/watch?v=VCRxOdCueqM)
