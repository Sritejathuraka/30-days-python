## ** Strings ** ##
'''A string is sequence of characters enclosed in quotes'''

# Declare strings
single_quote = 'Please Subscribe'
double_quote = "it's a video"
triple_quote = ''' A string is sequence of
 characters enclosed 
 in quotes '''

# How to access characters in string
text = 'python'

## How to Slice string
slice_text = 'programming'
slice_text[:5]
slice_text[5:]
slice_text[::-1]

# strings operations in python

# concatenation
text1 = ' I '
text2 = ' love '
text3 = ' python '
result = text1 + text2 + text3

# repetition
multi_text1 = 'Hello '

multi_result  = multi_text1 * 5

# Membership
text = 'python programming'
result = 'java' in text

# string methods in python

method_text = "Hello programmer"
print('UPPER CASE', method_text.upper())
print('Lower CASE', method_text.lower())
print('replace text', method_text.replace('programmer','python'))

#split and joining strings
words = method_text.split()
join =  "_".join(words)

# count occurences
count_text = 'banana'
count_letter = count_text.count('n')
print('counted letter', count_letter )

#checking start and end
checking_text = "hello py"
start_check = checking_text.startswith('0hel')
end_check = checking_text.endswith(' py')
print("starts with", start_check)
print("ends with", end_check)