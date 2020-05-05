def read_grades(gradefile):
    line=gradefile.readline()
    while line!='\n':
        line=gradeline.readline()


    grade_to_ids={}

    line=gradefile.readline()

    while line!='':
        student_id=line[:4]
        grade=float(line[4:].strip())

        if grade not in grade_to_ids:
            grade_to_ids[grade]=[student_id]
        else:
            grade_to_ids[grade].append(student_id)
    
        line=gradefile.readline()
    return grade_to_ids

        
def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    '''
  
    result = []
    for k in L:
       if k in d:
          result.append(k)

    return result


def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool
  
    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    '''

    result = True
    for i in range(len(L1)):
       if L1[i]!=len(L2[i]):
            result = False

    return result

def double_values(collection):
    for v in range(len(collection)):
         collection[v] = collection[v] * 2

def get_diagonal_and_non_diagonal(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):
            if row == col:
                diagonal.append(L[row][col])
            elif row != col:
                non_diagonal.append(L[row][col])         
            

            # CODE MISSING HERE

    return (diagonal, non_diagonal)


def count_chars(s):
    '''(str) -> dict of {str: int}

    Return a dictionary where the keys are the characters in s and the values
    are how many times those characters appear in s.

    >>> count_chars('abracadabra')
    {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
    '''
    d = {}

    for c in s:
        if not (c in d):
            d[c]=1
        else:
            d[c] = d[c] + 1

    return d

def smaller_of_largest(L1, L2):
    '''(list of int, list of int) -> int

    Return the smaller of the largest value in L1 and the large    st value inL2.

    Precondition: L1 and L2 are not empty.

    >>> smaller_of_largest([1, 4, 0], [3, 2])
    3
    >>> smaller_of_largest([4], [9, 6, 3])
    4
    '''

    return min(max(L1),max(L2))
def count_values_that_are_keys(d):
    '''(dict) -> int

    Return the number of values in d that are also keys in d.
   
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
    3
    >>> count_values_that_are_keys({1: 1})
    1
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
    2
    >>> count_values_that_are_keys({1: 2})
    0
    '''

    result = 0
    for k in d:
        if k in d:
             result = result + 1

    return result

def add_to_letter_counts(d, s):
    '''(dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values
    are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.

    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    >>> letter_counts
    {'i': 1, 'r': 6, 'e': 4}
    '''

    for c in s:
        d[c]=d[c]+1
        
