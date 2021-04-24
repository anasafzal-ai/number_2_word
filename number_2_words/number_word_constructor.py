#KEY ASSUMPTIONS:
# (1) NO NEGATIVE NUMBERS
# (2) NUMBER CANNOT EXCEED 12-DIGITS
# (3) NO DECIMAL POINTS
# (4) ONLY NUMERICAL DATA IS VALID, FUNCTION WILL INVALIDATE ANY NUMBER CONTAINING LETTERS OR SPECIAL CHARACTERS
# (5) FUNCTION CAN ACCEPT STRING NUMBER "1234", INT NUMBER 1234, OR READ PLAIN TEXT FILE AND GRAB NUMBER FROM FILE IF AVAILABLE
# (6) FILES ACCEPTED ARE ONLY PLAIN-TEXT FILES (.TXT) 



from number_2_words.number_map import number_map

def construct_number_word(number, index):

    number = str(number)

    if number == '0':
        return 'zero'

    num_length = len(number)

    #want to ensure that each 'block' has 3 values, since we want to break up potential 12-digit number into sections of 3. So if it's 3 => 003 if it's 31 => 031 if it's 256 => 256 etc.

    if num_length % 3 == 1:                     #i.e. if distance to the nearest multiple of 3 is 2 (1,4,7,10)
        number = number.zfill(num_length + 2)
    elif num_length % 3 == 2:                   #i.e. if distance to the nearest multiple of 3 is 1 (2,5,8,11)
        number = number.zfill(num_length + 1)
    else:
        number = number                         #i.e. if distance to the nearest multiple of 3 is 0 (3,6,9,12)


    number_word = '' #begin as empty string, this is the string you're going to populate iteratively and turn into the word you need

    #breaking up the 3-value block (left -> right in the string, e.g. 665231 -> (665))
    hundreds_element = int(number[0])
    tens_element = int(number[1])
    singles_element = int(number[2])

    number_word += number_map.get('singles').get(str(hundreds_element)) if number[0] != '0' else ''  #add the first number word
    number_word += number_map.get('tens').get('100') if number_word != '' else '' #add the ending "hundred" if there is a number otherwise just ''

    #the next problem is the issue of the second element i.e. 'tens' or 'doubles', specifically whether the value is =10, >10, or 0. In each case, there needs to be an appropriate response. 
    if tens_element == 1: #if the value is in the doubles (10-19)
        number_word += ' and ' + number_map.get('doubles').get(str((10)+ singles_element)) if hundreds_element != 0 else number_map.get('doubles').get(str((10)+ singles_element)) #if the hundreds digit is not 0, (e.g. 123) and add in an "and" in between them so "one hundred *and* twenty-three"

    elif tens_element > 1: #if the value is in the tens (20s-90s)
        number_word += number_map.get('tens').get(str(tens_element * 10)) if hundreds_element == 0 else ' and ' + number_map.get('tens').get(str(tens_element * 10))
        number_word += '-'
        number_word += number_map.get('singles').get(str(singles_element))

    elif tens_element == 0: #if the value is in the singles (0 - 9)
        number_word  += number_map.get('singles').get(str(singles_element)) if hundreds_element == 0 else ' and ' + number_map.get('singles').get(str(singles_element)) 

    if number_word.endswith('and zero'):  #deal with instances when we have zero at the end
        number_word = number_word[:-len('and zero')]
    elif number_word.endswith('zero'):
        number_word = number_word[:-len('-zero')]
    else:
        number_word += ''

    if not len(number_word) == 0:    
        number_word += list(number_map.get('endings').values())[index]

    return number_word



def run_number_words(number):

    number = str(number)

    num_length = len(number)

    if num_length > 12:

        return "Invalid Input."
    
    else:

        count = num_length // 3 if num_length % 3 == 0 else num_length // 3 + 1 #count the number of 'blocks' or commas there will be (e.g. a million = 3 because {1},{000},{000})
        copy = count
        number_word = [] #have a empty list that you're going to append each 'block' to 

        for i in range(num_length - 1, -1, -3):
            number_word.append(construct_number_word(str(number)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))  #here, we are appending to the list each finished 'block' of 3 digits (000) in our number using our function and looping through the index
            count -= 1 #run it down till we've covered the entire index

        number_word = [i for i in number_word if i != ''] #remove all empty string values from the list, this will help with the formatting of including commas in the final number word

        for index, value in enumerate(number_word): #if there is a block that is between 0-9 and the number is bigger than one block i,e. 1000 or greater then add "and" to the single value
            if value in list(number_map.get('singles').values()) and len(number_word) > 1:
                number_word[index] = ' and ' + value 

            elif 'thousand' not in value and 'million' not in value and 'billion' not in value and 'hundred' not in value and len(number_word) >=2: #if the value is between 10s-90s and there are more than 1 blocks then add an "and"
                number_word[index] = ' and ' + value
                
            
            #since the final block does not have a comma (e.g. sixty-six billion, seven hundred and twenty-three million, one hundred and seven thousand and eight) we need to format the final value to ensure there is no comma there but in all the other blocks
        if len(number_word) == 1:
            final_number_word = "".join(number_word[::-1])
        else:
            number_first = ", ".join(number_word[::-1][:-1])
            number_last = "".join(number_word[::-1][-1]) if number_word[::-1][-1].startswith(" and") else ", " + "".join(number_word[::-1][-1])
            final_number_word = number_first + number_last
        
        return final_number_word


