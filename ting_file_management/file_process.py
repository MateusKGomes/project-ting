import sys

from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue

def process(path_file, instance: Queue):
    content = txt_importer(path_file)
    lines = sum(1 for _ in content)
    for item in instance.data:
        if item["nome_do_arquivo"] == path_file:
            return None

    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": lines,
        "linhas_do_arquivo": content
    }
    instance.enqueue(file)

    print(file)

def remove(instance: Queue):
    
    if not instance:
        print("Não há elementos")
    else:
        instance.dequeue()
        print(f"Arquivo {instance} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
