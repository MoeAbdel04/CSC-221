import random
import pandas as pd

# DataFrames to store results
subnet_guess_df = pd.DataFrame(columns=["Question", "Correct Answer", "User Answer", "Result"])
decimal_guess_df = pd.DataFrame(columns=["Random Binary", "Correct Decimal", "Result"])
binary_guess_df = pd.DataFrame(columns=["Random Decimal", "Correct Binary", "Result"])

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
    
    print("\n===============================")
    print(f"Subnet Address: {ip_address}/{subnet_mask}")
    print(f"Question: {question}")
    
    user_answer = input("Your answer: ")
    
    if user_answer == correct_answer:
        print("\nCorrect! ✅")
        result = "Correct"
    else:
        print(f"\nIncorrect! ❌ The correct answer is {correct_answer}")
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
    print("===============================")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        ask_subnet_question()
    elif choice == "2":
        return

def binary_to_decimal():
    """
    Function to handle Binary to Decimal conversion game.
    Generates a random binary number and asks the user to guess its decimal value.
    """
    random_decimal = random.randint(0, 255)
    random_binary = format(random_decimal, '08b')
    print("\n===============================")
    print(f"Random Binary: {random_binary}")
    
    user_guess = input("Enter the Decimal value of the binary number: ")
    
    if int(user_guess) == random_decimal:
        print("\nCorrect! ✅")
        result = "Correct"
    else:
        print(f"\nIncorrect! ❌ The correct decimal value was {random_decimal}")
        result = "Wrong"
    
    # Add to DataFrame
    global decimal_guess_df
    decimal_guess_df = pd.concat([decimal_guess_df, pd.DataFrame([{
        "Random Binary": random_binary, 
        "Correct Decimal": random_decimal, 
        "Result": result
    }])], ignore_index=True)

    # Submenu
    print("\n1) Reset (generate another random binary)")
    print("2) Back to main menu")
    print("===============================")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        binary_to_decimal()
    elif choice == "2":
        return

def decimal_to_binary():
    """
    Function to handle Decimal to Binary conversion game.
    Generates a random decimal number and asks the user to guess its binary value.
    """
    random_decimal = random.randint(0, 255)
    correct_binary = format(random_decimal, '08b')
    print("\n===============================")
    print(f"Random Decimal: {random_decimal}")
    
    user_guess = input("Enter the Binary value of the decimal number: ")
    
    if user_guess == correct_binary:
        print("\nCorrect! ✅")
        result = "Correct"
    else:
        print(f"\nIncorrect! ❌ The correct binary value was {correct_binary}")
        result = "Wrong"
    
    # Add to DataFrame
    global binary_guess_df
    binary_guess_df = pd.concat([binary_guess_df, pd.DataFrame([{
        "Random Decimal": random_decimal, 
        "Correct Binary": correct_binary, 
        "Result": result
    }])], ignore_index=True)

    # Submenu
    print("\n1) Reset (generate another random decimal)")
    print("2) Back to main menu")
    print("===============================")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        decimal_to_binary()
    elif choice == "2":
        return

def save_results():
    """
    Function to save all results (subnet, binary, and decimal guesses) to CSV files.
    """
    subnet_guess_df.to_csv("subnet_guess.csv", index=False)
    decimal_guess_df.to_csv("decimal_guess.csv", index=False)
    binary_guess_df.to_csv("binary_guess.csv", index=False)
    print("\nResults saved to 'subnet_guess.csv', 'decimal_guess.csv', and 'binary_guess.csv'")
