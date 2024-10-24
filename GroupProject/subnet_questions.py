import random
from data import wildcard_df
import pandas as pd

# Sample subnet questions
subnet_questions = [
    {"question": "Enter Address Class and leading Bit Pattern (separate by /)", "answer": "B / 10"},
    {"question": "What is the prefix Length?", "answer": "19"},
    {"question": "What is the wild card mask (WCM)?", "answer": "0.0.0.31"},
    {"question": "What is the subnet mask?", "answer": "255.255.254.0"}
]

def subnet_question():
    """ Subnet question game """
    random_question = random.choice(subnet_questions)
    question = random_question["question"]
    correct_answer = random_question["answer"]
    
    print(f"\nSubnet Question: {question}")
    user_answer = input("Your answer: ")
    
    if user_answer == correct_answer:
        print("Correct!")
        result = "Correct"
    else:
        print(f"Incorrect! The correct answer is {correct_answer}")
        result = "Incorrect"
    
    # Add to CSV DataFrame
    global wildcard_df
    wildcard_df = pd.concat([wildcard_df, pd.DataFrame([{
        "Question": question,
        "Correct Answer": correct_answer,
        "User Answer": user_answer,
        "Result": result
    }])], ignore_index=True)
    
    # Submenu
    print("\n1) Reset (ask another subnet question)")
    print("2) Back to main menu")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        subnet_question()
