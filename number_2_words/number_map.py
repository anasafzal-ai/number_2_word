#this nested dictionary maps all the necessary values needed to make up any number word. 
# Each sub-dictionary represents the relevant mapping to the structure of number words. 

number_map = {'singles': {
     '0': 'zero',
     '1':'one', 
     '2':'two', 
     '3': 'three',
     '4':'four',
     '5':'five',
     '6':'six',
     '7': 'seven',
     '8': 'eight',
     '9': 'nine'},

     'doubles': {
     '10': 'ten', 
     '11': 'eleven', 
     '12': 'twelve', 
     '13': 'thirteen', 
     '14': 'fourteen', 
     '15':'fifteen', 
     '16': 'sixteen', 
     '17': 'seventeen', 
     '18': 'eighteen', 
     '19': 'nineteen'},

     'tens': { 
     '20': 'twenty', 
     '30': 'thirty', 
     '40':'forty', 
     '50': 'fifty',
     '60': 'sixty', 
     '70': 'seventy',
     '80': 'eighty', 
     '90': 'ninety', 
     '100': ' hundred'},

     'endings': {
     'empty': '', 
     '1000':' thousand', 
     '1000000': ' million', 
     '1000000000':' billion'}
}
