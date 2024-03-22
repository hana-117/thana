import PySimpleGUI as sg

layout = [
    [sg.Text('入力して下さい'), sg.InputText(key='-Input-')],
    [sg.Button('入力結果を出力します', key='-Btn1-')]
]

window = sg.Window('InputTextの値を取得', layout)

while True:
    event, value = window.read()  # イベントの入力を待つ

    if event == '-Btn1-':
        output = value['-Input-']
        sg.popup(output)
        break
    elif event is None:
        break

window.close()