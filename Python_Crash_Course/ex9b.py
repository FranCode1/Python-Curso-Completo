# FILES AND EXCEPTIONS


from pathlib import Path

path = Path('ex9a.txt')

# Forma 1:
# contents = path.read_text()
# contents = contents.rstrip()

# Forma 2:
contents = path.read_text().rstrip()

print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)

# Formas de crear una ruta de archivo o Path:
# path = Path('text_files/filename.txt')
# path = Path('/home/eric/data_files/text_files/filename.txt')

