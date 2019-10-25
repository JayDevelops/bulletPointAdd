import pyperclip

def destinedArgument():
    # Ask the user for the desired text manipulation they want
    print("Please be aware your text needs to be copied in your computer's clipboard before running this program\n")
    print("Please input the desired text manipulation you desire: ")
    print("Your choices are the following: \n 'Uppercase' \n 'Lowercase' \n 'Capitalize")
    userInput = input()

    #Gets the user's clipboard text and pastes it into pyperclip
    text = pyperclip.paste()

    # TODO: Seperate each line into a different line, as the pyperclip string thinks it's only one line
    lines = text.split('\n')

    textValue = ""

    def stringManpulation(textValue):
        for sentence in range(len(lines)):
            lines[sentence].textValue()

    if userInput == "uppercase" or userInput == "Uppercase":
        textValue = "uppercase"
        stringManpulation(textValue)
    elif userInput == "lowercase" or userInput == "Lowercase":
        textValue = "lower"
        stringManpulation(textValue)
    elif userInput == "capitalize" or userInput == "Capitalize":
        textValue = "capitalize"
        stringManpulation(textValue)
    else:
        print("please input a valid answer next time, run the program again")


    #Now the manipulated text is added back to the user's clipboard
    pyperclip.copy(text)

#calls the function below
destinedArgument()
