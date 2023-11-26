from string import digits, ascii_lowercase, ascii_uppercase
from random import choice



new_code = 'code'
# all = 
new_code = ''.join(choice(digits + ascii_uppercase + ascii_lowercase) for i in range(12))
print(new_code)