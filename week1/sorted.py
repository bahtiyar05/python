file=open("text.txt",'r')
sorted_list=[]
sorted_list=file.readlines()
#readlines  reads all the lines of a file and assigns it to a list! That's great!
'''
line=file.readline()
while line!='':
    sorted_list.append(line)
    line=file.readline()
'''
file.close()
sorted_list.sort()
print(sorted_list)

file=open("result.txt",'w')
for line in sorted_list:
    file.write(line)

file.close()

              
