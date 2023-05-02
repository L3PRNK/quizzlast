import tkinter as tk
from PIL import ImageTk, Image
import cv2

list_of_names = []

def cleanup_data():
    with open('names.txt') as f:
        for line in f:
            list_of_names.append(line.strip())
        print("Names loaded:", list_of_names)


def generate_certificates():
    for name in list_of_names:
        template = cv2.imread("certificate1.png")
        cv2.putText(template, name, (420, 1169), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 1,
                    cv2.LINE_AA)
        cv2.imwrite(f'C:/quizzlast/generated-certificates/{name}.png', template)
        print("Certificate generated for", name)

def genrate():
    generate_certificates()
    root.destroy()
    import man

def main():
    cleanup_data()

# Create the main window
root = tk.Tk()
root.title("Welcome")
root.geometry("586x304")
root.resizable(False,False)

# Load the background image
bg_image = Image.open("email bg 123.png")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label to display the welcome message
welcome_label = tk.Label(root, text="QUIZZ!!", font=("Times", 20),bg='black',fg='white')
welcome_label.place(x=200,y=100)

# Create the login button
login_button = tk.Button(root, text="Get certificate", font=("Times", 25),bg='black',fg='white',command=genrate)
login_button.place(x=200,y=150)

if __name__ == "__main__":
    main()
    root.mainloop()
