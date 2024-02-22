# import random

# #generate a secret number from 1 to 100 
# secret_num=random.randint(1,100)

# #initialize the attempts
# attempts=0

# print("WELCOME TO THE NUMBER GUESSING GAME ")
# print("YOU MAY SELECT ANY NUMBER FROM 1 TO 100")


# while True:
#   try:
#     #get the  players guess
#     guess=int(input("GUESS THE NUMBER BETWEEN 1 TO 100 :"))

#     #increament the attempts
#     attempts+=1
    
#     if guess==secret_num:
#       print("CONGRATULATIONS YOU GUESSED THE CORRECT NUMBER")
#       print(f"It took you {attempts} attempts")
#       break
#     elif guess>secret_num:
#       print("Try a lower number")
#     else:
#       print("Try  a higher number")
#   except ValueError:
#     print("invalid input ")
import random
import tkinter as tk

# Generate a secret number from 1 to 100
secret_num = random.randint(1, 100)

# Initialize the attempts
attempts = 0

# Function to check the player's guess
def check_guess():
    global attempts
    guess = int(guess_entry.get())
    attempts += 1

    if guess == secret_num:
        result_label.config(text=f"CONGRATULATIONS!\nYou guessed the correct number in {attempts} attempts.")
        guess_button.config(state=tk.DISABLED)
    elif guess > secret_num:
        result_label.config(text="Try a lower number")
    else:
        result_label.config(text="Try a higher number")

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Create and configure GUI elements
instructions_label = tk.Label(root, text="Welcome to the Number Guessing Game!\nYou may select any number from 1 to 100.")
instructions_label.pack()

guess_label = tk.Label(root, text="Enter your guess:")
guess_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

guess_button = tk.Button(root, text="Submit Guess", command=check_guess)
guess_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()

