# Тестовое задание для Workmate

---

## Оглавление
- [Описание](#описание)
- [Примеры запуска](#примеры-запуска)

---

## Описание
CLI-скрипт для обработки CSV-файлов.
Дополнительно, добавлено логирование.

---

## Примеры запуска
1. Несколько файлов.
```
uv run app/main.py --files math.csv physics.csv --report median-coffee
```
(https://github.com/GohubSilently/test_task_workmate/blob/develop/Снимок%20экрана%202026-03-26%20в%2013.30.57.png)

2. Один файл.
```
uv run app/main.py -f programming.csv -r median-coffee
```
(https://github.com/GohubSilently/test_task_workmate/blob/develop/Снимок%20экрана%202026-03-26%20в%2013.30.38.png)

3. Без указания --report или --files.
```
uv run app/main.py -f programming.csv --report
uv run app/main.py programming.csv --report median-coffee 
```
(https://github.com/GohubSilently/test_task_workmate/blob/develop/Снимок%20экрана%202026-03-26%20в%2013.26.16.png)

---
