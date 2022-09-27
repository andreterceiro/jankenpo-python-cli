import simplegui
import random

# A variable to store the computer choice
computer_choice = ""
result = ""

# Handler to draw on canvas
def draw(canvas):
    '''Draw the buttons in the canvas'''
    canvas.draw_text(result, [50,85], 40, "Blue")    

def click_paper():
    '''Store the user input and evaluate (against the computer choice)'''
    evaluate("Paper")
    
def click_rock():
    '''Store the user input and evaluate (against the computer choice)'''
    evaluate("Rock")

def click_scissors():
    '''Store the user input and evaluate (against the computer choice)'''    
    evaluate("Scissors")
    
def evaluate(user_choice):
    computer_choice = random.choice(["Paper", "Rock", "Scissors"])
    
    if user_choice == "Paper":
        if computer_choice == "Rock":
            show_user_victory(computer_choice)
        elif computer_choice == "Scissors":
            show_computer_victory(computer_choice)
        else:
            show_draw(computer_choice)

    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            show_user_victory(computer_choice)
        elif computer_choice == "Paper":
            show_computer_victory(computer_choice)
        else:
            show_draw(computer_choice)
    else:
        if computer_choice == "Paper":
            show_user_victory(computer_choice)
        elif computer_choice == "Rock":
            show_computer_victory(computer_choice)
        else:
            show_draw(computer_choice)

def show_computer_victory(computer_choice):
    return show_result("Computer selected '" + computer_choice + "'. Computer wins")

def show_user_victory(computer_choice):
    return show_result("Computer selected '" + computer_choice + "'. User wins")

def show_draw(computer_choice):
    return show_result("Computer selected '" + computer_choice + "'. Draw")

def show_result(text):
    global result
    result = text

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Game", 795, 150)
frame.add_button("Paper", click_paper)
frame.add_button("Rock", click_rock)
frame.add_button("Scissors", click_scissors)

frame.set_draw_handler(draw)

# Start the frame animation
frame.start()