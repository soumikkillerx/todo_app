import functions



import PySimpleGUI as sg

# Define the layout of the window
# Create the window
label=sg.Text("type in a todo")
input_box=sg.InputText(tooltip="enter todo")
add_button=sg.Button("add!!")


window = sg.Window('my todo app', layout=[[label,add_button],[input_box]])

window.read()

# Close the window
window.close()