#function to find the average of two numbers
def average_of_two_numbers(x,y):
    average = 0
    for value in x,y:
        average += value/(2)
    return average
print(average_of_two_numbers(90,40))

#ii)
#Allow User input and finding the minimum number
css_mark = int(input("enter css mark"))
java_mark = int(input("enter java mark"))
html_mark = int(input("enter html mark"))

if css_mark < java_mark and css_mark < html_mark:
    print(f"{css_mark} is the minimum number")
elif java_mark < css_mark and java_mark < html_mark:
    print(f"{java_mark} is the minimum number")
else:
    print(f"{html_mark} is the minimum number")