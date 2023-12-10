# Получение директории, в которой находится файл скрипта
import sys
import os

file_path = os.path.realpath(__file__)
script_dir = os.path.dirname(file_path)
sys.path.append(os.path.join(script_dir, 'PythonGame'))

