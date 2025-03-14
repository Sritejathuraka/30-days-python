## ** Basic Programming **
'''  *** Topics covered ***
        . Variables and Datatypes
        . Input and Output
        . Operators
        . Conditional Statements 
'''
## ** Programming one **
''' *** Basic Caluculator *** '''
num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
choose_operation = int(input('''Enter 0 for Addition
Enter 1 for Subtraction
Enter 2 for Multiplication
Enter 3 for Division
Enter 4 for Modulus
Enter 5 for Floor Division
Enter 6 for Exponentiation
Choose here: 
'''))
if choose_operation == 0:
    print(f'Addition of {num1} and {num2} is: ', num1 + num2)
elif choose_operation == 1:
    print(f'Subtraction of {num1} and {num2} is: ', num1 - num2)
elif choose_operation == 2:
    print(f'Multiplication of {num1} and {num2} is: ', num1 * num2)
elif choose_operation == 3:
    print(f'Division of {num1} and {num2} is: ', num1 / num2)
elif choose_operation == 4:
    print(f'Modulus of {num1} and {num2} is: ', num1 % num2)
elif choose_operation == 5:
    print(f'Floor Division of {num1} and {num2} is: ', num1 // num2)
elif choose_operation == 6:
    print(f'Exponentiation of {num1} and {num2} is: ', num1 ** num2)
else:
    print(f'Entered invalid number, Choose 0 to 6 only')

## ** Programming two **
''' *** Basic Grading system *** '''
# Taking student name and grade as input
student_name = input("Enter Student Name: ")
student_grade = int(input("Enter Student Grade: "))

# Checking the grade and assigning the respective grade category
if student_grade > 90:
    print(f'{student_name} got A+')

elif student_grade >= 85 and student_grade <= 90:  ## ✅ Pythonic way: 85 <= student_grade <= 90
    print(f'{student_name} got A')

elif student_grade >= 75 and student_grade < 85:  ## ✅ Pythonic way: 75 <= student_grade < 85
    print(f'{student_name} got B+')

elif student_grade >= 65 and student_grade < 75:  ## ✅ Pythonic way: 65 <= student_grade < 75
    print(f'{student_name} got B')

elif student_grade >= 55 and student_grade < 60:  ## ✅ Pythonic way: 55 <= student_grade < 60
    print(f'{student_name} got C')

elif student_grade >= 40 and student_grade < 55:  ## ✅ Pythonic way: 40 <= student_grade < 55
    print(f'{student_name} got D')

elif student_grade < 40:
    print(f'{student_name} Failed, Better luck next time')

else:
    print(f'Entered invalid details')
