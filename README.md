# Python Django Internship
## Contents
Following are the contents to be covered during this internship:
- Python Programming
- Relational Databases (PostgreeSQL)
- Django
- Django Rest Framework
- Project
## Python Introduction and Flow Control
# Problem 1
## Real World Problems
This repository contains programs demonstrating basic concepts of Python and flow of control.
- # Real_world_problem_1.py:
- ## Suppose, a student wants to pass an exam. He requires minumum 33 marks to pass that exam. He will sit in exam again and again until he gets 33 or above marks.
- The exam() function takes a number of marks as input and prints a message based on the marks.
   If the marks are less than 33, the function calls itself again with the marks increased by 1. This continues until the marks are 33 or more, at which point the function 
     prints a message congratulating the user on passing the exam.
    If the marks are not a number, the function prints an error message.
  
# Problem 2
- # 2_Real_world_problem_2.py:
- ## Program checks you are hungry or not. if you are hungry then a fastfood menu will display and you have to pick the item from the menue. When You order the item then show you a message that "Your order has been placed successfully".
- 1. The menu() function prints a menu of fast food items that the user can order.
2. The function takes the user's order as input and checks if it is a valid number.
3. If the order is valid, the function prints a message thanking the user for their order.
4. If the order is not valid, the function prints an error message and asks the user to enter a valid number.
5. The while True loop ensures that the menu is displayed repeatedly until the user enters "No".
6. The status variable is used to store the user's input.
7. The if statement checks if the user's input is "Yes" or "No".
8. If the user's input is "Yes", the menu() function is called.

# Problem 3
- # Meeting_Rooms.py
- ## We are given an input array of meeting time intervals, intervals, where each interval has a start time and an end time.Find the minimum number of meeting rooms required to hold these meetings.
- 1. The Arrange_Meetings class has a minMeetingRooms() function that takes an array of meeting time intervals as input.
2. The function first sorts the intervals by their start time.
3. Then, it initializes a heap to store the end times of the meetings.
4. The function then iterates through the intervals and checks if the start time of the current meeting is greater than or equal to the end time of the meeting at the top of the heap.
5. If it is, the function pops the meeting at the top of the heap.
6. Otherwise, the function pushes the end time of the current meeting to the heap.
7. The function returns the number of meetings in the heap.

## Getting Started
1. Clone the repository.
2. Run the programs using Python 3.

## Contributing
Contributions are welcome! I'd like the respected CEO to check my programs and guide me accordingly.
