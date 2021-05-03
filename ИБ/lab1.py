#программа составлена на языке python3.9 
#(https://www.python.org/downloads/release/python-390/)
#в ходе создания программы был использован 
#генератор форм page (http://page.sourceforge.net/)


import tkinter as tk
import tkinter.ttk as ttk
#tkinter - библиотека для работы с оконными приложениями

import random

#функция блокирует ввод с клавиатуры, кроме ctrl+C (копирование)
def ctrlEvent(e):
	if (e.state == 20 and e.keysym == 'c'): return
	return "break" #заблокировать ввод
#

abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
symbol = '!”#$%&’,*'

# функция, генерирующая пароль по заданному алгоритму
def generate(self):
    #random.choice(a) - выбрать случайный элемент из списка "a"
    
    b1=random.choice(ABC)
    
    b2=random.choice(ABC)
    
    b3=str(len(self.Text1.get()) % 10)
    
    b4=random.choice(num)
    
    b5=random.choice(symbol)
    
    b6=random.choice(abc)
    
    self.Text2.delete('0', 'end')               # 
    self.Text2.insert('0', b1+b2+b3+b4+b5+b6)   # вывод результата
#

class Form:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("520x115+1041+208")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1, 1)
        top.title("")
        self.toplevel=top

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.019, rely=0.087, relheight=0.817
                , relwidth=0.954)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.02, rely=0.553, height=32, width=185)
        
        self.Button1.configure(activebackground="#f9f9f9")
        
        self.Button1.configure(command=lambda: generate(self)) 
        
        self.Button1.configure(font="-family {Liberation Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Button1.configure(text='''Сгенерировать пароль''')

        self.Text1 = tk.Entry(self.Frame1)
        self.Text1.place(relx=0.423, rely=0.106, relheight=0.298, relwidth=0.552)

        self.Text1.configure(background="white")
        self.Text1.configure(font="-family {Liberation Sans} -size 12")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.02, rely=0.106, height=29, width=194)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(font="-family {Liberation Sans} -size 12 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label1.configure(text='''Идентификатор''')
        
        self.Text2 = tk.Entry(self.Frame1)
        self.Text2.place(relx=0.423, rely=0.574, relheight=0.298
                , relwidth=0.552)
                
        self.Text2.bind("<Key>", lambda e: ctrlEvent(e))#отследить ввод с клавиатуры в 
        # текстовом поле 2
        
        self.Text2.configure(background="white")
        self.Text2.configure(font="-family {Liberation Sans} -size 12")
        self.Text2.configure(selectbackground="blue")
        self.Text2.configure(selectforeground="white")
        

if __name__ == '__main__':
    root=tk.Tk()
    w=Form(root)
    w.toplevel.mainloop()





