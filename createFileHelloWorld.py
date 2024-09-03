# This program:
# Opens a file 'hello.txt",
# Stores message "Hello World!" into the file.
# Closes the file.
# Re-opens the file;
# Reads message into string and prints it.


def writeFile():
    # Open a file with the name hello.txt
    myFile = open('hello.txt', 'w')
    # Store the message "Hello World!" in the file.
    myFile.write("Hello World!")
    # Close the file.
    myFile.close()
    # Report close successful.
    print("File closed succssfully. ")
    print(" ")


writeFile()


def readFile():
    # Open the same file.
    myFile = open('hello.txt', 'r')
    # Read the message into a string variable.
    for line in myFile:
        # Print as string by default.
        print(line)
    # Close the file.
    myFile.close()
    

readFile()
