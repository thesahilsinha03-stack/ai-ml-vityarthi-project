import datetime

current_date = datetime.date.today().strftime('%Y-%m-%d')
current_date_lst = current_date.split('-')

bday_log = [
   ('Ayushi', ('1999', '10', '19')),
   ('Yash', ('1999', '04', '21')),
]

# Loop to allow multiple entries
while True:
    add = input('To add a birthday type "y" (or any other key to finish): ').strip().lower()
    
    if add == 'y':
        new = input('Add birthday in format yyyy-mm-dd: ')
        name = input('Whose bday? ')
        date = new.split('-')
        bday_log.append((name, tuple(date)))
        print(f" Added {name} to the list!\n")
    else:
        break # Exit the loop if the user doesn't type 'y'

print("\n--- Checking for birthdays today ---")

for birthday in bday_log:
    # Check if month and day match
    if current_date_lst[1] == birthday[1][1] and current_date_lst[2] == birthday[1][2]:
        age = int(current_date_lst[0]) - int(birthday[1][0])
        
        # Logic for ordinal suffix (st, nd, rd, th)
        if 10 <= age % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(age % 10, 'th')
            
        print(f"🎉 It's {birthday[0]}'s {age}{suffix} Birthday!")
