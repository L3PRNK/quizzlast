import tkinter as tk
from tkinter import*
from PIL import ImageTk

def sports_final():
    root.destroy()
    import sports

def gk():
    root.destroy()
    import gk

def movies():
    root.destroy()
    import movies


def auto_mobile():
        root.destroy()
        import automobile


def on_button_click(choice):
    print(f"Choice {choice} selected")

# Create tkinter window
root = tk.Tk()
root.title("Quiz")
root.geometry("1280x960")

Backgroundimage=ImageTk.PhotoImage(file='bgimage1.png')
bgLabel=Label(root,image=Backgroundimage)
bgLabel.grid()
# Create buttons for choices
button1 = Button(root,text='General Knowleadge',bd=0,bg='Black',fg='pink',cursor='hand2',width=25,font=('Microsoft Yahei UI Light',20, 'bold underline')
          ,command=gk)
button1.place(x=100,y=250)

button2 = Button(root,text='AutoMobile',bd=0,bg='Black',fg='blue',cursor='hand2',width=25,font=('Microsoft Yahei UI Light', 20, 'bold underline')
          ,command=auto_mobile)
button2.place(x=300,y=350)

button3 = Button(root,text='Sports',bd=0,bg='Black',fg='pink',cursor='hand2',width=25,font=('Microsoft Yahei UI Light',20, 'bold underline')
          ,command=sports_final)
button3.place(x= 500 ,y=450 )

button4 = Button(root,text='Movies',bd=0,bg='Black',fg='blue',cursor='hand2',width=25,font=('Microsoft Yahei UI Light', 20, 'bold underline')
            ,command=movies)
button4.place(x= 800 ,y= 550   )

root.mainloop()