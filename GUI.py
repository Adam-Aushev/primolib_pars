from tkinter import ttk, messagebox, Label, filedialog
import os 
import time
from main import product
from tkinter import Text, Tk, NSEW
from oculus import get_img_text
from sheet_tools import write_data


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


def generate_sheet():
    path_list = filedialog.askopenfilenames()
    if path_list:
        name_list = [f'{os.path.split(files)[1]}\n' for files in path_list]
        path_list = [f'{files}\n' for files in path_list]
        name_list = ''.join(name_list)
        text_editor.insert(1.0, name_list)
        sheet_path = ''
        for each in path_list:
            each = each.strip()
            sheet_name = f'{os.path.splitext(each)[0]}.xlsx'
            sheet_data = get_img_text(each)
            print(sheet_data)
            sheet_path = write_data(sheet_name, sheet_data)
        with open('sheet_list.txt', 'w+', encoding='utf-8') as file:
            file.writelines(sheet_path)
        os.system(f'open {sheet_path}')
 

# сохраняем текст из текстового поля в файл
def save_file():
    export_path = filedialog.askdirectory()
    if export_path:
        with open('export_path.txt', 'w+', encoding='utf-8') as file:
            file.write(export_path)
        return export_path
    

def go_process():
    if not os.path.isfile('sheet_list.txt'):
        messagebox.showinfo('Title', 'Выберите таблицы для парсинга')
    elif not os.path.isfile('export_path.txt'):
        messagebox.showinfo('Title', 'Выберите Путь сохранения')
    else:
        try:
            with open('sheet_list.txt', 'r', encoding='utf-8') as sheet_list:
                sheet_list = sheet_list.readlines()
                product(sheet_list, './export')
        except Exception:
            print(Exception)
            messagebox.showerror("Title", Exception)
        messagebox.showinfo('Title', 'Процесс завершен')


    

if __name__ == "__main__":
    save_dir = 'export'
    os.mkdir(save_dir) if not os.path.isdir(save_dir) else 2
    with open('export_path.txt', 'w+', encoding='utf-8') as file:
        file.write('export/')
    root = Tk()
    root.title("Lib Search")
    root.geometry("600x500")
    root.grid_rowconfigure(index=0, weight=1)
    root.grid_columnconfigure(index=0, weight=1)
    open_text = Label(root, text='Выберите "Сгенерировать из картинки" если хотите ' \
    '\nизвлечь информацию из картинки автоматически\n' \
    'или если у вас есть готовые таблицы укажите их нажав "Выбрать таблицы\n' \
    'после нажмите "Парсинг" чтобы извлечь из сайта фалы RUSMARK')
    open_text.grid(column=0, columnspan=3, row=0)
    text_editor = Text()
    text_editor.grid(column=0, columnspan=3, row=1)
    open_button = ttk.Button(text="Сгенерировать из картинки", command=generate_sheet)
    open_button.grid(column=1, row=2, sticky=NSEW, padx=5)
    open_button = ttk.Button(text="Выбрать таблицы", command=open_file)
    open_button.grid(column=0, row=3, sticky=NSEW, padx=5)
    # with open('sheet_list.txt', 'w+', encoding='utf-8') as file:
    #     path_list = file.readlines()
    process_button = ttk.Button(text="Парсинг", command=go_process)
    process_button.grid(column=1, row=3, sticky=NSEW, padx=5)

    save_button = ttk.Button(text="Папка сохранения", command=save_file)
    save_button.grid(column=2, row=3, sticky=NSEW, padx=10)

    # ttk.Progressbar(orient="horizontal", length=300, value=10).grid(column=0, row=2)
    root.mainloop()
    print('Процесс завершен!')
    os.remove('sheet_list.txt') if os.path.isfile('sheet_list.txt') else 1
    os.remove('export_path.txt') if os.path.isfile('export_path.txt') else 1


