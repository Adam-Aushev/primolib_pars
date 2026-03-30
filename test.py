from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os 
import time
from main import product
import json
from oculus import get_img_text, paddy
import sys
from datetime import datetime

print(datetime.now().time())
# exp_path = 'export\\input_rusmark_files\\'
# pathes = os.listdir(exp_path)
# pathes = [f'{exp_path}{path}' for path in pathes]
# code = [f'"{item}"' for item in pathes]
# code = ' + '.join(code)
# code = f'copy /b {code} collect.mrc'
# os.system(code)
# print(code)

# print(sys.platform)

# def open_file(file_path):
#     if sys.platform == 'win32':
#         os.system(f'start {file_path}')
#     elif sys.platform == 'darwin':
#         os.system(f'open {file_path}')
# # paddy('img/img_hard.jpg')

# from paddleocr import PaddleOCRVL

# pipeline = PaddleOCRVL()
# output = pipeline.predict("img/img_hard.jpg")
# for res in output:
#     res.print()
#     res.save_to_img("output")
#     res.save_to_json(save_path="output")
#     res.save_to_markdown(save_path="output")