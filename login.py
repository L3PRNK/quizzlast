from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def login_user():
    if usernameEntry.get()=='' or  passwordEntry.get()=='':
        messagebox.showerror('Error','All fields  are required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='9820742127')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Data Connectivity Issue')
            return
        Query='use userdata'
        mycursor.execute(Query)
        Query='Select * from data where username=%s and password=%s'
        mycursor.execute(Query, (usernameEntry.get(), passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error', 'Invalid Username or Password')
        else:
            messagebox.showinfo('welcome', 'Login is sucessful')
            login_window.destroy()
            import options


def forget_pass():
    def change_password():
        if user_entry.get()==''or newpassword_entry.get()==''or Confirmpass_entry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=window)
        elif newpassword_entry.get()!=Confirmpass_entry.get():
            messagebox.showerror('Error','Passwords are not Matching',parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='9820742127',database='userdata')
            mycursor = con.cursor()
            Query='select * from data where username=%s'
            mycursor.execute(Query,(user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                Query='update data set password=%s where username=%s'
                mycursor.execute(Query,(newpassword_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset,please login with new password',parent=window)
                window.destroy()




    window = Toplevel()
    window.title('Change Password')
    bgpic = ImageTk.PhotoImage(file='background.jpg')
    bgLabel = Label(window, image=bgpic)
    bgLabel.grid()

    heading_label= Label(window, text='Reset Password', font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white',
                    fg='firebrick')
    heading_label.place(x=485, y=60)

    userlabel = Label(window, text='Username', font=('arial', 12, 'bold'), bg='white',
                    fg='orchid1')
    userlabel.place(x=470, y=130)
    user_entry = Entry(window,width=25,fg='magenta2',font=('arial', 12, 'bold'),bd=0)
    user_entry.place(x=470, y=160)
    Frame(window,width=250, height=2, bg='orchid1').place(x=470,y=180)

    newpasswordlabel = Label(window, text='New password', font=('arial', 12, 'bold'), bg='white',
                      fg='orchid1')
    newpasswordlabel.place(x=470, y=210)
    newpassword_entry = Entry(window, width=25, fg='magenta2', font=('arial', 12, 'bold'), bd=0)
    newpassword_entry.place(x=470, y=240)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=270)

    Confirmpasslabel = Label(window, text='Confirm Password', font=('arial', 12, 'bold'), bg='white',
                      fg='orchid1')
    Confirmpasslabel.place(x=470, y=310)
    Confirmpass_entry = Entry(window, width=25, fg='magenta2', font=('arial', 12, 'bold'), bd=0)
    Confirmpass_entry.place(x=470, y=340)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=370)

    ResetButton = Button(window, text='Submit', bd=0, bg='magenta2', fg='white', activebackground='magenta2',
                         activeforeground='white', cursor='hand2', width=19,
                         font=('arial', 16, 'bold'), command=change_password)
    ResetButton.place(x=470, y=390)





    window.mainloop()

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
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


def signup_page():
    login_window.destroy()
    import signup



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


forgotButton=Button(login_window,text='forgot password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light', 8, 'bold'),fg='firebrick',command=forget_pass)
forgotButton.place(x=740,y=285)

LoginButton=Button(login_window,text='Login',bd=0,bg='firebrick1',activebackground='firebrick1',activeforeground='white',cursor='hand2',width=19,font=('Microsoft Yahei UI Light', 12, 'bold'),command=login_user)
LoginButton.place(x=610,y=340)

orlabel=Label(login_window,text='-----------or-----------',font=('Open Sans',16),fg='firebrick1',bg='white')
orlabel.place(x=610,y=400)




signuplabel=Label(login_window,text='Dont have the account',font=('Open Sans',9),fg='firebrick1',bg='white')
signuplabel.place(x=600,y=450)


newaccButton=Button(login_window,text='Create One',bd=0,bg='white',fg='blue',activebackground='white',activeforeground='blue',cursor='hand2',width=9,font=('Open Sans',9,'bold underline')
                    ,command=signup_page)
newaccButton.place(x=730,y=450)





login_window.mainloop()