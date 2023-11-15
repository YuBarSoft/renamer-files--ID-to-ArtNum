import os
import pandas as pd


def rename_files(csv_file, folder_path):
    # Чтение данных из CSV-файла
    df = pd.read_csv(csv_file, delimiter=';', encoding='windows-1251')
    # Перебор строк в DataFrame
    for index, row in df.iterrows():
        # Получение артикула и ID из строки
        article = row['Артикул']
        id = str(row['ID'])
        ## Поиск файлов с соответствующим ID в папке
        files = [f for f in os.listdir(folder_path) if f.startswith(id)]

        ## Переименование файлов
        for file_name in files:
            old_path = os.path.join(folder_path, file_name)
            new_name = file_name.replace(id, article)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
        print(f"Переименованы файлы с ID {id} в соответствии с артикулом {article}")


csv_file = "rename.csv"
folder_path = "img"
rename_files(csv_file, folder_path)
