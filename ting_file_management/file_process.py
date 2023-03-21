import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    new_dict = dict()
    new_dict["nome_do_arquivo"] = path_file
    new_dict["qtd_linhas"] = len(txt_importer(path_file))
    new_dict["linhas_do_arquivo"] = txt_importer(path_file)

    if new_dict not in instance:
        instance.enqueue(new_dict)
        return sys.stdout.write(str(new_dict))


def remove(instance):
    if not len(instance):
        return sys.stdout.write("Não há elementos\n")
    removed = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    return sys.stdout.write(
        f"Arquivo {removed} removido com sucesso\n"
    )


def file_metadata(instance, position):
    try:
        return sys.stdout.write(str(instance.search(position)))
    except IndexError:
        return sys.stderr.write("Posição inválida")
