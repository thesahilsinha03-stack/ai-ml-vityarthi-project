🎂 Birthday Reminder Bot
A simple yet effective Python script to track birthdays, calculate current ages, and display them with the correct ordinal suffixes (1st, 2nd, 3rd, etc.). This version includes a looping feature to allow multiple entries in a single session.

* Table of Contents
Prerequisites

Dependencies

Installation

Configuration

Execution Steps

How the Logic Works

 *Prerequisites
Python 3.x: Ensure you have Python installed. You can check by running python --version in your terminal.

Operating System: Works on Windows, macOS, and Linux.

 *Dependencies
This project uses Zero External Dependencies.

It utilizes the built-in datetime module.

No pip install commands are required, making it lightweight and portable.

 *Installation
Clone or Create the File:
Create a new file named birthday_reminder.py on your computer.

Copy the Code:
Paste your Python code into that file and save it.

Open Terminal:
Navigate to the directory where you saved the file:

Bash
cd path/to/your/folder
⚙️ Configuration
You can pre-load the script with birthdays by editing the bday_log list directly in the code:

Python
bday_log = [
   ('Name', ('YYYY', 'MM', 'DD')),
   ('Ayushi', ('1999', '10', '19')),
]
Note: Ensure the Month and Day are strings with two digits (e.g., '05' instead of '5') to ensure a perfect match with the system clock.

 Execution Steps
Run the Script:
Execute the following command:

Bash
python birthday_reminder.py
Interactive Input:

The script will ask: To add a birthday type "y":.

Type y to add a new person.

Follow the prompts for the date (YYYY-MM-DD) and the person's name.

Exit Input Mode:

Once you are done adding names, type any other key (like 'n') to proceed to the birthday check.

View Results:

The script will scan the list and print a message if someone has a birthday today:

It's Yash's 27th Birthday!

🧠 How the Logic Works
Date Matching: The script compares current_date_lst[1] (Month) and current_date_lst[2] (Day) against the stored tuples.

Age Calculation: It subtracts the birth year from the current year.

Ordinal Suffixes: It uses a smart dictionary lookup to determine whether to append "st", "nd", "rd", or "th" based on the age (e.g., 21st, 22nd, 23rd).

Since your script currently clears the new names every time you close the terminal, would you like me to help you set up a "Save to File" feature using JSON?
