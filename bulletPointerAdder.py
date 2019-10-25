# Adds bullter points to each individula wikepedia list items
# Gets it from the clipboard then pastes it back into the clipboard

#   The module where we can copy and paste into the clipboard
import pyperclip

#   Gets the clipboard and pastes it into the function
text = pyperclip.paste()

# TODO: Seperate lines and add stars below
# Splits the lines into a new line, \n equals new line
lines = text.split('\n')

# Loop through all the lines
for sentence in range(len(lines)):
    # Adds a star to each string
    lines[sentence] = "• " + lines[sentence]
# Joins each line as a whole string
text = '\n'.join(lines)

# Now, copies the manipuated string into your clipboard
pyperclip.copy(text)
