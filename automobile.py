import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
import random

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Movies")
        self.master.geometry("990x660")
        self.master.resizable(False, False)

        # Load questions from CSV file
        self.questions = pd.read_csv('automobile.csv')

        # Create widgets
        self.background_image = ImageTk.PhotoImage(Image.open("mm (1).png"))
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)
        # Create widgets
        self.question_label = tk.Label(self.master, text="Question", font=("Helvetica", 35),wraplength=1000,bg='black',fg='white')
        self.question_label.pack(pady=10)

        self.option_a = tk.Button(self.master, text="Option A", font=("Helvetica", 20),bg='black',fg='white',
                                  command=lambda: self.check_answer("A"))
        self.option_a.pack(pady=5)

        self.option_b = tk.Button(self.master, text="Option B", font=("Helvetica", 20),bg='black',fg='white',
                                  command=lambda: self.check_answer("B"))
        self.option_b.pack(pady=5)

        self.option_c = tk.Button(self.master, text="Option C", font=("Helvetica", 20),bg='black',fg='white',
                                  command=lambda: self.check_answer("C"))
        self.option_c.pack(pady=5)

        self.option_d = tk.Button(self.master, text="Option D", font=("Helvetica", 20),bg='black',fg='white',
                                  command=lambda: self.check_answer("D"))
        self.option_d.pack(pady=5)

        self.next_button = tk.Button(self.master, text="Next", font=("Helvetica", 20), command=self.next_question)
        self.next_button.pack(pady=10)

        self.score_label = tk.Label(self.master, text="Score: 0", font=("Helvetica", 20))
        self.score_label.pack(pady=10)

        # Initialize game state
        self.current_question = None
        self.correct_answer = None
        self.score = 0
        self.questions_answered = 0

        # Start game
        self.next_question()

    def next_question(self):
        # Select a random question from the DataFrame
        self.current_question = self.questions.sample(n=1)

        if self.questions_answered < 10:
            # Update the question label
            self.question_label.config(text=self.current_question['Question'].values[0])

            # Update the option buttons
            self.option_a.config(text=self.current_question['Option A'].values[0], state="normal")
            self.option_b.config(text=self.current_question['Option B'].values[0], state="normal")
            self.option_c.config(text=self.current_question['Option C'].values[0], state="normal")
            self.option_d.config(text=self.current_question['Option D'].values[0], state="normal")

            # Set the correct answer
            self.correct_answer = self.current_question['Answers'].values[0]

            # Initialize the state of each option button
            self.option_states = [True, True, True, True]

            # Enable the Next button
            self.next_button.config(state="disabled")
            self.questions_answered += 1

        else:
            self.l1 = tk.Label(root, text=f"score={self.score}", font=("Times", 25), bg="yellow")
            self.l1.pack()
            self.question_label.config(text=f"Final Score: {self.score}")
            self.option_a.pack_forget()
            self.option_b.pack_forget()
            self.option_c.pack_forget()
            self.option_d.pack_forget()
            self.score_label.pack_forget()
            self.next_button.pack_forget()

            self.restart_button = tk.Button(self.master, text="Certification", font=("Helvetica", 20),
                                            command=self.restart_game)
            self.restart_button.pack(pady=10)

    def restart_game(self):
            root.destroy()
            import txtcreator

    def check_answer(self, answer):
        # Check if the answer is correct
        if answer == self.correct_answer:
            self.score += 1

        # Update the score label
        self.score_label.config(text="Score: {}".format(self.score))

        # Disable the option buttons and enable the Next button
        self.option_a.config(state="disabled")
        self.option_b.config(state="disabled")
        self.option_c.config(state="disabled")
        self.option_d.config(state="disabled")
        self.next_button.config(state="normal")


root = tk.Tk()
app = QuizGame(root)
root.mainloop()