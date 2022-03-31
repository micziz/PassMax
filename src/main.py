# Make a password manager

# Import standard modules
import time

# List passwords
passwords = []
ff = open("pass.txt", "rt")
passwords = ff.readlines()

# Create a new password function
def createPassword():
    print("Create a new password")
    # Get password
    newPassword = input("Enter the new password: ")
    # Tell user password is being saved
    print("Password created, saving...")
    time.sleep(2)
    # Save password
    passwords.append(newPassword)
    f = open("pass.txt", "at")
    f.write(newPassword + "\n")

# List passwords function
def listPasswords():
    print("List all passwords")
    print("Here are your passwords")
    # Read passwords from file
    for password in passwords:
        print(f"Password: {password}")

# Edit passwords function
def editPasswords():
    # Get password to edit
    print("What password do you want to edit?")
    print("PS: You can list all passwords using L, to see which one you want to edit")
    whatPassToEdit = input("Enter the password you want to edit: ")
    # Check if password exists
    # If yes:
    if whatPassToEdit in passwords:
        # Get new password
        print("What do you want to change it to?")
        newPassword = input("Enter the new password: ")
        # Add to list
        passwords[passwords.index(whatPassToEdit)] = newPassword
        # Tell user password is being saved
        print("Password changed, saving...")
        # Delete old password
        with open("pass.txt", "r") as f:
            # read data line by line 
            data = f.readlines()
        with open("pass.txt", "wt") as f:
            for line in data:
                if line.strip("\n") != whatPassToEdit: 
                    f.write(line)
        # Save new password
        with open("pass.txt", "at") as f:
            f.write(newPassword + "\n")
    # If no:
    else:
        # Tell user password does not exist
        print("Password not found")

# Delete passwords function
def deletePasswords():
    # Get password to delete
    print("What password do you want to delete?")
    print("PS: You can list all passwords using L, to see which one you want to delete")
    whatPassToDelete = input("Enter the password you want to delete: ")
    # If password exists:
    if whatPassToDelete in passwords:
        # Delete password
        print("Password deleted, saving...")
        with open("pass.txt", "r") as f:
            # read data line by line 
            data = f.readlines()
        with open("pass.txt", "wt") as f:
            for line in data:
                if line.strip("\n") != whatPassToDelete: 
                    f.write(line)
    # If password does not exist:
    else:
        # Tell user password does not exist
        print("Password not found")
        
# Dlete all passwords function
def deleteAllPasswords():
    # Confirm deletion
    print("Are you sure you want to delete all passwords?")
    print("PS: You can deleate just one password using D, to see which one you want to delete")
    deleteAll = input("Enter Y to delete all passwords: ")
    # If yes:
    if deleteAll == "Y":
        # Say deleting
        print("All passwords deleted, saving...")
        with open("pass.txt", "w") as f:
            f.write("")
    # If no:
    else:
        # Say not deleting
        print("Not deleting, returning to normal program")


# While loop to keep program running
while True:
    # Welcome user
    print("Welcome to tpm")
    # Ask user what they want to do
    print("What do you want to do today?")
    # List options
    whatToDo = input("[C]reate a new password, [L]ist all passwords, [E]dit a password, [D]elete a password, [DA]Deleate all passwords [Q]uit: ")
    # If user wants to create a new password
    if whatToDo == "C":
        # Call createPassword function
        createPassword()
    # If user wants to list all passwords
    elif whatToDo == "L":
        # Call listPasswords function
        listPasswords()
    # If user wants to edit a password
    elif whatToDo == "E":
        # Ask user which password to edit
        editPasswords()
    elif whatToDo == "D":
        # Ask user which password to delete
        deletePasswords()
    elif whatToDo == "DA":
        # Deleate all passwords
        deleteAllPasswords()
    elif whatToDo == "Q":
        print("Quitting, goodbye!")
        break
    