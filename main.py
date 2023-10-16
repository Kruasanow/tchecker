from tkinter import *
from tkinter.ttk import Combobox, Checkbutton

window = Tk()
window.title('Как заебала ебаная танковая помойка')

def clicked():
    choosed_res.configure(text=f'Выбранные серверы - {[k for k, v in check_choosed_srv().items() if v == True]}')

def check_choosed_srv():
    check_arr = {}
    for _ in range(9):
        if chk_state1.get() == True:
            check_arr['1'] = True
        if chk_state2.get() == True:
            check_arr['2'] = True
        if chk_state3.get() == True:
            check_arr['4'] = True
        if chk_state4.get() == True:
            check_arr['5'] = True
        if chk_state5.get() == True:
            check_arr['6'] = True
        if chk_state6.get() == True:
            check_arr['7'] = True
        if chk_state7.get() == True:
            check_arr['8'] = True
        if chk_state8.get() == True:
            check_arr['9'] = True
        
    if chk_state9.get() == True:
        keys_to_set = ['1', '2', '4', '5', '6', '7', '8', '9']
        for key in keys_to_set:
            check_arr[key] = True

    return check_arr
        

srv_list = [
            """RU1 — Россия, Москва 
            ( login.p1.worldoftanks.net )
            """,

            """RU2 — Россия, Москва 
            ( login.p2.worldoftanks.net )
            """,

            """RU4 — Россия, Екатеринбург 
            ( login.p4.worldoftanks.net )
            """,

            """RU5 — Россия, Москва 
            ( login.p5.worldoftanks.net )
            """,

            """RU6 — Россия, Москва 
            ( login.p6.worldoftanks.net )
            """,

            """RU7 — Россия, Санкт-Петербург 
            ( login.p7.worldoftanks.net )
            """,

            """RU8 — Россия, Красноярск 
            ( login.p8.worldoftanks.net )
            """,

            """RU9 — Россия, Хабаровск 
            ( login.p9.worldoftanks.net )
            """
            ]

srvs = [
            'login.p1.worldoftanks.net',
            'login.p2.worldoftanks.net',
            'login.p4.worldoftanks.net',
            'login.p5.worldoftanks.net',
            'login.p6.worldoftanks.net',
            'login.p7.worldoftanks.net',
            'login.p8.worldoftanks.net',
            'login.p9.worldoftanks.net'
            ]

l_sec = Label(window, 
          text='Эта злоебучая писанина проверяет пинг на до серверов Lesta (Мир танков)\n', 
          font=("Arial",10))
l_sec.grid(column=0,row=1)

l_head = Label(window, 
          text='ТАНКОТРАХЕР', 
          font=("Arial",30))
l_head.grid(column=0,row=0)

#-------------------------------------

l_srv1 = Label(window, 
          text=srv_list[0], 
          font=("Arial",10))
l_srv1.grid(column=0,row=3)

l_srv2 = Label(window, 
          text=srv_list[1], 
          font=("Arial",10))
l_srv2.grid(column=0,row=4)

l_srv3 = Label(window, 
          text=srv_list[2], 
          font=("Arial",10))
l_srv3.grid(column=0,row=5)

l_srv4 = Label(window, 
          text=srv_list[3], 
          font=("Arial",10))
l_srv4.grid(column=0,row=6)

l_srv5 = Label(window, 
          text=srv_list[4], 
          font=("Arial",10))
l_srv5.grid(column=0,row=7)

l_srv6 = Label(window, 
          text=srv_list[5], 
          font=("Arial",10))
l_srv6.grid(column=0,row=8)

l_srv7 = Label(window, 
          text=srv_list[6], 
          font=("Arial",10))
l_srv7.grid(column=0,row=9)

l_srv8 = Label(window, 
          text=srv_list[7], 
          font=("Arial",10))
l_srv8.grid(column=0,row=10)

#-------------------------------------


#-------------------------------------

chk_state1 = BooleanVar()
chk_state1.set(False)
chk1 = Checkbutton(window, text='', var=chk_state1)
chk1.grid(column=1,row=3)

chk_state2 = BooleanVar()
chk_state2.set(False)
chk2 = Checkbutton(window, text='', var=chk_state2)
chk2.grid(column=1,row=4)

chk_state3 = BooleanVar()
chk_state3.set(False)
chk3 = Checkbutton(window, text='', var=chk_state3)
chk3.grid(column=1,row=5)

chk_state4 = BooleanVar()
chk_state4.set(False)
chk4 = Checkbutton(window, text='', var=chk_state4)
chk4.grid(column=1,row=6)

chk_state5 = BooleanVar()
chk_state5.set(False)
chk5 = Checkbutton(window, text='', var=chk_state5)
chk5.grid(column=1,row=7)

chk_state6 = BooleanVar()
chk_state6.set(False)
chk6 = Checkbutton(window, text='', var=chk_state6)
chk6.grid(column=1,row=8)

chk_state7 = BooleanVar()
chk_state7.set(False)
chk7 = Checkbutton(window, text='', var=chk_state7)
chk7.grid(column=1,row=9)

chk_state8 = BooleanVar()
chk_state8.set(False)
chk8 = Checkbutton(window, text='', var=chk_state8)
chk8.grid(column=1,row=10)

chk_state9 = BooleanVar()
chk_state9.set(False)
chk9 = Checkbutton(window, text='Выбрать все', var=chk_state9)
chk9.grid(column=0,row=11)

#-------------------------------------

choosed_res = Label(window, 
          text='', 
          font=("Arial",10))
choosed_res.grid(column=0,row=14)

b = Button(window, 
           text='Проверить',
           background='black',
           fg='red', 
           command=clicked)
b.grid(column=0,row=13)

txt = Entry(window, width=10)
# txt.grid(column=0,row=1)

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст")  
combo.current(1)  # установите вариант по умолчанию  
# combo.grid(column=1, row=1)  


chk_state = BooleanVar()
chk_state.set(False)
chk = Checkbutton(window, text='Выбрать', var=chk_state)
# chk.grid(column=0,row=2)

window.geometry('500x800')
window.mainloop()



