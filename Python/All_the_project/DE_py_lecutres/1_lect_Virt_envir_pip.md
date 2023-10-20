Создание виртуального окружения
---
### Подготовка к созданию окружения (новая папка)

**mkdir new_project**
**cd new_project**

### Создание окружения

**python -m venv venv** — для Windows;
**python3 -m venv venv** — для Linux и MacOS.
(Проверяем установилась ли папка venv: **dir**)

### Активация окружения

**venv\Scripts\activate** — для Windows;
**source venv/bin/activate** — для Linux и MacOS.

### Выход из окружения

deactivate 

Работа с pip
--- 

**Package Installer for Python** — система управления 
пакетами, которая используется для установки 
и управления программными пакетами, 
написанными на Python.

- **pip install requests**
  (Requests —
это простая, но элегантная библиотека для работы с HTTP)
- **pip freeze**
  (список всех дополнений внутри нашего виртуального окружения)
- **pip freeze > requirements.txt**
  (перемещениие в requirements.txt перечня всех уже установленных дополнений)
- **more requirements.txt**
- **pip install -r requirements.txt**
  (установка в новое окружение всего содержимого файла)

# Включить интерпритатор 

- python (python3)
