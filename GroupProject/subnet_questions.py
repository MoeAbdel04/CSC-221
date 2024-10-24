import random
from data import wildcard_df
import pandas as pd

# Sample subnet questions with associated context
subnet_questions = [
    {
        "ip": "172.16.0.0", 
        "subnet_mask": "255.255.255.224", 
        "question": "What is the wild card mask (WCM)?", 
        "answer": "0.0.0.31"
    },
    {
        "ip": "192.168.1.0", 
        "subnet_mask": "255.255.255.0", 
        "question": "What is the wild card mask (WCM)?", 
        "answer": "0.0.0.255"
    },
    {
        "ip": "10.0.0.0", 
        "subnet_mask": "255.255.240.0", 
        "question": "What is the wild card mask (WCM)?", 
        "answer": "0.0.15.255"
    },
    {
        "ip": "172.16.0.0", 
        "subnet_mask": "255.255.254.0", 
        "question": "What is the wild card mask (WCM)?", 
        "answer": "0.0.1.255"
    }
]

def subnet_question():
    """ Subnet question game """
    random_question = random.choice(subnet_questions)
    ip_address = random_question["ip"]
    subnet_mask = random_question["subnet_mask"]
    question = random_question["question"]
    correct_answer = random_question["answer"]
    
    # Display the context for the question
    print(f"\nSubnet Address: {ip_address}/{subnet_mask}")
    print(f"Question: {question}")
    
    user_answer = input("Your answer: ")
    
    if user_answer == correct_answer:
        print("Correct!")
        result = "Correct"
    else:
        print(f"Incorrect! The correct answer is {correct_answer}")
        print(f"Explanation: The wildcard mask is the inverse of the subnet mask {subnet_mask}. "
              "Subtract each octet of the subnet mask from 255 to get the wildcard mask.")
        result = "Incorrect"
    
    # Add to CSV DataFrame
    global wildcard_df
    wildcard_df = pd.concat([wildcard_df, pd.DataFrame([{
        "Question": f"{question} (IP: {ip_address}, Subnet Mask: {subnet_mask})",
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
