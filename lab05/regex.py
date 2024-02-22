#1

import re

pattern = 'ab*'
test_string = input()

if re.search(pattern, test_string):
    print("Match found!")
else:
    print("No match found.")


#2
    
import re

pattern = 'ab{2,3}'
test_string = input()

if re.search(pattern, test_string):
    print("Match found!")
else:
    print("No match found.")


#3

import re

pattern = '[a-z]+_[a-z]+'
test_string = input()

matches = re.findall(pattern, test_string)
print(matches)


#4

import re

pattern = '[A-Z][a-z]+'
test_string = input()

matches = re.findall(pattern, test_string)
print(matches)


#5

import re

pattern = 'a.*b$'
test_string = input()

if re.match(pattern, test_string):
    print("Match found!")
else:
    print("No match found.")


#6
    
import re

pattern = '[\s,\.]'
test_string = input()

new_string = re.sub(pattern, ':', test_string)
print(new_string)



#7

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

snake_case_string = input()
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)



#8

import re

pattern = '[A-Z][a-z]*'
test_string = input()

matches = re.findall(pattern, test_string)
print(matches)



#9

import re

pattern = '(?<!^)(?=[A-Z])'
test_string = input()

new_string = re.sub(pattern, ' ', test_string)
print(new_string)


#10

def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

camel_case_string = input()
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)
