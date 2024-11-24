import tkinter as tk
from tkinter import messagebox

# Quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter",
    },
    {
        "question": "Who developed Python programming language?",
        "options": ["Guido van Rossum", "Elon Musk", "Dennis Ritchie", "Bill Gates"],
        "answer": "Guido van Rossum",
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "function", "def", "lambda"],
        "answer": "def",
    },
]

# Initialize variables
current_question = 0
score = 0


def next_question():
    global current_question, score

    # Get the selected option
    selected_option = var.get()
    if selected_option == "":
        messagebox.showwarning("Warning", "Please select an option!")
        return

    # Check if the answer is correct
    if selected_option == questions[current_question]["answer"]:
        score += 1
        messagebox.showinfo("Correct!", "That's the right answer!")
    else:
        messagebox.showerror("Wrong!", f"Correct answer: {questions[current_question]['answer']}")

    # Load the next question
    current_question += 1
    if current_question < len(questions):
        load_question()
    else:
        show_result()


def load_question():
    global current_question

    # Update question and options
    question_label.config(text=f"Q{current_question + 1}: {questions[current_question]['question']}")
    for i, option in enumerate(questions[current_question]["options"]):
        option_buttons[i].config(text=option, value=option)
    var.set("")  # Clear the previous selection


def show_result():
    # Display the final score
    messagebox.showinfo("Quiz Completed", f"Your score: {score}/{len(questions)}")
    root.destroy()  # Close the app


# Initialize the main tkinter window
root = tk.Tk()
root.title("Python Quiz App")

# Create a frame for the quiz
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Question label
question_label = tk.Label(frame, text="", font=("Arial", 14), wraplength=400, justify="left")
question_label.pack(pady=10)

# Radio buttons for options
var = tk.StringVar(value="")  # Stores the selected option
option_buttons = []
for i in range(4):
    button = tk.Radiobutton(frame, text="", variable=var, value="", font=("Arial", 12), anchor="w")
    button.pack(fill="x", padx=20, pady=5)
    option_buttons.append(button)

# Next button
next_button = tk.Button(root, text="Next", command=next_question, font=("Arial", 12), bg="blue", fg="white")
next_button.pack(pady=10)

# Load the first question
load_question()

# Run the application
root.mainloop()