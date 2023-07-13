import os
import json


exte = {
    'Изображения': ['.jpg', '.jpeg', '.png', '.gif'],
    'Видео': ['.mp4', '.avi', '.mov'],
    'Документы': ['.doc', '.docx', '.pdf', '.txt'],
    'Другое': []
}


telegram_directory = 'C:\\Users\\User\\Downloads\\Telegram Desktop'


output_directory = 'C:\\Users\\User\\Downloads\\tg'


for category in exte:
    category_path = os.path.join(output_directory, category)
    os.makedirs(category_path, exist_ok=True)


for filename in os.listdir(telegram_directory):
    file_path = os.path.join(telegram_directory, filename)


    _, extension = os.path.splitext(filename)
    extension = extension.lower()


    category = None
    for cat, exts in exte.items():
        if extension in exts:
            category = cat
            break


    if category:
        category_path = os.path.join(output_directory, category)
        new_file_path = os.path.join(category_path, filename)
        os.rename(file_path, new_file_path)
    else:
        category_path = os.path.join(output_directory, 'Другое')
        new_file_path = os.path.join(category_path, filename)
        os.rename(file_path, new_file_path)


json_path = os.path.join(output_directory, 'exte.json')
with open(json_path, 'w') as json_file:
    json.dump(exte, json_file, indent=4)

print('Готова .')
