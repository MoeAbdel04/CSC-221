import random
import pandas as pd
import unittest
from unittest import mock

# DataFrames to store results
subnet_guess_df = pd.DataFrame(columns=["Question", "Correct Answer", "User  Answer", "Result"])
decimal_guess_df = pd.DataFrame(columns=["Random Binary", "Correct Decimal", "Result"])
binary_guess_df = pd.DataFrame(columns=["Random Decimal", "Correct Binary", "Result"])

subnet_questions = [
    {"ip": "172.16.0.0", "subnet_mask": "255.255.255.224", "question": "What is the wildcard mask (WCM)?", "answer": "0.0.0.31"},
    {"ip": "192.168.1.0", "subnet_mask": "255.255.255.0", "question": "What is the wildcard mask (WCM)?", "answer": "0.0.0.255"},
]

def ask_subnet_question():
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
    
    global subnet_guess_df
    subnet_guess_df = pd.concat([subnet_guess_df, pd.DataFrame([{
        "Question": f"{question} (IP: {ip_address}, Subnet Mask: {subnet_mask})",
        "Correct Answer": correct_answer, 
        "User  Answer": user_answer, 
        "Result": result
    }])], ignore_index=True)

def binary_to_decimal():
    random_decimal = 255  # Fixed value for testing
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
    
    global decimal_guess_df
    decimal_guess_df = pd.concat([decimal_guess_df, pd.DataFrame([{
        "Random Binary": random_binary, 
        "Correct Decimal": random_decimal, 
        "Result": result
    }])], ignore_index=True)

def decimal_to_binary():
    random_decimal = 255  # Fixed value for testing
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
    
    global binary_guess_df
    binary_guess_df = pd.concat([binary_guess_df, pd.DataFrame([{
        "Random Decimal": random_decimal, 
        "Correct Binary": correct_binary, 
        "Result": result
    }])], ignore_index=True)

def save_results():
    subnet_guess_df.to_csv("subnet_guess.csv", index=False)
    decimal_guess_df.to_csv("decimal_guess.csv", index=False)
    binary_guess_df.to_csv("binary_guess.csv", index=False)
    print("\nResults saved to 'subnet_guess.csv', 'decimal_guess.csv', and 'binary_guess.csv'")

class TestFunctions(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=["0.0.0.31"])
    def test_ask_subnet_question_correct_answer(self, mock_input):
        ask_subnet_question()
        self.assertEqual(subnet_guess_df.iloc[0]["Result"], "Correct")


    @mock.patch('builtins.input', side_effect=["255"])
    def test_binary_to_decimal_correct_guess(self, mock_input):
        binary_to_decimal()
        self.assertEqual(decimal_guess_df.iloc[0]["Result"], "Correct")

    @mock.patch('builtins.input', side_effect=["198"])
    def test_binary_to_decimal_incorrect_guess(self, mock_input):
        binary_to_decimal()
        self.assertEqual(decimal_guess_df.iloc[0]["Correct Decimal"], 255)

    @mock.patch('builtins.input', side_effect=["11111111"])
    def test_decimal_to_binary_correct_guess(self, mock_input):
        decimal_to_binary()
        self.assertEqual(binary_guess_df.iloc[0]["Result"], "Correct")

    @mock.patch('builtins.input', side_effect=["10101110"])
    def test_decimal_to_binary_incorrect_guess(self, mock_input):
        decimal_to_binary()
        self.assertEqual(binary_guess_df.iloc[0]["Correct Binary"], "11111111")

    @mock.patch('pandas.DataFrame.to_csv')
    def test_save_results(self, mock_to_csv):
        save_results()
        self.assertEqual(mock_to_csv.call_count, 3)

if __name__ == "__main__":
    unittest.main()
