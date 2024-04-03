# 電卓アプリ

import PySimpleGUI as sg

# サイズとフォントは使い回すので変数で設定
size = (2, 2)
font = ('Arial', 20)

# 以下グローバル変数の設定
displayed_num = 0 # 表示される数字
holded_num = 0 # 演算子を押す前に作成した数字
decimal_point = 1 # 小数点第何位か
decimal_flag = False # 少数フラグ（False =整数）

# 四則演算子または[=]を押すまで数字キーを押すごとに桁数を増やしながら数字を並べる関数
def stack_num(number):
    # グローバル変数の宣言をしないとdisplayed_numがローカル変数扱いされてしまう
    global displayed_num
    displayed_num = displayed_num * 10 + number
    return displayed_num

# 数字キーを押すごとに小数点以下の数字を並べていく関数
def add_decimal(number):
    # グローバル変数の宣言をしないとdisplayed_numがローカル変数扱いされてしまう
    global displayed_num, decimal_point
    displayed_num = displayed_num + number * 1 / 10**decimal_point 
    decimal_point += 1
    return displayed_num

# 表示される数、小数点第何位、小数点フラグの３つの変数をリセットする関数(使いまわすためコードが長くなるので関数にした）
def reset_var():
    global displayed_num, decimal_point, decimal_flag
    displayed_num = 0
    decimal_flag = False
    decimal_point = 1


layout = [[sg.Text('電卓', font=font)],
          [sg.Text(key='-出力-', font=font, size=(30, 1), background_color='#000', relief=sg.RELIEF_SOLID, border_width=5), sg.Button('C',size=(8, 1), font=font, key='C')],
          # 同一の[]内に入れるた要素は横並び
          [sg.Button(7,size=size, font=font, key=7),sg.Button(8,size=size, font=font, key=8),sg.Button(9,size=size, font=font, key=9),sg.Button('/',size=size, font=font, key='/')],
          [sg.Button(4,size=size, font=font, key=4),sg.Button(5,size=size, font=font, key=5),sg.Button(6,size=size, font=font, key=6),sg.Button('*',size=size, font=font, key='*')],
          [sg.Button(1,size=size, font=font, key=1),sg.Button(2,size=size, font=font, key=2),sg.Button(3,size=size, font=font, key=3),sg.Button('-',size=size, font=font, key='-')],
          [sg.Button(0,size=size, font=font, key=0),sg.Button('.',size=size, font=font, key='.'),sg.Button('=',size=size, font=font, key='='),sg.Button('+',size=size, font=font, key='+')]]


window = sg.Window('電卓', layout)
          
while True:
    
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    # 数字キーを押すと小数点以下に数字が表示されるようにするためのフラグの変更
    elif event == '.':
        decimal_flag = True

    # 数字キーを押した場合は、小数点か判断してstack_num関数またはadd_decimal関数を呼び出す
    elif event in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        # 表示されている数字が少数かどうかで呼び出す関数を変える
        if decimal_flag == False:
            displayed_num = stack_num(event)
        else:
            displayed_num = add_decimal(event)
        window['-出力-'].update(displayed_num)

    # 1回目の四則演算子キーを押下時(holded_numが0)はまだ計算しない。2回目以降、四則演算子キーの押下時(holded_numが0ではない)一旦計算し、operatorsを新しい四則演算子で更新しておく
    elif event in ['/', '*', '-', '+']:
        if holded_num == 0:
            holded_num = displayed_num
            reset_var()
            operators = event
        else:
            if operators == '/':
                holded_num = holded_num / displayed_num
                operators = event
                reset_var()
            elif operators == '*':
                holded_num = holded_num * displayed_num
                operators = event
                reset_var()
            elif operators == '-':
                holded_num = holded_num - displayed_num
                operators = event
                reset_var()
            elif operators == '+':
                holded_num = holded_num + displayed_num
                operators = event
                reset_var()
        window['-出力-'].update(holded_num)

    # [=]キーを押した場合は、表示はholded_numの値を表示し、displayed_numを0にしてリセットしておく
    elif event in ['=']:
        if holded_num == 0:
            holded_num = displayed_num
            reset_var()
        else:
            if operators == '/':
                holded_num = holded_num / displayed_num
                reset_var()
            elif operators == '*':
                holded_num = holded_num * displayed_num
                reset_var()
            elif operators == '-':
                holded_num = holded_num - displayed_num
                reset_var()
            elif operators == '+':
                holded_num = holded_num + displayed_num
                reset_var()
        window['-出力-'].update(holded_num)
        holded_num = 0

    # clearキーを押した場合、全てリセットさせ0を表示する
    elif event in ['C']:
        holded_num = 0
        operators = ''
        reset_var()
        window['-出力-'].update(displayed_num)
        

# 画面から削除して終了
window.close()