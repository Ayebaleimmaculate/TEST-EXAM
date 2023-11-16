# sum of items in a list
student_marks=[78,83,90,88,75]
def sum_of_items(student_marks):
    total_mark = 0
    for x in student_marks:
        total_mark += x
    return total_mark
print(f"the sum of the items in the student marks list is {sum_of_items(student_marks)}")

#displaying the first and last mark in the list
first = student_marks[0]
last = student_marks[4]
print(f"the fist mark is {first}, and the last mark is {last}")

#add 96 to the the list
student_marks.append(96)
print(student_marks)

#updating the student mark of 78 to 87
student_marks[0] =87
print(student_marks)