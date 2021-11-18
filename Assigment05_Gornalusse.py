# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# German Gornalusse, 11.16.2021, Added code to complete assignment 5
# German Gornalusse, 11.17.2021, Modified code after reviewing class materials
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFileName = "ToDoFile.txt"  # An object that represents a file. I removed the path here so the code works in different computers.
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
readFile = open(objFileName, "r")
for row in readFile:
    strData = row.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
readFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("="*30)
        print("To do list showings Tasks and Priorities")
        for row in lstTable:
            print(row["Task"]+ '|'+ row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("="*30)
        print("Now you will be enter a dyad Task and Priority!")
        inputTask= input(str("Please enter a Task: "))
        inputPriority = input(str("Please enter a Priority: "))
        dicRow = {"Task": inputTask, "Priority": inputPriority}
        lstTable.append(dicRow)
        print("=" * 30)
        print("To do list showings Tasks and Priorities")
        for row in lstTable:
            print(row["Task"] + '|' + row["Priority"])
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        taskToRemove = str(input("Which Task would you like to remove:  ?"))
        # This part is at a much higher than I can understand and didn't want to copy paste from the Answer so I left it incomplete
        # I did not understand how to remove an item either from the video either
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(objFileName, "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Thank you and good bye!")
        break  # and Exit the program
