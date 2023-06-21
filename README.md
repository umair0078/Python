# Python Django Internship
## Contents
Following are the contents to be covered during this internship:
- Python Programming
- Relational Databases (PostgreeSQL)
- Django
- Django Rest Framework
- Project
## DAY 1
## Python Introduction and Flow Control
This repository contains programs demonstrating basic concepts of Python and flow of control.
- [Program 1](01_data_types.py): I already know about python datatypes therefore I have just write some comments and revised them.

- [Program 2](02_Dictionary.py): This program creates a dictionary called `d` and assigns it some key-value pairs.It then prints the contents of the dictionary, using different methods to access the values.

- [Program 3](03_dict_pr.py): This program first defines an empty dictionary called `fav_lang`.It then prompts the user to enter their favorite language and stores their input in the dictionary.

- [Program 4](04_list.py): List is very important concept in Python and in this file I proved that it is mutable and unhashable data type.

- [Program 5](05_list_methods.py): In this file I have applied important methods on list.

- [Program 6](06_tuple.py): In this file I revised the tuple and its methods as we know tuple is an immutable and hashable datatype and a tuple with single value will create using using a comma after that value i., (4,) , otherwise it will be treated as an integer.

- [Program 7](07_set.py): In this file I show that a set is an unordered collection of unique items. It is unindexed and we cannot repeat values in a set.An ampty set will create using set(). we cannot add list and dictionary inside a set becaue the are unhashable. I also used some set methods here.

- [Program 8](08_namespace.py): First, I use multi-line comment for the covenience then, I show that what how we the vriables are in global, local and nested global namespace.

- [Program 9](09_is and ==.py): In this file I show that is used to check if two values are located on the same part of the memory and and == compares the values, if the are exaclty equal to each other or not.

- [Program 10](10_global keyword.py): The first line of the program defines a global variable called a and assigns it the value 10. The second line defines a function called my_func(). The function my_func() defines a local variable called a and assigns it the value 20. The function then prints the value of the local variable a.The third line of the program calls the function my_func(). The fourth line defines a function called func_2(). The function func_2() uses the global keyword to access the global variable a and assigns it the value 50. The function then prints the value of the global variable a.The last line of the program prints the value of the global variable a.
  
- [Program 11](11_concatination.py): This program first defines two strings, `a` and `b`, and then combines them with the string representation of the integer `c`.
It then prints the message and prompts the user to enter their name.

- [Program 12](12_if_statement.py): The control will go inside the if statement only if the given condition is true otherwise it will print nothing.

- [Program 13](13_if_else_statement.py): The control will go go inside if statement if the given condition is true otherwise it will go inside the else block.

- [Program 14](14_Grade_Calculation.py): This program takes the user's marks as input and then prints their grade.The grade is determined using a series of if-elif statements.

- [Program 15](15_greatest_number.py): This program first takes the four numbers as an input from the user in integer form and then it first compares the first two numbers and the greater number is stored in f1 as a result, then it compares next two numbers and the result of greatest number will store in f2 as a result and then finally, it compares the f1 and f2 and we will get the greatest number.

- [Program 16](16_practice_problem.py): This program first takes the name of the user as an input and I have created a list. Then I used the condition, if name is present in the list it will print "Your name is present in the list", otherwise it will print "Your name is not present in the list".
  
- [Program 17](17_practice_problem2.py): This program first takes the favourite fruit of the user as an input and I have created a list of fruits. Then I used the condition, if fruit entered by the user is present in the list it will print "Yes, it is present"", otherwise it will print "It is not present".

- [Program 18](18_practice_problem3.py): This program prints those fruits present in the list which starts with "B" or "b".

- [Program 19](19_spam_detector.py): This program detects the spam based on the text entered by the user.

- [Program 20](20_input.py): In this program we use the built-in input function which takes the input from the user and prints the result.The input function by default takes the input in string then we have to typecast it according to our requirements.

- [Program 21](21_string_methods.py): In this program I applied the some important built-in methods on string.

- [Program 22](22_string_slicing.py): In this program I sliced the string in various ways.

- [Program 23](23_type_conversion.py): In this program we typecast the integer into sting because we cannot concatinate an integer into a string.

- [Program 24](24_while_loop.py): In this file I used while loop 3 times for my revision it runs as long as the given condition is true.

- [Program 25](25_for_loop.py): This program first defines a list called `numbers` that contains the numbers from 1 to 9.
It then prints the numbers in the list using three different for loops.The range() function returns a sequence of numbers, starting from 1 and ending at 9 (not including 10). The second for loop will print the numbers from from 1 to 20 and it will skip the two numbers and then prints the third number because range is "range(1,21,3).

## REAL WORLD PROBLEM 1
### File: 1_REAL_World_Problem_1.py
### Problem Statement: If an employee comes office after 9:30 A.M, deduct 1.5% salary of that employee.
- First I created a class Employee and a constructor inside this class which takes two parameters name and salary.
- I created class variables self.name and self.salary inside this constructor.
- Then, I created a function "deduct_if_late", which deducts 1.5% salary of an employee if he comes office after 9:30 A.M.
- Inside this function I created "arrival_time" variable,it stores the current time in the format %I:%M:%S %p, which is hour:minute:second AM/PM and time_deadline stores the time 9:30 AM in the same format.
- Then, I write the condition if arrival_time is greater than time_deadline then deduct 1.5% of the salary.
- I created two objects "Asad" and "Amjad" of the Employee class and call the function on these objects separately.
- As a result,the salary of Employees is deducting 1.5% if the comes late.


## REAL WORLD PROBLEM 2
### File: 1_REAL_World_Problem_1.py
### Problem Statement: Calculate the total runs scored by a batsman in an innings
- First, I take the total_score variable and assign 0 as value to it.
- I use the while loop and this loop will continue to run until the programmer explicitly stops it using the break statement.
- In every Iteration It will display "Enter 'out' to stop" which I have printed and takes score as an input from the user.
- The input function takes the input as a string so I used string method lower() here here.
- If the user Enter 'out' in either uppercase or lowercase the loop will stop iterating beacuse of break statement and total_score of the player will print.
- The try: keyword marks the beginning of the try block.
- The int() function tries to convert the value of the variable score to an integer.
- The total_score += score statement adds the value of score to the variable total_score.
- The except: keyword indicates the beginning of the except block.
- The ValueError keyword specifies the type of exception in case of invalid value that the except block will handle.
- The print() statement prints the message "Invalid Input! Please Enter a valid score".


  

## Getting Started
1. Clone the repository.
2. Run the programs using Python 3.

## Contributing
Contributions are welcome! I'd like the respected CEO to check my programs and guide me accordingly.
