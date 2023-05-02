import tkinter as tk
from PIL import Image, ImageTk

# create a tkinter window
root = tk.Tk()
root.geometry('500x300')

# set the background image
img = Image.open("email bg 123.png")
background_image = ImageTk.PhotoImage(img)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# create a label and an entry widget for input
name_label = tk.Label(root, text="Enter a name:", font=("Arial", 16), bg='white', fg='black')
name_label.pack(pady=20)
name_entry = tk.Entry(root,  font=("Arial", 16), bg='blue', fg='black')
name_entry.pack(pady=20)

# define a function to save the name to a file
def save_name():
    name = name_entry.get()
    with open("names.txt", "w") as f:
        f.write(name + "\n")
    name_entry.delete(0, tk.END)
    root.destroy()
    import new

save_button = tk.Button(root, text="Save", font=("Arial", 16) ,bg='blue', fg='white', command=save_name)
save_button.pack()

# start the tkinter event loop
root.mainloop()
