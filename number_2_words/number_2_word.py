
#import the number to word map and 2 functions that constructs the number to word and runs it 
from number_2_words.number_map import number_map
from number_2_words.number_word_constructor import construct_number_word, run_number_words

def number_2_word(number):

    """
    Valid input is either: 
    (1) int value from Plain text file (no special characters within substring int value)
    (2) int value from string (no special characters within substring int)
    (3) int value from actual number (no float)

    """

    if isinstance(number, str) and ".txt" in number:  #dealing with .txt files

        txt_file = open(number, "r+")

        #if .txt file has lines, remove them and make the string one line
        string_without_lines = ""
        for line in txt_file:
            strip_line = line.rstrip()
            string_without_lines += strip_line

        s = string_without_lines

        #only keep the valid number from the string
        valid_number = str([int(char) for char in s.split() if char.isdigit()])[1:-1]

        if valid_number == '':
            return "Invalid Input"
        
        all_numbers = "".join([char.replace(' ', '') for char in s if char.isdigit()])

        if valid_number == all_numbers:
            return run_number_words(valid_number)
        else:
            return "Invalid Input"


    elif isinstance(number, str):

        valid_number = str([int(char) for char in number.split() if char.isdigit()])[1:-1]

        if valid_number == '':
            return "Invalid Input"
        
        all_numbers = "".join([char.replace(' ', '') for char in number if char.isdigit()])

        if valid_number == all_numbers:
            return run_number_words(valid_number)
        else:
            return "Invalid Input"


    elif isinstance(number, int) and number > 0:
        
        return run_number_words(number)


    else:
        return "Invalid Input."




