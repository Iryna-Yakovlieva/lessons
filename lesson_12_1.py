import codecs
import re

def delete_html_tags(html_file="/Users/irina/Desktop/PythonBase/lessons/draft.html",
                     result_file='/Users/irina/Desktop/PythonBase/lessons/my_cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    new_text = re.sub(r'<[^>]+>', '', html)
    clean_text = re.sub(r'\n\s*\n', '\n', new_text)
    with open(result_file, 'w', encoding='utf-8') as f:
        f.write(clean_text)  # Запис рядка у файл
    return result_file
print("Файл збережено в:", delete_html_tags())
