import random
from data import wildcard_df
import pandas as pd

# Expanded list of 10 subnet questions with associated context
subnet_questions = [
    {
        "ip": "172.16.0.0", 
        "subnet_mask": "255.255.255.224", 
        "question": "What is the wildcard mask (WCM)?", 
        "answer": "0.0.0.31"
    },
    {
        "ip": "192.168.1.0", 
        "subnet_mask": "255.255.255.0", 
        "question": "What is the wildcard mask (WCM)?", 
        "answer": "0.0.0.255"
    },
    {
        "ip": "10.0.0.0", 
        "subnet_mask": "255.255.240.0", 
        "question": "What is the wildcard mask (WCM)?", 
        "answer": "0.0.15.255"
    },
    {
        "ip": "172.16.0.0", 
        "subnet_mask": "255.255.254.0", 
        "question": "What is the wildcard mask (WCM)?", 
        "answer": "0.0.1.255"
    },
    {
        "ip": "192.168.1.0", 
        "subnet_mask": "255.255.254.0", 
        "question": "What is the prefix length?", 
        "answer": "23"
    },
    {
        "ip": "172.16.0.0", 
        "subnet_mask": "255.255.0.0", 
        "question": "What is the network class and leading bit pattern (separate by /)?", 
        "answer": "B / 10"
    },
    {
        "ip": "10.0.0.0", 
        "subnet_mask": "255.0.0.0", 
        "question": "What is the network class and leading bit pattern (separate by /)?", 
        "answer": "A / 0"
    },
    {
        "ip": "192.168.1.0", 
        "subnet_mask": "255.255.255.128", 
        "question": "What is the wildcard mask (WCM)?", 
        "answer": "0.0.0.127"
    },
    {
        "ip": "172.16.0.0", 
        "subnet_mask": "255.255.240.0", 
        "question": "What is the prefix length?", 
        "answer": "20"
    },
    {
        "ip": "192.168.0.0", 
        "subnet_mask": "255.255.255.192", 
        "question": "What is the subnet mask?", 
        "answer": "255.255.255.192"
    }
]

def subnet_question():
    """ Subnet question game """
    
    # Ensure the question list is not empty
    if not subnet_questions:
        print("No subnet questions available.")
        return
    
    # Select a random question
    random_question = random.choice(subnet_questions)
    
    # Ensure all keys exist in the selected question
    if not all(k in random_question for k in ("ip", "subnet_mask", "question", "answer")):
        print("Invalid question structure. Skipping.")
        return

    # Extract data from the selected question
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
        result = "Incorrect"
    
    # Add to CSV DataFrame and print the updated DataFrame
    global wildcard_df
    new_row = pd.DataFrame([{
        "Question": f"{question} (IP: {ip_address}, Subnet Mask: {subnet_mask})",
        "Correct Answer": correct_answer,
        "User Answer": user_answer,
        "Result": result
    }])
    
    wildcard_df = pd.concat([wildcard_df, new_row], ignore_index=True)
    
    # Print wildcard_df for debugging
    print("\nUpdated wildcard_df:")
