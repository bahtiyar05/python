import tkinter.filedialog
import grade1
al_filename="grades.txt"
al_file=open(al_filename,'r')


al_histfilename="history.hist"
al_histfile=open(al_histfilename,'w')
# Read the grades into a list
grades = grade1.read_grades(al_file)

print(grades)
# Count the gradesper range
range_counts=grade1.count_grade_ranges(grades)

print(range_counts)

    
# Write the histogram to the file


al_file.close()
al_histfile.close()
