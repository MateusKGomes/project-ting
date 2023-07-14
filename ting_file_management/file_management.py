import sys

def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido\n')
        return None
    try:
        with open(path_file, 'r') as file:
            content = file.read().split('\n')
            return content
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
        return None