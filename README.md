# Python Django Internship
## Contents
Following are the contents to be covered during this internship:
- Python Programming
- Relational Databases (PostgreeSQL)
- Django
- Django Rest Framework
- Project
## OOP

## REAL WORLD PROBLEM 1
### File: 01_Designing_Browser_History.py
This program implements a simple browser history. The BrowserHistory class has three methods: __init__, visit, and back. The __init__ method initializes the browser history with the homepage. The visit method adds a new URL to the history and clears the forward history. The back method returns the URL that was visited steps steps ago. The forward method returns the URL that was visited steps steps forward.

To run the program, you can save it as a .py file and then run it from the command line. I saved this file  as 01_Designing_Browser_History.py. so I can run it using command
python 01_Designing_Browser_History.py

## REAL WORLD PROBLEM 2
### File:  02_Destinatiom_City.py
The FindDestinationCity class has one method, destination_city. This method takes a list of lists as input, where each inner list represents a path between two cities. The method then creates a dictionary to store the number of outgoing paths for each city. For example, if the input list contains the paths ["Jhang", "Faisalabad"], ["Faisalabad", "Sheikhupura"], ["Sheikhupura", "Lahore"]], then the dictionary will have the following entries:
{
    "Jhang": 1,
    "Faisalabad": 1,
    "Sheikhupura": 0,
    "Lahore": 0
}
The method then iterates over the dictionary and returns the city with no outgoing paths. In the example above, the city with no outgoing paths is Lahore, so the method will return "Lahore".
The print statement in the code prints the dictionary so that you can see the number of outgoing paths for each city This is helpful for debugging the code.

To run the program, you can save it as a .py file and then run it from the command line. I saved this file  as 02_Destinatiom_City.py. so I can run it using command
python 02_Destination_City.py


## REAL WORLD PROBLEM 3
### File:  03_Minimum_Cost_to_Travel.py
The MinimumTravlellingCost class has one method, twoCitySchedMinCost. This method takes a list of lists as input, where each inner list represents the cost of traveling from one city to another. The method then sorts the list by the difference between the first and second costs, so that the list is sorted in ascending order of the difference between the costs. For example, if the input list contains the costs [[34, 45], [23, 8], [12, 36], [67, 45]], then the sorted list will be [[12, 36], [34, 45], [23, 8], [67, 45]].

The method then iterates over the sorted list and adds the first cost to the total cost if the index is less than half of the length of the list, and adds the second cost to the total cost if the index is greater than or equal to half of the length of the list. This ensures that the total cost is the minimum possible cost of traveling to two cities.
The print statements in the code print the original list and the sorted list so that you can see the results of the sorting.

To run the program, you can save it as a .py file and then run it from the command line. I saved this file  as 03_Minimum_Cost_to_Travel.py. so I can run it using command
python 03_Minimum_Cost_to_Travel.py

## REAL WORLD PROBLEM 4
### File:  04_Max_Coins.py
The CoinPiles class has one method, maxCoins. This method takes a list of integers as input, where each integer represents the number of coins in a pile. The method then sorts the list in descending order, so that the largest pile is at the end of the list. The method then iterates over the list and adds the middle coin from each group of three consecutive piles to the total number of coins. For example, if the input list contains the numbers [11, 23, 3, 344, 55, 67], then the method will add the following coins to the total:

The middle coin from the first group of three piles, which is 23.
The middle coin from the second group of three piles, which is 55.
The middle coin from the third group of three piles, which is 67.
The method then returns the total number of coins.
The print statements in the code print the sorted list and the total number of coins so that you can see the results of the computation.

To run the program, you can save it as a .py file and then run it from the command line. I saved this file  as 04_Max_Coins.py. so I can run it using command
python 04_Max_Coins.py


## REAL WORLD PROBLEM 5
### File:  05_deck_of_cards.py
I first define two classes here Card and Deck. The Card class represents a single card in a deck of cards. The Deck class represents a deck of cards. The Deck class has methods to build a deck of cards, shuffle the deck, draw a card from the deck, and show the deck.

The program then defines a Player class. The Player class represents a player in a card game. The Player class has methods to draw a card from the deck, show the player's hand, and discard a card from the player's hand.

The program then creates a Deck object and a Player object. The Player object is named umair. The program then calls the draw method on the umair object three times to draw three cards from the myDeck object. The showHand method is then called on the umair object to show the player's hand. The discard method is then called on the umair object to discard one of the cards from the player's hand. The showHand method is then called again to show the player's hand.

The program then calls the discard method on the umair object again to discard another card from the player's hand. The showHand method is then called one last time to show the player's hand.

To run the program, you can save it as a .py file and then run it from the command line. I saved this file  as 05_deck_of_cards.py. so I can run it using command
python 05_deck_of_cards.py

  
## Getting Started
1. Clone the repository.
2. Run the programs using Python 3.

## Contributing
Contributions are welcome! I'd like the respected CEO to check my programs and guide me accordingly.
