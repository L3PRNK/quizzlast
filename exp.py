import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class QuizApp:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.score = 0

        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title("Quiz App")
        self.root.config(bg='#e6f2ff')
        image = tk.PhotoImage(file="img_1.png")
        bg_label = tk.Label(self.root, image=image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = image


        # Set up fonts and colors
        font_question = ("castellar", 14, "bold")
        font_option = ("garamond", 12)
        color_text = "#3498DB"
        color_bg = "black"

        # Question label
        self.label_question = tk.Label(self.root, wraplength=400, font=font_question, fg=color_text, bg=color_bg)
        self.label_question.pack(pady=20)

        # Style for the radio buttons
        style = ttk.Style()
        style.configure("TRadiobutton", font=font_option, foreground=color_text, background=color_bg)

        # Radio buttons for options
        self.var_option = tk.StringVar()
        self.radio_option_a = ttk.Radiobutton(self.root, text="Option A", variable=self.var_option, value="A")
        self.radio_option_a.pack(pady=10)
        self.radio_option_b = ttk.Radiobutton(self.root, text="Option B", variable=self.var_option, value="B")
        self.radio_option_b.pack(pady=10)
        self.radio_option_c = ttk.Radiobutton(self.root, text="Option C", variable=self.var_option, value="C")
        self.radio_option_c.pack(pady=10)
        self.radio_option_d = ttk.Radiobutton(self.root, text="Option D", variable=self.var_option, value="D")
        self.radio_option_d.pack(pady=10)

        # Submit button
        self.button_submit = tk.Button(self.root, text="Submit", font=font_option, bg='white', fg=color_text, command=self.submit)
        self.button_submit.pack(pady=20)

        # Score label
        self.label_score = tk.Label(self.root, text="Score: 0", font=font_question, fg=color_text, bg=color_bg)
        self.label_score.pack()

        self.show_question()

        self.root.mainloop()

    def show_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.label_question.config(text=question[0])
            self.radio_option_a.config(text=question[1])
            self.radio_option_b.config(text=question[2])
            self.radio_option_c.config(text=question[3])
            self.radio_option_d.config(text=question[4])
            self.var_option.set("")
        else:
            self.show_result()

    def submit(self):
        selected_option = self.var_option.get()
        if selected_option == self.questions[self.current_question][-1]:
            self.score += 1
        self.current_question += 1
        self.label_score.config(text=f"Score: {self.score}")
        self.show_question()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"You scored {self.score} out of {len(self.questions)}!")



# Define your questions here
questions = [
    ["Which of the following car is a 'Convertible'?",
     "Volkswagen Golf GTI",
     "Honda S2000",
     "Mahindra Scorpio",
     "Cadillac XTS",
     "D"],
    ["Which of the following material is used to make connecting rod?  ",
     "Forged steel",
     "Mild Steel",
     "Cast Iron",
     "toll steel",
     "C"],

    ["Which of the following parts does not include an automobile chassis?  ",
     "Brakes",
     "Sterring System",
     "Differential",
     "Shock absorbers",
     "C"],
    ["What is the function of the alternator?  ",
     "Recharging the Battery",
     "Voltage Regulator",
     "Auto-ignition",
     "None of the above",
     "A"],

    ["What is the function of the alternator? ",
     "Recharging the Battery",
     "Voltage Regulator",
     "Auto-ignition",
     "None of the above",
     "B"],

    ["Which of the following automobile has two/four doors? ",
     "Convertible",
     "Special purpose vehicles",
     "Sedan",
     "Pickups",
     "C"],
    ["What is an Automobile?",
     "self-propelled vehicle",
     "used for carrying passengers and goods on the ground",
     "contains the power source for its propulsion",
     "All of the mentioned",
     "D"],

    ["Automobile can be classified based on which of the following parameter?",
     "Fuel Used",
     "Transmission",
     "Drive",
     "All of the mentioned",
     "D"],
    ["Which of the following is a classification of automobiles based on Load?",
     "Heavy transport vehicle (HTV)",
     "Sedan Hatchback car",
     "Four wheeler vehicle",
     "Front-wheel drive",
     "A"],


]
