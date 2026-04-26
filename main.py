"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True, remove_duplicates=False):
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot sort {type(items)}")

    if remove_duplicates:
        items = list(set(items))

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates_arg = sys.argv[2].lower()
        if remove_duplicates_arg not in ("yes", "no"):
            print("El segundo argumento debe ser yes o no")
            sys.exit(1)
        remove_duplicates = remove_duplicates_arg == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        print("El tercer argumento indica si se quiere ordenar de forma ascendente (yes) o descendente (no)")
        sys.exit(1)

    print(f"The words will be read from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"File {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    print(sort_list(word_list, remove_duplicates=remove_duplicates))
