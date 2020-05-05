def count_adjacent_repeats(s):


    repeats=0

    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            repeats=repeats+1
    return repeats


def count_adjacent_repeats1(s):
    repeats1 = 0
    for i in range(len(s)):
        if s[i] == s[i + 1]:
             repeats1 = repeats1 + 1
    return repeats1



def shift_left(L):
    '''(list) - >NoneType


    '''
    first_item=L[0]
    
    for i in range(1,len(L)):
        L[i-1]=L[i]

    L[-1]=first_item
    


def sum_items(list1,list2):
    sumlist=[]
    for i in range(len(list1)):
        sumlist.append(list1[i]+list2[i])
    return sumlist



def count_matches(s1,s2):
    num_matches=0
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            num_matches+=1
    return num_matches

