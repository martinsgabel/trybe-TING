from ting_file_management.queue import Queue


def get_line(word, dict_lines: list):
    occurences = []
    for index, current_line in enumerate(dict_lines, start=1):
        if word in current_line.lower():
            occurences.append({"linha": index})
    return occurences


def exists_word(word, instance: Queue):
    noncased_word = word.lower()
    res = []
    # search by each dict
    for index in range(len(instance)):
        current_dict = instance.search(index)
        lines = get_line(
            noncased_word, current_dict["linhas_do_arquivo"]
        )

        if not lines:
            return res

        res.append({
            "palavra": noncased_word,
            "arquivo": current_dict["nome_do_arquivo"],
            "ocorrencias": lines
        })

    return res


def search_by_word(word, instance):
    pass
