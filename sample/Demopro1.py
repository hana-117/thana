import PySimpleGUI as sg

layout = [  [sg.LBox([], size=(20,10), key='-FILESLB-')],
            [sg.Input(visible=False, enable_events=True, key='-IN-'), sg.FilesBrowse()],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    # When choice has been made, then fill in the listbox with the choices
    if event == '-IN-':
        window['-FILESLB-'].Update(values['-IN-'].split(';'))
window.close()