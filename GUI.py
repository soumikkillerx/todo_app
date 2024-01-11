import functions
import  time



import PySimpleGUI as sg

# Define the layout of the window
sg.theme("Black")
# Create the window
label=sg.Text("type in a todo")
clock=sg.Text("",key='clock')
input_box=sg.InputText(tooltip="enter todo",key="todo")
list_box=sg.Listbox(values=functions.get_todos(),key='todos'
                    ,enable_events=True,
                    size=[45,15])
add_button=sg.Button("add")

edit_button=sg.Button("edit")
complete_button=sg.Button("complete")
exit_button=sg.Button("exit")

window = sg.Window('my todo app', layout=[[clock],[label],[add_button,input_box],[list_box,edit_button,complete_button],[exit_button]],
                   font= ('Helvetica',15))

while True:
    event,values=window.read(timeout=500)
    print(1,event)
    print(2,values)
    print(3,values["todos"])
    window['clock'].update(value=time.strftime("%b %d, %Y %h:%M:%S"))
    match event:
        case "add":
          todos=functions.get_todos()
          new_todo=values['todo'] +"\n"
          todos.append(new_todo)
          functions.write_todos(todos)
          window['todos'].update(values=todos)

        case "edit":
            try:
                todo_to_edit=values["todos"][0]
                new_todo=values['todo']
                todos=functions.get_todos()
                index= todos.index(todo_to_edit)
                todos[index]=new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
                sg.Popup("PLEASE SELECT AN ITEM FIRST",font= ('Helvetica',10))


        case 'complete':
            try:
                todo_to_complete=values['todos'][0]
                todos=functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.Popup("PLEASE SELECT AN ITEM FIRST", font=('Helvetica', 10))



        case 'exit':
            break


        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break




# Close the window
window.close()