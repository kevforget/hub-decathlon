BLACK_COLOR="\u001b[30m"
def black(stringToColor):
	return BLACK_COLOR + str(stringToColor) + RESET_COLOR

RED_COLOR="\u001b[31m"
def red(stringToColor):
	return RED_COLOR + str(stringToColor) + RESET_COLOR

GREEN_COLOR="\u001b[32m"
def green(stringToColor):
	return GREEN_COLOR + str(stringToColor) + RESET_COLOR

YELLOW_COLOR="\u001b[33m"
def yellow(stringToColor):
	return YELLOW_COLOR + str(stringToColor) + RESET_COLOR

BLUE_COLOR="\u001b[34m"
def blue(stringToColor):
	return BLUE_COLOR + str(stringToColor) + RESET_COLOR

MAGENTA_COLOR="\u001b[35m"
def magenta(stringToColor):
	return MAGENTA_COLOR + str(stringToColor) + RESET_COLOR

CYAN_COLOR="\u001b[36m"
def cyan(stringToColor):
	return CYAN_COLOR + str(stringToColor) + RESET_COLOR

WHITE_COLOR="\u001b[37m"
def white(stringToColor):
	return WHITE_COLOR + str(stringToColor) + RESET_COLOR

RESET_COLOR="\u001b[0m"
def reset(stringToColor):
	return RESET_COLOR + str(stringToColor) + RESET_COLOR



# If you want to add other colors (i.e. the "bright ones")
# Go there : https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

# Copy paste the codes you want like this :
# Black: \u001b[30m
# Red: \u001b[31m

# Then research for this regex :
# ([A-Za-z]*): (\\u001b\[\d*m)

# And replace by this
# \U$1_COLOR="$2"\ndef \L$1(stringToColor):\n\treturn \U$1_COLOR + str(stringToColor) + RESET_COLOR\n
