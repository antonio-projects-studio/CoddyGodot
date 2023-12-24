#file2.py
print("Запустился file2")
from .file1 import *
print(a, b, c)
print("file2 Закончил работу")