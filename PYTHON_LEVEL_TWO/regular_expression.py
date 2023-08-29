### Example 1
import re

patterns = ['term1','term2']

text = 'This is a string with term1, not not the other!'

for pattern in patterns:
    print("I'm searching for: "+pattern)

    if re.search(pattern,text):
        print("MATCH!")
    else:
        print("NOT MATCH!")

### Example 2 Special regular Expression match object
import re
text = 'This is a string with term1, not not the other!'

match = re.search('term1',text)

# print(type(match))
print(match.start())

## Example 3 We can split string as well
import re
split_term = '@'

email = 'user@gmail.com'

print(re.split(split_term,email))
# print(match.start())

Example 4 Lots of time we have to look at the lot more complex pattern.

import re
print(re.findall('match','test phrase match in match middle'))

# Example 5 metacharacter syntax

import re
def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for patterns {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

# test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dsssss...sddddd'
# test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_phrase = 'This is a string with numbers 12312 and a symbol #hashtag'

test_patterns = ['sd*']  # followed by zero or more
# test_patterns = ['sd+'] # followed by one or more
test_patterns = ['sd?']  # followed by either zero or one
test_patterns = ['sd{1,3}'] # in curly bracket you can define actual number or list of number
test_patterns = ['s[sd]+'] # s is followed by either one or more s or d

# Below this use the test_pharse which actually have a valid sentences and comment the ssdd one
test_patterns = ['[^!.?]+'] # Exclusion ^ --> to find the punctuation.
test_patterns = ['[a-z]+'] # for only lower case character
test_patterns = ['[A-Z]+'] # For only Upper Case Character

# use 3rd test_phrase to run the below function
test_patterns = [r'\d+'] #lower case d is essential for to search the digits
test_patterns = [r'\D+'] # Upper case D is for the character
test_patterns = [r'\s+'] # For all the whitespace
test_patterns = [r'\S+'] # For all the non-whitespace
test_patterns = [r'\w+'] # For all the alpha numeric character
test_patterns = [r'\W+'] # For all the non-alpha numeric

multi_re_find(test_patterns,test_phrase)


