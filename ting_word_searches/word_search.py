from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    lower_word = word.lower()

    result = []
    for el in instance.data:
        ocorrencias = []
        lines = el['linhas_do_arquivo']
        arq = el['nome_do_arquivo']
        for index, w in enumerate(lines):
            check_word = w.lower()
            if lower_word in check_word:
                ocorrencias.append({"linha": index + 1})
        if len(ocorrencias) > 0:
            result.append({
                "palavra": word,
                "arquivo": arq,
                "ocorrencias": ocorrencias
            })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
