# Task 1 – Rule-Based Chatbot

## 📌 Project Overview

This project is a simple rule-based chatbot developed using Python as part of the CodSoft internship tasks.

The chatbot interacts with the user through the command line and responds to predefined questions using `if-elif-else` statements.

## 🎯 Objective

The objective of this task is to build a simple chatbot that:

* Accepts user input
* Identifies predefined queries
* Provides appropriate responses
* Maintains a basic conversation flow
* Demonstrates the use of conditional statements in Python

## 🛠️ Technologies Used

* Python
* `if-elif-else` statements
* `while` loop
* `datetime` module
* Command Line Interface (CLI)

## 💬 Features

The chatbot can respond to:

* Hello / Hi
* How are you?
* What is your name?
* Who created you?
* What can you do?
* Current time
* Current date
* Thank you / Thanks
* Bye

## ▶️ How to Run

1. Make sure Python is installed on your computer.
2. Open the terminal in the Task1 folder.
3. Run the following command:

```bash
python task1.py
```

4. Enter a predefined query.
5. Type `bye` to exit the chatbot.

## 🧠 How It Works

The chatbot continuously accepts input from the user using a `while` loop.

The input is converted to lowercase and unnecessary spaces are removed using:

```python
user = input("You: ").lower().strip()
```

The chatbot then checks the input against predefined conditions using `if`, `elif`, and `else` statements.

If the input matches a predefined rule, the corresponding response is displayed. Otherwise, the chatbot displays a message indicating that it does not understand the query.

## 📷 Sample Interaction

```text
ChatBot: Hello! I am a simple chatbot.
Type 'bye' to exit.

You: hello
ChatBot: Hello! How can I help you?

You: what is your name
ChatBot: My name is RuleBot.

You: time
ChatBot: Current time is 10:30:25

You: bye
ChatBot: Goodbye! Have a nice day.
```

## 📚 Learning Outcome

Through this task, I learned about:

* Conditional statements
* Loops
* User input handling
* String manipulation
* Basic conversation flow
* Using Python's `datetime` module
* Developing a simple rule-based chatbot
