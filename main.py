import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime



root = tk.Tk()
root.title('IT-инвентарь')
root.geometry('1150x720')
root.minsize(900, 600)
root.configure(bg="#f2f5fa")


BG = "#f2f5fa"
WHITE = "#ffffff"
BLUE = "#1769e8"
NAVY = "#10243d"
TEXT = "#20334d"
GRAY = "#718096"
GREEN = "#15965a"
ORANGE = "#d58a18"
RED = "#d64545"



programs = [
    {
        "name": "Microsoft Office",
        "version": "2021",
        "category": "офисные",
        "license": "Да",
        "start": "12.03.2026",
        "end": "25.10.2026",
        "computers": "Рабочий ПК, ноутбук"
    },
    {
        "name": "Adobe Photoshop",
        "version": "2024",
        "category": "графические",
        "license": "Да",
        "start": "01.02.2026",
        "end": "02.10.2026",
        "computers": "Рабочий ПК, ноутбук"
    },
    {
        "name": "Windows 11 PRO",
        "version": "23H2",
        "category": "системные",
        "license": "Да",
        "start": "10.01.2025",
        "end": "20.11.2027",
        "computers": "Рабочий ПК, ноутбук"
    },
    {
        "name": "Kaspersky Endpoint Security",
        "version": "12",
        "category": "Антивирусы",
        "license": "Да",
        "start": "15.01.2026",
        "end": "15.10.2026",
        "computers": "Рабочий ПК, ноутбук"
    },
    {
        "name": "Visual Studio Code",
        "version": "1.98",
        "category": "Разработка",
        "license": "Нет",
        "start": "05.04.2026",
        "end": "-",
        "computers": "Рабочий ПК, ноутбук"
    }
]

Computers = [
    {
        "Name": "Рабочий ПК",
        "Inventory": "PC-IT-024",
        "system": "Windows 11 PRO",
        "departament": "ИТ-Отдел"
    },
    {
        "Name": "Ноутбук",
        "Inventory": "NB-IT-011",
        "system": "Windows 11 PRO",
        "departament": "Мобильное устройство"
    }
]

request = [
    {
        'id': '1042',
        'name': 'установка Microsoft Office',
        'type': 'установка',
        'date': '20.09.2026',
        'status': 'Выполнена'
    },
    {
    'id': '1048',
    'name': 'Обновление  Adobe Photoshop',
    'type': 'Обновление',
    'status': 'В обработке'
    }
]



style = ttk.Style()







































































































