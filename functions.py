def read_todos(filepath="todos.txt"):
    """ Return a text file and return the list of todo items """
    with open(filepath, 'r') as file:
        data = file.readlines()
    return data


def write_todos(data, filepath="todos.txt"):
    """ Takes a list of todo items and write it to a text file """
    with open(filepath, 'w') as file:
        file.writelines(data)


def print_todos(data):
    """Prints a list of todo items"""
    for index, item in enumerate(data):
        print(f"{index + 1} - {item}")


# print(__name__)

if __name__ == "__main__":
    print(read_todos())