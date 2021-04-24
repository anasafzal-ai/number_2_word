# number_2_word
- This project looks at converting any number to it's word variant (i.e. 1 -> "one")
- Due to the intuitive structure of the mapping system as well as the functions, if in the future changes needed to be made (such as increasing valid range to the trillions, or allowing negative numbers, or even removing the conjunctions) it is very easy to do so. 
- Also, as the functions are seperated by what key role they play in converting a number to a word, de-bugging is incredibly easy (even if we apply Eagleson's Law!)

# ASSUMPTIONS - There are several key assumptions held in this project:
- Number cannot exceed 12-digits.
- Number can only be positive.
- Number must be an integer.
- Valid inputs include ".txt" files, integer, and string containing a valid integer. 
- String must contain a valid number (e.g. "1234") and cannot have inside of it a non-number (e.g. "#1234" or "1,2,3,4" or "1234." are all invalid.)  
- ".txt" file can contain non-numbers as long as it is not inside the number (valid: "I am 25 years old", invalid: "I am 25-years old")
- ".txt" file only contains one valid number otherwise invalid input. (valid: "253000 Kilos", invalid: "25 3,000 Kilos")

# INSTRUCTIONS - To run the scripts successfully and use the function, you must:
- Have all the files in the same directory - you can do this by either cloning the repository or downloading the zip. 
- If using a ".txt" file, ensure that it is either in the same directory or properly pathed.
- The function that should ultimately be run is the "number_2_word()" function from the "number_2_word.py" file.
- To immediately see test cases and examples in using the number_2_word() function, please check the "Examples.py" file.

# EXAMPLES & TEST CASES- To see some examples of this function working:
- Run the "Examples.py" file. 
- Ensure you have all the necessary scripts, as well as all the files in the Examples folder, this can be done by cloning the repository or downloading the entire project.
