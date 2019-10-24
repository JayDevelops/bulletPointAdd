# Adds bullter points to each individula wikepedia list items
# Gets it from the clipboard then pastes it back into the clipboard

 #The module where we can copy and paste into the clipboard
import pyperclip

#Gets the clipboard and pastes it into the function
text = pyperclip.paste()

#TODO: Seperate lines and add stars below
lines = text.split('\n') #Splits the lines into a new line, \n equals new line

for sentence in range(len(lines)): #loop through all the lines
    lines[sentence] = "• " + lines[sentence] #Adds a star to each string

text = '\n'.join(lines) #Joins each line as a whole string

#Now, copies the manipuated string into your clipboard
pyperclip.copy(text)
