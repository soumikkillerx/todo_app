import functions



import PySimpleGUI as sg

# Define the layout of the window
# Create the window
label=sg.Text("type in a todo")
input_box=sg.InputText(tooltip="enter todo",key="todo")
list_box=sg.Listbox(values=functions.get_todos(),key='todos'
                    ,enable_events=True,
                    size=[45,15])
add_button=sg.Button("add")

edit_button=sg.Button("edit")
window = sg.Window('my todo app', layout=[[label],[add_button,input_box],[list_box,edit_button]],
                   font= ('Helvetica',15))

while True:
    event,values=window.read()
    print(1,event)
    print(2,values)
    print(3,values["todos"])
    match event:
        case "add":
          todos=functions.get_todos()
          new_todo=values['todo'] +"\n"
          todos.append(new_todo)
          functions.write_todos(todos)
          window['todos'].update(values=todos)

        case "edit":
            todo_to_edit=values["todos"][0]
            new_todo=values['todo']
            todos=functions.get_todos()
            index= todos.index(todo_to_edit)
            todos[index]=new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break




# Close the window
window.close()