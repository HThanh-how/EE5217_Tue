import re

with open('Chapter7_Pages200_300.txt', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

figures = re.findall(r'Fig\.\s*\d+\.\d+.*?(?=\n)', text)
with open('figures_list.txt', 'w', encoding='utf-8') as out:
    for i, fstr in enumerate(figures):
        out.write(f"{i+1}. {fstr}\n")
