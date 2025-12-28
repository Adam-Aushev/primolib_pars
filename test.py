import re
import requests
from openpyxl import load_workbook;
import os
import json
from bs4 import BeautifulSoup
import sys
import time
import random

# Импортируем модуль Tkinter — стандартную библиотеку для создания GUI в Python
import tkinter as tk

# Создаём главное окно приложения
root = tk.Tk()

# Устанавливаем заголовок окна
root.title("Приветствие")

# Устанавливаем размеры окна: ширина 550 пикселей, высота 100 пикселей
root.geometry("550x100")

# Создаём текстовую метку с сообщением и шрифтом Arial, размер 12
label = tk.Label(
    root,
    text="Привет, это EXE файл, созданный с помощью PyInstaller!",
    font=("Arial", 12)
)

# Размещаем метку в окне и добавляем отступ сверху/снизу
label.pack(pady=20)

# Запускаем главный цикл приложения — окно остаётся открытым, пока пользователь его не закроет
root.mainloop()