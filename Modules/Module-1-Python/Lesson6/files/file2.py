#file2.py
print("запустился file2")

from .file1 import *
print(a, b, c)

print("file2 закончил работу")