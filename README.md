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

2. Один файл.
```
uv run app/main.py -f programming.csv -r median-coffee
```

3. Без указания --report или --files.
```
uv run app/main.py -f programming.csv --report
uv run app/main.py programming.csv --report median-coffee 
```

---
