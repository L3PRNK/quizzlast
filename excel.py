import tkinter as tk
from PIL import ImageTk, Image

def login():

    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Welcome")

root.geometry("626x351")
# Load the background image
bg_image = Image.open("welcomebg.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label to display the welcome message
welcome_label = tk.Label(root, text="Quizz!", font=("Arial", 24))
welcome_label.pack(pady=20)

# Create the login button
login_button = tk.Button(root, text="get certificate", font=("Arial", 14),command=login)
login_button.pack()

# Run the application
root.mainloop()
