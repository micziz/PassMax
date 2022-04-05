# Import standard modules
import time, base64, os, sys

# Import non standard modules
from password_generator import PasswordGenerator
from pyfiglet import Figlet

# Declare figelt
f = Figlet(font='slant')
# Render thanks
print(f.renderText('PassMax'))
# Declare version
version = "0.1.0"
# Start the password generator
pwo = PasswordGenerator()
# Filename to store passwords
filename = "pass.txt"
# List of passwords
passwords = []

# Check what platform the user is using
# And declere the correct clear command
if sys.platform == "linux":
    clear_command = "clear"
elif sys.platform == "linux2":
    clear_command = "clear"
elif sys.platform == "darwin":
    clear_command = "clear"
elif sys.platform == "win32":
    clear_command = "cls"

# Try to open file
try:
    # Read passwords from file
    ff = open(filename, "rt")
    # Decode passwords with base64
    passwords_encoded = ff.readlines()
    passwords_encodedStr = str(passwords_encoded)
    passwords_bytes = passwords_encodedStr.encode('ascii')
    final_bytes = base64.b64decode(passwords_bytes)
    final = final_bytes.decode('ascii')
    # Add passwords to list
    passwords.append(final)
    # Close file
    ff.close()
    # Sleep for 2 seconds
    time.sleep(2)
# If file does not exist:
except FileNotFoundError:
    # Print error
    print("No pass.txt found")
    print("Creating pass.txt")
    # Create file
    ff = open(filename, "wt")
    ff.close()
    ff = open(filename, "rt")
    # Add passwords to list
    passwords = ff.readlines()
    # Sleep for 2 seconds
    time.sleep(2)

# Create a new password function
def createPassword():
    # Check if the user wants to create a new password by themselves or by using a random password generator
    print("1-Create a new password by yourself. \n2-Use a random password generator \n3-Custom random password generation")
    # Get user choice
    userChoice = input("Enter your choice: ")
    # If user wants to create a new password by themselves:
    if userChoice == "1":
        # Get password
        newPassword = input("Enter the new password: ")
        # Tell user password is being saved
        print("\nPassword created, saving...")
        # Sleep for 2 seconds
        time.sleep(2)
        # Encode password
        password_encoded = newPassword.encode('ascii')
        password_bytes = base64.b64encode(password_encoded)
        password_finished = password_bytes.decode('ascii')
        # Save password
        passwords.append(password_finished)
        f = open(filename, "at")
        f.write(password_finished)
        f.write("\n")
    # If user wants to use a random password generator:
    elif userChoice == "2":
        # Generate password
        newPassword = pwo.generate()
        # Tell user password is being saved
        print("\nPassword created, saving...")
        # Sleep for 2 seconds
        time.sleep(2)
        # Encode password
        password_encoded = newPassword.encode('ascii')
        password_bytes = base64.b64encode(password_encoded)
        password_finished = password_bytes.decode('ascii')
        # Save password
        passwords.append(newPassword)
        # Save password to file
        f = open(filename, "at")
        f.write(password_finished)
        f.write("\n")
    # If user wants to use a random password generator with custom length:
    elif userChoice == "3":
        # Get length of password
        lengthOfPassword = int(input("Enter the length of the password: "))
        # Set the length of the password in the password generator
        pwo.minlen = lengthOfPassword
        pwo.maxlen = lengthOfPassword
        # Generate password
        newPassword = pwo.generate()
        # Tell user password is being saved
        print("\nPassword created, saving...")
        # Sleep for 2 seconds
        time.sleep(2)
        # Encode password
        password_encoded = newPassword.encode('ascii')
        password_bytes = base64.b64encode(password_encoded)
        password_finished = password_bytes.decode('ascii')
        # Save password
        passwords.append(newPassword)
        # Save password to file
        f = open(filename, "at")
        f.write(password_finished)
        f.write("\n")
    # If user enters something else:    
    else:
        # Tell user to enter 1,2 or 3 the next time
        print("Invalid command, returning to menu")
        time.sleep(2)
        
        

# List passwords function
def listPasswords():
    if passwords == []:
        print("There are no passwords")    
    else:
        print("Here are your passwords")
        # Read passwords from file
        fL = open(filename, "rt")
        passwordRead = fL.readlines()
        passwordReadStr = str(passwordRead)
        base64_bytes = passwordReadStr.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        passwordsImported = message_bytes.decode('ascii')
        passwords.append(passwordsImported)
        # Add a number for every password is printed
        passwordNumber = 1
        passwordNumberString = str(passwordNumber)
        for password in passwords:
            print(f"Password {passwordNumberString}: {password}")
            passwordNumber += 1
            passwordNumberString = str(passwordNumber)

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
        # Encode password
        newPassword_encoded = newPassword.encode('ascii')
        newPassword_bytes = base64.b64encode(newPassword_encoded)
        newPassword_finished = newPassword_bytes.decode('ascii')
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
            f.write(newPassword_finished + "\n")
    elif whatPassToEdit == "L":
        listPasswords()
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
        passwords.remove(whatPassToDelete)
    elif whatPassToDelete == "L":
        listPasswords()
    # If password does not exist:
    else:
        # Tell user password does not exist
        print("Password not found")
        
# Delete all passwords function
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
        passwords.clear()
    # If no:
    else:
        # Say not deleting
        print("Not deleting, returning to normal program")

# Info function
def info():
    # Tell version
    print(f"PassMax version {version}\n")
    # Author
    print("Author: micziz\n")
    # License
    print("License: GNU GPLv3\n")
    # General info
    print("""
PassMax is a password manager that allows you to store your passwords in a secure way and local way!
PassMax is open source. Source code is available at https://www.github.com/micziz/PassMax.  
          """)

# Import passwords from file function 
def importPassword():
    # Steps to import passwords
    print("There are some steps to follow:")
    print("1-Take all passwords you want to import and save them in a file")
    print("Note: All passwords must be on diffrent lines")
    print("2-Rename the file to import.txt")
    print("3-Open PassMax and select Import")
    # Ask for user to confirm
    checkIfStepsFollowed = input("Enter Y if you followed the steps: ")
    # If yes:
    if checkIfStepsFollowed == "Y":
        # Print that you are importing
        print("Importing passwords...")
        # Open file
        fI = open("src/import.txt", "rt")
        # Read file
        importedPasswords = fI.readlines()
        # Append to list
        for passwo in importedPasswords:
            passwords.append(passwo)
        # Add to file
        for importedPassword in importedPasswords:
            with open(filename, "at") as f:
                f.write(importedPassword)

# Export passwords to file function
def exportPassword():
    whatPassToExport = input("Enter the password you want to export: ")
    if whatPassToExport in passwords:
        # Export password
        print("Exporting password...")
        # Open file
        whatPassToExport_encoded = whatPassToExport.encode('ascii')
        whatPassToExport_bytes = base64.b64encode(whatPassToExport_encoded)
        WPTEpassword_finished = whatPassToExport_bytes.decode('ascii') 
        fE = open("src/export.txt", "wt")
        # Write to file
        fE.write(WPTEpassword_finished)
        # Close file
        fE.close()

def exportAllPass():
    fE = open("src/export.txt", "wt")
    for password in passwords:
        passwordEncode = password.encode('ascii')
        password_bytes = base64.b64encode(passwordEncode)
        passwordFinished = password_bytes.decode('ascii')
        fE.write(passwordFinished + "\n")
    print("Exported all passwords")

def commands():
    os.system(clear_command)
    print("Welcome to the commands section! Here you can find all commands you can use in PassMax")
    print("[C]: Create a new password. You can create a password by yourself, or you can use the auto-generator (With Paramaters)")
    print("[L]: List all passwords. You can list all passwords you have saved")
    print("[E]: Edit a password. You can edit a password you have saved")
    print("[D]: Delete a password. You can delete a password you have saved")
    print("[DA]: Delete all passwords. You can delete all passwords you have saved")
    print("[I]: Import passwords. You can import passwords from a file")
    print("[EX]: Export a password. You can export a password to a file")
    print("[EXA]: Export all passwords. You can export all passwords to a file")
    print("[IN]: Info. You can get info about PassMax")
    print("[CM]: Commands. You can get info about all commands you can use in PassMax")
    print("[Q]: Quit PassMax")
    returnToMenu = input("Enter Q to return to the main menu: ")
    if returnToMenu == "Q":
        print("Returning to main menu...")
    else:
        commands()
        

# While loop to keep program running
while True:
    os.system(clear_command)
    # Welcome user
    print("Welcome to PassMax!")
    # Ask user what they want to do
    print("What do you want to do today?")
    # List options
    print("Create Passwords: [C]reate a new password\nImport/Export: [I]mport other files [EX]prot a password [EXA]Export All Passwords\nManage Password: [L]ist all passwords, [E]dit a password\nDeleate Password: [D]elete a password, [DA]Deleate all passwords\nOther: [IN]fo, [CM]Commands [Q]uit: ")
    # Get user input
    whatToDo = input("Enter your choice: ")
    # If user wants to create a new password
    if whatToDo == "C":
        # Call createPassword function
        createPassword()
    # If user wants to import other files
    elif whatToDo == "I":
        # Call importPassword function
        importPassword()
    # if user wants to export a password
    elif whatToDo == "EX":
        exportPassword()
    # If user wants to export all passwords
    elif whatToDo == "EXA":
        exportAllPass()
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
    elif whatToDo == "IN":
        info()
    elif whatToDo == "CM":
        commands()
    elif whatToDo == "Q":
        print("Quitting, goodbye!")
        break
    