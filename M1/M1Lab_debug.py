# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:51:37 2024

@author: seidih6290
"""

# Data dictionary containing the exam questions and answers
exam = {
    1: {"question": "A learner's permit usually requires supervised driving.", "answer": False},
    2: {"question": "A commercial driver's license (CDL) is required for operating a large truck or bus.", "answer": True},
    3: {"question": "Renewal periods for driver's licenses can vary, but it's typically more frequent than every 10 years.", "answer": False},
    4: {"question": "A red traffic light always indicates that you must stop.", "answer": True},
    5: {"question": "Driving with headphones on in both ears is illegal in many states.", "answer": False},
    6: {"question": "Driving under the influence (DUI) is a serious offense, not a minor traffic violation.", "answer": True},
    7: {"question": "A yellow diamond-shaped sign is a warning or caution sign.", "answer": True},
    8: {"question": "In most states, turning right on red is allowed after a complete stop if there is no oncoming traffic.", "answer": True},
    9: {"question": "The speed limit on interstate highways is usually higher than on local roads, but it can vary.", "answer": True},
    10: {"question": "The legal age for obtaining a driver's license varies by state in the U.S.", "answer": True}
}

def start_program():
    """
    This function starts the quiz program, iterates over questions, 
    asks the user for answers, and calculates the score.
    """
    print("Start program...\n")
    correct = 0

    for q_id, ques in exam.items():
        # Display question
        print("\nQuestion", q_id)
        print(ques["question"])

        # Ask for answer
        ans = int(input("Enter 1 for True, or 2 for False: "))

        # Validate the answer
        while ans not in [1, 2]:
            print("Invalid answer!!!")
            print("\nEnter answer for the following question again\n")
            print(ques["question"])
            ans = int(input("Enter 1 for True, or 2 for False: "))

        # Convert answer to boolean
        ans = True if ans == 1 else False

        # Compare answer
        if ans == ques["answer"]:
            print("\nAnswer Correct! Well done!")
            correct += 10
        else:
            print("\nIncorrect. The correct answer is", ques["answer"])

    print("\nAll questions answered, score displayed below\n")

    # Display score
    dis_score(correct)

def dis_score(score):
    """
    Display the score and tell the user if they passed or failed.
    """
    print("Your score is", score)

    if score >= 80:
        print("You Passed!")
    else:
        print("Your score is below 80!!!")
        print("You didn't pass the exam")

def menu():
    """
    Display the menu options to the user.
    """
    print('---------MENU---------')
    print('1) Run Program')
    print('2) Exit')
    print('----------------------')