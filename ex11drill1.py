print("Here's another form")

print("Tell me your favorite number between 1 and 10:", end=' ')

number = int(input())

print("This is your number:  ", number)

number2 = int(input("Here's another way to prompt for a number:  "))

print("This is your second number:  {}".format(number2))


print("\nAnd now for my favorite exercise!\nAverage the grades!")

grade1 = float(input('Please enter the first grade: '))
grade2 = float(input('Please enter the second grade: '))
grade3 = float(input('Please enter the third grade: '))
grade4 = float(input('Please enter the fourth grade: '))
grade5 = float(input('Please enter the fifth grade: '))

grade_average = (grade1 + grade2 + grade3 + grade4 + grade5) / 5

print(f"The average of {grade1}, {grade2}, {grade3}, {grade4}, and {grade5} is {grade_average}.")
