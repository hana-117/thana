import PySimpleGUI as sg

layout = [
    [sg.Text('オリジナルテキスト')],
    [sg.Text('テキスト１', text_color='#008000', font=('YuGothic', 20),size=(10,2))],
    [sg.Text('テキスト２', text_color='#000000', font=('YuGothic', 30),size=(4,2))],
    [sg.Text('テキスト３', text_color='#ff0000', font=('YuGothic', 40),background_color='#ffffff')],
]

window = sg.Window('テキストカラーの設定', layout)

while True:
    event, value = window.read()  # イベントの入力を待つ
    print(a)

    if event is None:
        break

window.close()