def collect_vowels(s):
    '''(str) -> str
    >>>collect_vowels('Happy Anniversary')
    'aAiea'

    '''
    vowels = ''
    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels+char
    return vowels


def count_vowels(s):
    '''(str) -> int
    Return th number of vowels in string
    
    >>>count_vowels('Happy day!'
    2

    '''
    num_vowels = 0
    
    for char in s:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1
    return num_vowels


message = 'Happy 29th!'
new_message = ''

for char in message:
    if char.isdigit():
        new_message = new_message + str((int(char) + 1) % 10)
    else:
        new_message = new_message + char

print(new_message)
