import random
import pandas as pd

# DataFrame to store subnet question results
subnet_guess_df = pd.DataFrame(columns=["Question", "Correct Answer", "User Answer", "Result"])

# List of Subnet Questions
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

def ask_subnet_question():
    """
    Function to handle Subnet Questions.
    Picks a random subnet question, asks the user to answer, and checks the answer.
    """
    random_question = random.choice(subnet_questions)
    ip_address = random_question["ip"]
    subnet_mask = random_question["subnet_mask"]
    question = random_question["question"]
    correct_answer = random_question["answer"]
    
    print(f"\nSubnet Address: {ip_address}/{subnet_mask}")
    print(f"Question: {question}")
    
    user_answer = input("Your answer: ")
    
    if user_answer == correct_answer:
        print("Correct!")
        result = "Correct"
    else:
        print(f"Incorrect! The correct answer is {correct_answer}")
        result = "Incorrect"
    
    # Add to DataFrame
    global subnet_guess_df
    subnet_guess_df = pd.concat([subnet_guess_df, pd.DataFrame([{
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
        ask_subnet_question()
    elif choice == "2":
        return

def save_subnet_results():
    """
    Function to save subnet guess results to a CSV file.
    """
    subnet_guess_df.to_csv("subnet_guess.csv", index=False)
    print("Results saved to 'subnet_guess.csv'")

def main_menu():
    """
    Main menu to navigate between different questions.
    """
    while True:
        print("\nMenu:")
        print("1. Subnet Address Question")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            ask_subnet_question()
        elif choice == "9":
            save_subnet_results()
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
