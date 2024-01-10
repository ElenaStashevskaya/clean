#программа удаляет все файлы, указанные в if, из директории dir_path
import os

dir_path = r'C:\Users\Елена\Downloads'

dir_content = os.listdir(dir_path)

for file in dir_content:
    if file.endswith('.txt'):
        os.remove(os.path.join(dir_path, file))