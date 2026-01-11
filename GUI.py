from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os 
import time
from main import product

# открываем файл в текстовое поле
def open_file():
    path_list = filedialog.askopenfilenames()
    if path_list:
        name_list = [f'{os.path.split(files)[1]}\n' for files in path_list]
        path_list = [f'{files}\n' for files in path_list]
        name_list = ''.join(name_list)
        text_editor.insert(1.0, name_list)
        with open('sheet_list.txt', 'w+', encoding='utf-8') as file:
            file.writelines(path_list)
 
# сохраняем текст из текстового поля в файл
def save_file():
    filepath = filedialog.askdirectory()
    with open('export_path.txt', 'w+', encoding='utf-8') as file:
        file.write(filepath)
    return filepath
    

def go_process():    
    with open('sheet_list.txt', 'r', encoding='utf-8') as file:
        path_list = file.readlines()
    print(path_list)
    try:
        product(path_list, './export')
    except Exception as err:
        print(err)
        messagebox.showerror("Title", err)
    messagebox.showinfo('Title', 'Процесс завершен')
    # os.mkdir('export/dir')

if __name__ == "__main__":
    root = Tk()
    root.title("Lib Search")
    root.geometry("500x400")
    root.grid_rowconfigure(index=0, weight=1)
    root.grid_columnconfigure(index=0, weight=1)
    text_editor = Text()
    text_editor.grid(column=0, columnspan=3, row=0)
    open_button = ttk.Button(text="Открыть файлы", command=open_file)
    open_button.grid(column=0, row=1, sticky=NSEW, padx=5)
    # with open('sheet_list.txt', 'w+', encoding='utf-8') as file:
    #     path_list = file.readlines()
    go_button = ttk.Button(text="Старт", command=go_process)
    go_button.grid(column=1, row=1, sticky=NSEW, padx=10)

    save_button = ttk.Button(text="Папка сохранения", command=save_file)
    save_button.grid(column=2, row=1, sticky=NSEW, padx=10)

    # ttk.Progressbar(orient="horizontal", length=300, value=10).grid(column=0, row=2)

    root.mainloop()
    print('Процесс завершен!')


