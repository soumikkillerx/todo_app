filename = 'files/todos.txt'


def get_todos(filename_todo=filename):
    file = open(filename_todo, 'r')
    todos = file.readlines()
    file.close()
    return todos


def write_todos(todos,filename_todo=filename):
    file = open(filename, 'w')
    file.writelines(todos)
    file.close()
