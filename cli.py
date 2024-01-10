from functions import get_todos, write_todos
import time

new_todos = []
todos = []
now =time.strptime(' %M:%H:%S')
print((f"it is {now}"))

while True:
    user_action = input('type add or show or exit or edit or complete----')
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:]
        # file = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        todos= get_todos()

        todos.append(""+todo+"\n")

        write_todos('files/todos.txt', todos)

    elif user_action.startswith('show'):
        # file = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos= get_todos()

        new_todos = [item.strip("\n") for item in todos]  # Update new_todos

        for index, item in enumerate(new_todos):
            row = f'{index + 1}--{item}'
            print(row)

    elif user_action.startswith('edit'):
        try:



            index = int(user_action[5:])
            index = index - 1

            # file = open('files/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            todos= get_todos()

            existing_todo = todos[index]
            print(existing_todo)
            new_task = input("Enter the new task")
            todos[index] = new_task +"\n"

            write_todos('files/todos.txt', todos)
        except ValueError:
            print('ur command is not valid')
            continue


    elif user_action.startswith('complete'):
        try:

            number=user_action[9:]
            # file = open('files/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            todos= get_todos()
            print(f'the todolist is {todos}')

            finish = int(input("Enter the todo number you want to complete:"))
            done = todos.pop(finish - 1)

            write_todos('files/todos.txt', todos)


            print(f"You have just finished your todo: {done}, congratulations!")
        except IndexError:
            print('no item with that index')
            continue


    elif 'exit' in user_action:
        break

    else:
        print("invalid command !!")
print('Bye!')



