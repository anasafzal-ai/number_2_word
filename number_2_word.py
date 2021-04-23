
#import the 2 functions that constructs the number to word and runs it 
from number_word_constructor import construct_number_word, run_number_words

def number_2_word(number):

    """
    Valid input is either: 
    (1) int value from Plain text file (no special characters within substring int value)
    (2) int value from string number (no special characters within substring int value)
    (3) int value from actual number (no float)

    """

    if isinstance(number, str) and ".txt" in number:

        txt_file = open(number, "r+")

        string_without_lines = ""
        for line in txt_file:
            strip_line = line.rstrip()
            string_without_lines += strip_line

        s = string_without_lines


        number = str([int(char) for char in s.split() if char.isdigit()])[1:-1]

        if number == '':
            return "Invalid Input"

        else:
            return run_number_words(number)

    elif isinstance(number, str):

        number = str([int(char) for char in number.split() if char.isdigit()])[1:-1]

        if number == '':
            return "Invalid Input"
        
        else:
            return run_number_words(number)

    elif isinstance(number, int) and number > 0:
        
        return run_number_words(number)

    else:
        return "Invalid Input."





