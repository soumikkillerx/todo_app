def get_todos(filename='files/todos.txt'):
    file = open(filename, 'r')
    todos = file.readlines()
    file.close()
    return todos


def write_todos(filename,todos_arg):
    file = open(filename, 'w')
    file.writelines(todos_arg)
    file.close()
