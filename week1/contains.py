def contains(value, lst):
    """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested        lists in lst.

   >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   """

    found = False
# We have not yet found value in the list.

 # CODE MISSING HERE
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True
    return found

def lines_startswith(file, letter):
    """ (file open for reading, str) -> list of str

     Return the list of lines from file that begin with letter.     The lines should have thenewline removed.

    Precondition: len(letter) == 1
    """

    matches = []
# CODE MISSING HERE
   matches.append(line.startswith(letter).rstrip('\n'))
    return matches

def mysty(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:
            matches = matches + 1

    return matches == (len(s) // 2)
