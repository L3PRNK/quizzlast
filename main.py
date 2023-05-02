from tkinter import*
from PIL import ImageTk



def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def on_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)




def password_enter(event):
    if usernameEntry.get()=='Password':
        usernameEntry.delete(0,END)





login_window=Tk()

login_window.geometry('990x660+550+150')
login_window.title('Quizz')
login_window.resizable(0,0)



bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(login_window,image=bgImage)

bgLabel.place(x=0,y=0)


heading = Label(login_window, text='User Login', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white', fg='firebrick')

heading.place(x=605,y=120)


usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick')
usernameEntry.place(x=605,y=200 )
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',on_enter)

frame1=Frame(login_window,width=250,height=2,bg='firebrick').place(x=580,y=222)

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick')
passwordEntry.place(x=605,y=260 )
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)


frame2=Frame(login_window,width=250,height=2,bg='firebrick').place(x=580,y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=254)


forgotButton=Button(login_window,text='forgot password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light', 8, 'bold'),fg='firebrick')
forgotButton.place(x=740,y=285)

LoginButton=Button(login_window,text='Login',bd=0,bg='firebrick1',activebackground='firebrick1',activeforeground='white',cursor='hand2',width=19,font=('Microsoft Yahei UI Light', 12, 'bold'))
LoginButton.place(x=610,y=340)

orlabel=Label(login_window,text='-----------or-----------',font=('Open Sans',16),fg='firebrick1',bg='white')
orlabel.place(x=610,y=400)




signuplabel=Label(login_window,text='Dont have the account',font=('Open Sans',9),fg='firebrick1',bg='white')
signuplabel.place(x=600,y=450)


newaccButton=Button(login_window,text='Create One',bd=0,bg='white',fg='blue',activebackground='white',activeforeground='blue',cursor='hand2',width=9,font=('Open Sans',9,'bold underline'))
newaccButton.place(x=730,y=450)





login_window.mainloop()
