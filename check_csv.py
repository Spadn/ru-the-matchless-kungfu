import csv
import sys

FILES_TO_CHECK = [
    "files/Etc/Localization/argument_text_en.csv",
    "files/Etc/Localization/event_dialogue_en.csv",
    "files/Etc/Localization/npc_dialogue_en.csv",
    "files/Etc/Localization/ui_en.csv"
]

def check_csv(file_path):
    errors = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        
        for line_num, row in enumerate(reader, start=2):
            if len(row) != len(header):
                errors.append(f"Ошибка на строке {line_num}: некорректное количество столбцов.")
    
    if errors:
        print(f"Ошибки в файле {file_path}:")
        for error in errors:
            print(error)
        return False  # Возвращаем False, если есть ошибки
    else:
        print(f"Ошибок в файле {file_path} не обнаружено.")
        return True

if __name__ == "__main__":
    all_files_valid = True
    for file in FILES_TO_CHECK:
        if not check_csv(file):
            all_files_valid = False
    if not all_files_valid:
        sys.exit(1)