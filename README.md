# number_2_word

This project looks at converting any number to it's word variant (i.e. 1 -> "one")

There are several key assumptions held in this project:
- Number cannot exceed 12-digits.
- Number can only be positive.
- Number must be an integer
- Valid inputs include ".txt" files, integer, and string of integer. 
- String must contain a valid number and cannot have inside of it a non-number (e.g. "#1234" or "1,2,3,4" or "1234." are all invalid.)  
- ".txt" file can contain non-numbers as long as it is not inside the number (valid: "I am 25 years old", invalid: "I am 25-years old")

To run the scripts successfully and use the function, you must:
- Have all the files in the same directory.
- If using a ".txt" file, ensure that it is either in the same directory or properly pathed.
- The function that should ultimately be run is the "number_2_word()" function from the "number_2_word.py" file.
- To run this function outside of the script, simply run "from number_2_word import number_2_word" into a new file in the same directory - simple as that!
