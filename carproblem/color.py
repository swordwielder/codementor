# generateSecretCode(colorList): a function that received a list of colors then
# generates and returns a random secret color code (as a list). Use
# random.randint(0, 5) to get a number between 0 and 5 inclusive, which you
# can then map to one of the colors of in colorList.
# computeExactMatches(computerColorList, playerColorList): a
# function that compares the secret color code with player’s guess and returns the
# number of exact matches (e.g.: correct colors in the right position).
# computePartialMatches(computerColorList, playerColorList): a
# function that compares the secret color code with player’s guess and returns the
# number of partial matches (e.g.: correct colors that are in the wrong position).
colors = 4

def generateSecretCode(colorList):
    