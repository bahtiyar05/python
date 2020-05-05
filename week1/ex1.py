def sum(a,b):
    '''(number,number) ->number
    Returns sum of two numbers 
    '''
    return a+b

def convert_to_celsius(fahrenheit):
    '''(number)-> number
    >>>convert_to_celsius(32)
    0
    >>>convert_to_celsius(212)
    100    
    '''
    return (fahrenheit - 32 )* 5 / 9

