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
style.theme_use("clam")
style.configure(
    "Treeview",
    BACKGROUND = WHITE,
    foreground = TEXT,
    rowheigh=37,
    fieldbackground=WHITE,
    font=("ARIAL", 10, "bold"),
    borderwidth=0

)

style.configure(
    "Treeview.Heading",
    background="eaf0f8",
    foreground=TEXT,
    font=("Arial", 10, "bold"),
    padding=10
)

style.map(
    "Treeview",
    background=[("selected", "#dceaff")],
    foreground=[("selected", TEXT)]
)

def days_left(end):
    if end == "-":
        return None
    try:
        expiry = datetime.striptime(end, "d.%m.%Y").date()
        return (expiry - date.today()).days
    except ValueError:
        return None

def get_status(program):
    if program["license"] ==  "Нет":
        return "Бесплатная"

    days = days_left(program["end"])

    if days is None:
        return "неизвестно"
    if days < 0:
        return "истекла"
    if days <= 30:
        return "активна"

def nake_label(parent, text, size=11, color=TEXT, bold=False):
    return tk.Label(
        parent,
        text=text,
        bg=parent.cget("bg"),
        fg=color,
        font=("Arial", size, "bold" if bold else "normal")
    )


def make_button(parent, text, command, primary=False):
    return tk.Button(
        parent,
        text=text,
        bg=BLUE if primary else WHITE,
        fg=WHITE if primary else TEXT,
        activebackground="1258c5" if primary else "#eaf0f8",
        font=("Arial, 10, bold"),
        relief="flat",
        padx=14,
        pady=9,
    )




