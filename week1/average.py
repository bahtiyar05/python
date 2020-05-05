def calculate_average(asn_grades):
    '''(list of list)


    '''
    total=0

    for item in asn_grades:
        total=total+item[1]

    return total/len(asn_grades)
#--------------------------------------------------------
def find_average(l):

    average=[]
    for number in l:
        total=0
        for items in number:
            total=total+items
        average.append(total/len(number))              
    return average  
