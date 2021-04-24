#In this file, we will showcase some examples of running the number_2_word function
#First, we will use the test cases provided in the brief
# Then, We will use a sub-sample of a wide range of random numbers from 1 - 999,999,999,999
# Then, We will also use an example ".txt" file as well called "example_sentence_file.txt"
# Then, We'll input a string number as well.
# Lastly we will include some examples of invalid inputs 

### import the necessary modules ###
from number_2_words.number_map import number_map
from number_2_words.number_word_constructor import construct_number_word, run_number_words
from number_2_words.number_2_word import number_2_word


### Example 0: use the test cases provided in the brief ###

test_case_1 = "The pump is 536 deep underground."

number_2_word(test_case_1)


test_case_2 = "We processed 9121 records."

number_2_word(test_case_2)


test_case_3 = "Variables reported as having a missing type #65678."

number_2_word(test_case_3)


test_case_4 = "Interactive and printable 10022 ZIP code."

number_2_word(test_case_4)


test_case_5 = "The database has 66723107008 records."

number_2_word(test_case_5)


test_case_6 = "I received 23 456,9 KGs."

number_2_word(test_case_6)




### Example 1: Random Sample of 150 numbers ranging from 1 - 999,999,999,999 ####

import numpy as np

np.random.seed(42)

#random sample of 25 numbers between 1 - 100
one_to_hundred = []
for i in range(25):
    one_to_hundred.append(np.random.randint(1,100))

#random sample of 25 numbers between 101 - 1,000
hundred_to_thousand = []
for i in range(25):
    hundred_to_thousand.append(np.random.randint(101,1000))

#random sample of 25 numbers between 1,001 - 99,999
tens_of_thousands = []
for i in range(25):
    tens_of_thousands.append(np.random.randint(1001,99999))

#random sample of 25 numbers between 100,000 - 999,999
hundreds_of_thousands = []
for i in range(25):
    hundreds_of_thousands.append(np.random.randint(100000,999999))

#random sample of 25 numbers between 1,000,000 - 999,999,999
millions = []
for i in range(25):
    millions.append(np.random.randint(1000000,999999999))

#random sample of 25 numbers between 1,000,000,000 - 999,999,999,999
billions = []
for i in range(25):
    billions.append(np.random.randint(1000000000,999999999999))

#Join them all together into one big list of 150 random numbers
random_sample = one_to_hundred + hundred_to_thousand + tens_of_thousands + hundreds_of_thousands + millions + billions


for i in random_sample:
    print(i, ":", number_2_word(i))



### Example 2: An example ".txt" file ###

file_name = "Examples/example_sentence_file.txt"

number_2_word(file_name)


### Example 3: An example str number ###

number_2_word("983475")

number_2_word("The answer to the ultimate question of life, the universe and everything is 42")


### Example 4: Invalid Input Examples ###

number_2_word(960.32)  

number_2_word("1,000,000") 

number_2_word(-67) 

number_2_word("j0hn") 

number_2_word("36 789") 

number_2_word("$785")

number_2_word("Examples/invalid_file_example.txt")

