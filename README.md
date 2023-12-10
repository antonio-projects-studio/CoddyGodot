# Coddy Godot

## Содержание
- [Модуль **Python**](#python)
	- [Visual Studio Code](#visual-studio-code)
		- [Урок](#11l)
		- [Домашнее задание](#11d)
	- [Типы данных](#типы-данных)
		- [Урок](#12l)
		- [Домашнее задание](#12d)
	- [Функции](#функции)
		- [Урок](#13l)
		- [Домашнее задание](#13d)
	- [Классы](#классы)
		- [Урок](#14l)
		- [Домашнее задание](#14d)

- [Модуль **GitHub**](#github)
	- Скоро

- [Модуль **Pygame**](#pygame)
	- [Player](#player)
		- [Урок](#33l)
		- [Домашнее задание](#33d)
	- [Algorithms + NPC](#algorithms-and-npc)
		- [Урок](#34l)
		- [Домашнее задание](#34d)
	- [NPC (continue)](#npc-continue)
		- [Урок](#35l)
		- [Домашнее задание](#35d)
- [Вспомогательные материалы](#вспомогательные-материалы)
	- [Видео](#видео)
	- [Ссылки](#ссылки)

---
## Python

### Visual Studio Code

#### <div id='11l'>Урок</div>

#### <div id='11d'>Домашнее задание</div>

1. **Обязательная часть**

- Установить [Visual Studio Code](https://visualstudio.microsoft.com/ru/downloads/)
- Настроить VS, то есть создать папочку, где будете делать домашки, установить интерпретатор (Python 3.11 в Microsoft Store), запустить файл питоновский
- Зарегистрироваться на [GitHub](https://github.com/)

2. **Дополнительная часть**

- Почитать про типы данных: [ссылка]( https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-3-tipy-dannyh-preobrazovanie-i-bazovye-operacii-2022-10-14)

3. **Статьи и видео**

- Видео про установку VS: [ссылка](https://www.youtube.com/watch?v=ryosJYNOTjI)

### Типы данных

#### <div id='12l'>Урок</div>

1. Материалы урока: [ссылка](./Lessons/Module-1-Python/Lesson-2-types.ipynb)

#### <div id='12d'>Домашнее задание</div>

1. **Обязательная часть**

- Создать файл `main.py` создать list и dict с различными переменными, написать цикл с выводом каждого элемента/ключ-значения в терминал

2. **Дополнительная часть**

- Почитать про функции: [ссылка](https://pythonworld.ru/tipy-dannyx-v-python/vse-o-funkciyax-i-ix-argumentax.html)

3. **Статьи и видео**

- Типы данных в `python`: [ссылка]( https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-3-tipy-dannyh-preobrazovanie-i-bazovye-operacii-2022-10-14)

### Функции

#### <div id='13l'>Урок</div>

1. Материалы урока: [ссылка](./Lessons/Module-1-Python/Lesson-3-functions.ipynb)

#### <div id='13d'>Домашнее задание</div>


1. **Обязательная часть**

- Создать файл `main.py`. Написать три функции:
	- Принимает два аргумента и возвращает целую часть от деления a/b 
	- Принимает три аргумента и возвращает среднее минимального и максимального числа
	- Принимает бесконечное количество аргументов и возвращает максимум из них (посмотрите в инете как делать, если не найдете, то подскажу)

2. **Дополнительная часть**

- Прочитать про классы: [ссылка](https://python-scripts.com/python-class)

3. **Статьи и видео**

- Функции в `python`: [ссылка](https://pythonworld.ru/tipy-dannyx-v-python/vse-o-funkciyax-i-ix-argumentax.html)

### Классы

**На следующий урок обязательно принести логин и пароль для входа в ваш аккаунт GitHub на компьютерах Coddy**

#### <div id='14l'>Урок</div>

1. Материалы урока: [ссылка](./Lessons/Module-1-Python/Lesson-4-class.ipynb)

#### <div id='14d'>Домашнее задание</div>

1. **Обязательная часть**

- Создать файл `main.py`. Написать класс Enemy.
	
Что должно быть в классе Enemy:
- Минимум три характеристики, например, дамаг/здоровье/уровень
- Функция класса:

	```python
	@classmethod
	def move(cls):
		...

	```
- Функция экземпляра:
	 ```python 
	 def move(self):
		 ...
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

2. **Дополнительная часть**

- Прочитать про пакеты и модули: [ссылка](https://habr.com/ru/articles/718828/)
- Посмотреть видео про пакеты и модули: [ссфлка](https://www.youtube.com/watch?v=VCRxOdCueqM)
- Прочитать про git: [ссылка](https://habr.com/ru/articles/541258/)

3. **Статьи и видео**

- Классы в `python`: [ссылка](https://python-scripts.com/python-class)
- Видео про классы: [ссылка](https://www.youtube.com/watch?v=XmCAGUo5k70)
- Видео про конструкторы классов: [ссылка](https://www.youtube.com/watch?v=m4Dc8S_S-I8)

---
## GitHub

---
## Pygame

### Player

#### <div id='33l'>Урок</div>

1. Материалы урока: [ссылка](./Lessons/Module-3-Pygame/Lesson-3-player.ipynb)

#### <div id='33d'>Домашнее задание</div>

1. **Обязательная часть**

- Продолжить разрабатывать свою игру. На уроке мы добавили игрока, вы можете настроить его геометрическую форму, цвет, логику передвижения

Советую найти на YouTube понравившееся вам передвижение персонажа, зайти на `github` игры и посмотреть код

2. **Дополнительная часть**

- Познакомиться с понятием алгоритмов, на следующем уроке будем реализовывать поиск игрока: [ссылка](https://blog.skillfactory.ru/glossary/algoritm/#:~:text=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%20%E2%80%94%20%D1%8D%D1%82%D0%BE%20%D1%87%D0%B5%D1%82%D0%BA%D0%B0%D1%8F%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B9,%D0%B4%D0%BB%D1%8F%20%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B8%20%D1%8D%D1%84%D1%84%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%BC%20%D1%81%D0%BF%D0%BE%D1%81%D0%BE%D0%B1%D0%BE%D0%BC.)

3. **Статьи и видео**


### Algorithms and NPC

#### <div id='34l'>Урок</div>

1. Материалы урока: [ссылка](./Lessons/Module-3-Pygame/Lesson-4-algorithm-npc.ipynb)

#### <div id='34d'>Домашнее задание</div>

1. **Обязательная часть**

- Продолжить разрабатывать свою игру. На уроке мы добавили NPC и поговорили об алгоритмах. Подумайте, по какому алгоритму будет передвигаться NPC, попробуйте реализовать его логику. Добавьте пару NPC в игру

Советую найти на YouTube понравившееся вам передвижение NPC, зайти на `github` игры и посмотреть код

2. **Дополнительная часть**

- Посмотреть, как работает алгоритм поиска путей: [ссылка](https://www.youtube.com/watch?v=gCclsviUeUk)

3. **Статьи и видео**

- Посмотреть, видео про математику в играх: [ссылка](https://www.youtube.com/watch?v=yecPG74pU8o)


### NPC (continue)

#### <div id='35l'>Урок</div>

1. Материалы урока: [ссылка](./Lessons/Module-3-Pygame/Lesson-5-npc-continue.ipynb)

#### <div id='35d'>Домашнее задание</div>


1. **Обязательная часть**

- Продолжить разрабатывать свою игру. На уроке мы добавили поиск путей для `NPC`. Попробуйте описать свою логику передвижения `NPC` в функции `run_logic`

Советую найти на YouTube понравившееся вам передвижение NPC, зайти на `github` игры и посмотреть код

2. **Дополнительная часть**

- Посмотреть танец алгоритма сортировки пузырьком: [ссылка](https://www.youtube.com/watch?v=5JMInXAtnQg)

3. **Статьи и видео**

## Вспомогательные материалы

### Ссылки
- Команды терминала: [ссылка](./Lessons/terminal-commands.md)
- Типы данных в `python`: [ссылка]( https://proglib.io/p/samouchitel-po-python-dlya-nachinayushchih-chast-3-tipy-dannyh-preobrazovanie-i-bazovye-operacii-2022-10-14)
- Функции в `python`: [ссылка](https://pythonworld.ru/tipy-dannyx-v-python/vse-o-funkciyax-i-ix-argumentax.html)
- Классы в `python`: [ссылка](https://python-scripts.com/python-class)
- Пакеты и модули в `python`: [ссылка](https://habr.com/ru/articles/718828/)
- Git: [ссылка](https://habr.com/ru/articles/541258/)
- Алгоритмы: [ссылка](https://blog.skillfactory.ru/glossary/algoritm/#:~:text=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%20%E2%80%94%20%D1%8D%D1%82%D0%BE%20%D1%87%D0%B5%D1%82%D0%BA%D0%B0%D1%8F%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B9,%D0%B4%D0%BB%D1%8F%20%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B8%20%D1%8D%D1%84%D1%84%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%BC%20%D1%81%D0%BF%D0%BE%D1%81%D0%BE%D0%B1%D0%BE%D0%BC.)
- Как работает алгоритм поиска путей: [ссылка](https://www.youtube.com/watch?v=gCclsviUeUk)

### Видео
- Видео про установку VS: [ссылка](https://www.youtube.com/watch?v=ryosJYNOTjI)
- Видео про классы: [ссылка](https://www.youtube.com/watch?v=XmCAGUo5k70)
- Видео про конструкторы классов: [ссылка](https://www.youtube.com/watch?v=m4Dc8S_S-I8)
- Видео про пакеты и модули: [ссылка](https://www.youtube.com/watch?v=VCRxOdCueqM)
- Видео про математику в играх: [ссылка](https://www.youtube.com/watch?v=yecPG74pU8o)
- Танец алгоритма сортировки пузырьком: [ссылка](https://www.youtube.com/watch?v=5JMInXAtnQg)


