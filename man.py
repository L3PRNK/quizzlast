import os
from email.message import EmailMessage
import ssl
import smtplib
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

email_sender = 'da@gmail.com'
email_password = ''


def send_certificate():
    email_receiver = email_entry.get()
    user_name = name_entry.get()

    if not email_receiver or not user_name:
        messagebox.showwarning("Error", "Please enter both email and name")
        return

    subject = 'Your quiz certificate'
    body = f"""
    Hi {user_name},

    Please find your quiz certificate attached.

    Best regards,
    DarshanS
    """

    # generate certificate file name based on user name
    cert_file_name = user_name.lower().replace(" ", " ") + ".png"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # attach certificate image file
    cert_path = os.path.join("C:\\", "quizzlast", "generated-certificates", cert_file_name)
    with open(cert_path, 'rb') as f:
        image_data = f.read()
        em.add_attachment(image_data, maintype='image', subtype='png', filename=cert_file_name)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    messagebox.showinfo("Success", "Certificate sent successfully!")


# create root window
root = tk.Tk()
root.title("Certificate Sender")
root.resizable(False,False)
root.geometry("512x356")
root.configure(bg="#F7F7F7")

root.background_image = ImageTk.PhotoImage(Image.open("email bg 123.png"))
root.background_label = tk.Label(root.master, image=root.background_image)
root.background_label.place(relwidth=1, relheight=1)

# create label and entry widgets for email
email_label = ttk.Label(root, text="Email:")
email_label.pack(pady=10,anchor='center')
email_entry = ttk.Entry(root, width=30)
email_entry.pack(anchor='center')

# create label and entry widgets for name
name_label = ttk.Label(root, text="Name:")
name_label.pack(pady=10)
name_entry = ttk.Entry(root, width=30)
name_entry.pack(anchor='center')

# create send button
send_button = ttk.Button(root, text="Send Certificate", command=send_certificate)
send_button.pack(pady=20,anchor='center')

root.mainloop()

