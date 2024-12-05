# Network Tools App

Description
The Network Tools App is a web-based application that provides users with tools for learning and practicing network-related concepts. It includes the following features:

- Binary to Decimal Conversion: Practice converting binary numbers to decimal format.
- Decimal to Binary Conversion: Practice converting decimal numbers to binary format.
- Classful Address Analysis: Determine the class of a given IP address.
- Wildcard Mask Determination: Calculate the wildcard mask for a given subnet mask.
- Results Management: Saves user interaction results to CSV files for review.
- This app is built with Flask and provides a user-friendly interface for practicing networking fundamentals.

SETTING UP VENV

Install virtual env with: python -m virtualenv venv

source venv/bin/activate

pip install flask

INSTALL REQUIRMENTS TO RUN APP

pip install -r requirements.txt

pip freeze > requirements.txt


cd (folder name) to run commands in the folder for the program

set SECRET_KEY=your_secret_key

flask --debug --app app run

Control c to quit