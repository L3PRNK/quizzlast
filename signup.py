from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql


def clear():
    emailentry.delete(0,END)
    Usernameentry.delete(0,END)
    Passwordentry.delete(0,END)
    ConfromPasswordentry.delete(0,END)
    check.set(0)
    signup_window.destroy()
    import login


def login_page():
 import login
 signup_window.destroy()


import pymysql
from tkinter import messagebox

def connect_database():
   if emailentry.get()=='' or Usernameentry.get()=='' or Passwordentry.get()=='':
       messagebox.showerror('Error','All Fields are required')
   elif Passwordentry.get() !=ConfromPasswordentry.get():
       messagebox.showerror('Error','Password Mismatch')
   elif check.get()==0:
       messagebox.showerror('Error','Please Accept to Terms and Condtions')

   else:
       try:
          con = pymysql.connect(host='localhost', user='root', password='9820742127')
          mycursor=con.cursor()
       except :
         messagebox.showerror('Error','Database Connectivity Issue, Please Try again')
         return
       try:
          Query = 'create database userdata'
          mycursor.execute(Query)
          Query = 'use userdata'
          mycursor.execute(Query)
          Query = 'create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
          mycursor.execute(Query)
       except:
           mycursor.execute('use userdata')

       Query='select * from data where username=%s'
       mycursor.execute(Query,(Usernameentry.get()))
       row=mycursor.fetchone()
       if row !=None:
           messagebox.showerror('Error','Username Already Exists')


       else:
           Query='insert into data(email,username,password) values(%s,%s,%s)'
           mycursor.execute(Query,(emailentry.get(),Usernameentry.get(),Passwordentry.get()))
           con.commit()
           con.close()
           messagebox.showinfo('Success','User is Succesfully Registered')
           clear()
           import login




signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)
Backgroundimage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(signup_window,image=Backgroundimage)
bgLabel.grid()

frame=Frame(signup_window)
frame.place(x=554,y=100)




heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white', fg='red')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light',10 , 'bold'), bg='white', fg='red')
emailLabel.grid(row=1 ,column=0,sticky='w',padx=25)

emailentry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10 , 'bold'),fg='white',bg='firebrick1')
emailentry.grid(row=2,column=0,sticky='w',padx=25)


UsernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light',10 , 'bold'), bg='white', fg='red')
UsernameLabel.grid(row=3 ,column=0,sticky='w',padx=25,pady=(10,0))

Usernameentry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10 , 'bold'),fg='white',bg='firebrick1')
Usernameentry.grid(row=4,column=0,sticky='w',padx=25,pady=(10,0))

PasswordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light',10 , 'bold'), bg='white', fg='red')
PasswordLabel.grid(row=5 ,column=0,sticky='w',padx=25,pady=(10,0))

Passwordentry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10 , 'bold'),fg='white',bg='firebrick1')
Passwordentry.grid(row=6,column=0,sticky='w',padx=25,pady=(10,0))


ConfromPasswordLabel = Label(frame, text='ConfromPassword', font=('Microsoft Yahei UI Light',10 , 'bold'), bg='white', fg='red')
ConfromPasswordLabel.grid(row=7 ,column=0,sticky='w',padx=25,pady=(10,0))

ConfromPasswordentry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10 , 'bold'),fg='white',bg='firebrick1')
ConfromPasswordentry.grid(row=8,column=0,sticky='w',padx=25,pady=(10,0))

check=IntVar()
termsandcondition=Checkbutton(frame,text='I Agree to Terms And Condition',font=('Microsoft Yahei UI Light',9 , 'bold'),cursor='hand2',variable=check)
termsandcondition.grid(row=9,column=0,pady=10,padx=15)


SignupButton=Button(frame,text='Signup',bd=0,bg='firebrick1',cursor='hand2',width=19,activebackground='firebrick1',activeforeground='white'
                    ,font=('Microsoft Yahei UI Light', 12, 'bold'),command=connect_database)
SignupButton.grid(row=10,column=0,pady=10)

Alreadyaccount = Label(frame, text='Already have an Account?', font=('Microsoft Yahei UI Light',10 , 'bold'), bg='white', fg='red')
Alreadyaccount.grid(row=11 ,column=0,sticky='w',padx=25,pady=(10,0))

LoginButton=Button(frame,text='Login',bd=0,bg='white',fg='blue',cursor='hand2',font=('Microsoft Yahei UI Light', 9, 'bold underline')
                  , command=login_page)
LoginButton.place(x=210,y=420
                  )


signup_window.mainloop()


