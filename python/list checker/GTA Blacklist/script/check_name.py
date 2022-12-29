import os

def print_menu():
    print("1. Check name")
    print("2. Change list")
    print("3. Display current settings")
    print("4. About")
    print("5. Exit")

# Set the initial list name to "default"
list_name = "default"

while True:
    print_menu()
    choice = input("Please enter your choice: ")

    if choice == "1":
        # First, we'll ask the user for their name
        name = input("Please enter your name: ")

        # Then, we'll open the specified list file and read its contents into a list
        list_path = os.path.join('lists', f"{list_name}.txt")
        with open(list_path, 'r') as f:
            names_list = f.read().splitlines()

        # Now we'll remove the hyphen and space from each name in the list, if requested
        remove_hyphen_space = input("Do you want to remove the leading hyphen and space from each name in the list? (y/n) ").lower() == 'y'
        if remove_hyphen_space:
            names_list = [n.strip(' -') for n in names_list]

        # Finally, we'll check if the user's name is in the list
        if name in names_list:
            # Print the "Welcome" message
            print(f"Welcome back, {name}!")
        else:
            # Print the "Sorry" message
            print(f"Sorry, {name}, you are not in the list.")

    elif choice == "2":
        # Ask the user for the new list name
        list_name = input("Please enter the new list name: ")

    elif choice == "3":
        # Display the current list name and whether or not the leading hyphen and space are being removed from each name
        remove_hyphen_space = input("Do you want to remove the leading hyphen and space from each name in the list? (y/n) ").lower() == 'y'
        print(f"Current list: {list_name}")
        print(f"Remove leading hyphen and space: {remove_hyphen_space}")

    elif choice == "4":
        # Print information about the program and the author
        print("This program allows you to check if your name is in a specified list.")
        print("The list is read from a text file located in the 'lists' folder.")
        print("You can also choose to remove the leading hyphen and space from each name in the list.")
        print("Author: OpenAI")

    elif choice == "5":
        # Exit the program
        break

