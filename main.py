import random

# Starting nicknames
nicknames = ["The Bulldog", "The Scientist", "Twinkle-toes", "The Coder", "The Jester", "The Sloth", "Quick-Silver"]

# Get user's first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Main menu
while True:
    print("MAIN MENU (" + first_name + " " + last_name + ")")
    print("1. Change Name")
    print("2. Display a Random Nickname")
    print("3. Display All Nicknames")
    print("4. Add a Nickname")
    print("5. Remove a Nickname")
    print("6. Exit")
    choice = input("Menu Option: ")

    if choice == "1":
        # Change name
        first_name = input("Please enter first name: ")
        last_name = input("Please enter last name: ")
        print("Name has been changed to " + first_name + " " + last_name + ".")
    
    elif choice == "2":
        # Display a random nickname
        random_nickname = random.choice(nicknames)
        print("\nRANDOM NICKNAME")
        print(first_name + " '" + random_nickname + "' " + last_name + ".")
   
    elif choice == "3":
        # Display all nicknames
        print("\nALL NICKNAMES")
        for nickname in nicknames:
            print(first_name + " '" + nickname + "' " + last_name + ".")
    
    elif choice == "4":
        # Add a nickname
        new_nickname = input("Please enter a nickname to add: ")
        if new_nickname in nicknames:
            print(new_nickname + " is already in the nickname list.")
        else:
            nicknames.append(new_nickname)
            print(new_nickname + " added to the nickname list.")
   
    elif choice == "5":
        # Remove a nickname
        nickname_to_remove = input("Please enter a nickname to remove: ")
        if nickname_to_remove in nicknames:
            nicknames.remove(nickname_to_remove)
            print(nickname_to_remove + " removed from the nickname list.")
        else:
            print(nickname_to_remove + " was not found in the nickname list.")
   
    elif choice == "6":
        # Exit
        print("Goodbye!") 
        exit()