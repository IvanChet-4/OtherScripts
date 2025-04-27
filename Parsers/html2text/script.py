import os
import html2text

# Укажите путь к директории с HTML-файлами
input_directory = '/home/user/parsers/inputsite/site.ru/'  # Указать путь
output_directory = '/home/user/parsers/outputsite/'  # Указать путь

# При необходимости, создание выходной директории
os.makedirs(output_directory, exist_ok=True)

# Проходим по всем файлам в директории
for filename in os.listdir(input_directory):
    if filename.endswith('.html'):
        # Полный путь к HTML-файлу
        html_file_path = os.path.join(input_directory, filename)

        # Открываем и читаем HTML-файл
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_doc = file.read()

        # HTML в Markdown
        markdown_text = html2text.html2text(html_doc)

        # Имя выходного файла
        md_filename = os.path.splitext(filename)[0] + '.md'
        md_file_path = os.path.join(output_directory, md_filename)

        # Записываем Markdown в файл
        with open(md_file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_text)
        print(f'Преобразован {filename} в {md_filename}')
