FILEPATH = 'todos.txt'


def getTodos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as fileLocal:
        todosLocal = fileLocal.readlines()
    return todosLocal

def writeTodos(todoArgg,filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todoArgg)

if __name__== "__main__":
    print("ee")