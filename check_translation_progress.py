import csv
import os
import re
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Путь к файлам
path = "files/Etc/Localization"
files = ["argument_text_en.csv", "event_dialogue_en.csv", "npc_dialogue_en.csv", "ui_en.csv"]

# Регулярное выражение для поиска кириллических символов (русский язык)
russian_pattern = re.compile('[А-Яа-яЁё]')

# Функция для анализа файла
def analyze_file(filename):
    total_lines = 0
    russian_lines = 0

    try:
        with open(os.path.join(path, filename), mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                total_lines += 1
                # Проверка каждой ячейки строки на наличие русского текста
                if any(russian_pattern.search(cell) for cell in row):
                    russian_lines += 1
    except Exception as e:
        logging.error(f"Ошибка при открытии файла {filename}: {e}")
        return None

    # Вычисляем процент строк на русском
    russian_percent = (russian_lines / total_lines * 100) if total_lines > 0 else 0

    # Возвращаем результаты в виде словаря
    return {
        "file_name": filename,
        "total_lines": total_lines,
        "russian_lines": russian_lines,
        "russian_percent": round(russian_percent, 2)
    }

# Анализ всех файлов
results = []
total_all_lines = 0
total_russian_lines = 0

for file in files:
    result = analyze_file(file)
    if result:
        results.append(result)
        total_all_lines += result["total_lines"]
        total_russian_lines += result["russian_lines"]

# Логируем результаты для каждого файла
for result in results:
    logging.info(f"Файл: {result['file_name']}")
    logging.info(f"Общее количество строк: {result['total_lines']}")
    logging.info(f"Количество строк на русском: {result['russian_lines']}")
    logging.info(f"Процент перевода на русский: {result['russian_percent']}%\n")

# Итог по всем файлам
total_russian_percent = (total_russian_lines / total_all_lines * 100) if total_all_lines > 0 else 0
logging.info("Итог по всем файлам:")
logging.info(f"Общее количество строк: {total_all_lines}")
logging.info(f"Общее количество строк на русском: {total_russian_lines}")
logging.info(f"Общий процент перевода на русский: {round(total_russian_percent, 2)}%")