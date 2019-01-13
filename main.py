# Project name: QuoteBook
# Description: Allows users to store, save, search and output quotes
# Start Date: December 30th, 2018

import datetime
import time
import random

# A quote will have a index, the words, author, date and category
class Quote(object):
    def __init__ (self, words, author, category):

        self.words = words
        self.author = author
        self.category = category


# TEST quote list:
one = Quote("You only live once.", "Drake", "Philosophy")
two = Quote("When life gives you lemons, make lemonade", "Unknown", "Motivational")
three = Quote("1 + 1 = 2", "Math", "")
four = Quote("qwerty","Key Board", "")
five = Quote("You have to be odd to be number one", "Dr. Seuss","Philosophy")
six = Quote("If you're good at something, never do it for free","Joker","Film")

qlt = [one,two,three,four,five,six]

# Global Variables **********************************************************************************

quote_list = qlt

menu = """
What would you like to do?
-------------------------------
0. Exit Program
1. Get Random Quote
2. Search Quote
3. Add Quote
4. Remove Quote
5. Get All Quotes
"""

categories_list = ["Inspirational", "Motivational", "Positive", "Funny", "Love", "Film", "Philosophy"]

# FUNCTIONS **********************************************************************************
def Search():
    searchInput = input("Search: ")
    newQuotes = SuperFilter(searchInput);
    if not newQuotes:
        return print("No Matches");
    else:
        DisplayList(newQuotes)
        return;
        

def SuperFilter(substring):
    SuperFilteredList = list(filter(lambda x: substring in x.words or substring in x.author or substring in x.category, quote_list))
    return SuperFilteredList;
        

def GetRandom():
    PrintCategories()
    x = input("Choose a category: ")
    if len(quote_list) == 0:
        return print("There are no quotes available.");
    
    elif int(x) == 0:
        rdm = random.randint(0,len(quote_list) - 1)
        print("")
        print(quote_list[rdm].words)
        print("Author: " + quote_list[rdm].author)
        print("Category: " + quote_list[rdm].category)
        return;
    else:
        
        filteredArray = FilterByCategory(categories_list[int(x) - 1])
        
        if len(filteredArray) == 0:
            return print("There are no quotes availible.");
        else:
            rdmIndex = random.randint(0,len(filteredArray) - 1)
            print("")
            print(filteredArray[rdmIndex].words)
            print("Author: " + filteredArray[rdmIndex].author)
            print("Category: " + filteredArray[rdmIndex].category)
            return;

def FilterByCategory(category):
    filtered = list(filter(lambda x: x.category == category, quote_list))
    return filtered;
    

def PrintCategories():
    # Print Categories
    print("""
        
Categories: """)
    print("0. None")
    for i in range(1, (len(categories_list) + 1)):
        print(str(i) + ". " + categories_list[i - 1])
    print(str(len(categories_list) + 1) + ". NEW")
    print("")
    return;
    

def AddQuote():
    w = (input("Enter the quote: "))
    a = (input("Enter the author: "))
    
    # Ask them for categories
    PrintCategories()
    
    userInput = (input("Input: "))

    if (int(userInput) == 0) or (int(userInput) > (len(categories_list) + 1)):
        c = ""

    elif int(userInput) == (len(categories_list) + 1):
        c = NewCategory()
        temp = Quote(w,a,c)
        quote_list.append(temp)
        
        return print("""
            
            Quote Added!""");

    else:
        c = categories_list[int(userInput) - 1]
        
        temp = Quote(w,a,c)
        quote_list.append(temp)
        
        return print("""
            
Quote Added!""");

def NewCategory():
    new = input("New Category: ")
    categories_list.append(new)
    print("Added!")
    return new;


def DisplayList(l):
    for i in range(0, len(l)):
        print("")
        print("Index " + str(i) + ": " + l[i].words)
        print("Author: " + l[i].author)
        print("Category: " + l[i].category)
        print("")
    return;

def RemoveQuote():
    index = int(input("""
        
Enter the index of the quote you would like to remove: """))
    if (index >= 0) and (index < len(quote_list)):
        quote_list.pop(index)
        return print("Quote removed!");
    else:
        return print("Invalid Index");


#START MENU: **********************************************************************************

print(menu)
option = int(input("""

Enter a option: """))

while option != 0:
    

    if option == 1:
        GetRandom()
        input()
        print(menu)
        option = int(input("""

Enter a option: """))
    
    elif option == 2:
        Search()
        input()
        print(menu)
        option = int(input("""

Enter a option: """))
    
    elif option == 3:
        AddQuote()
        input()
        print(menu)
        option = int(input("""

Enter a option: """))
    
    elif option == 4:
        RemoveQuote()
        input()
        print(menu)
        option = int(input("""

Enter a option: """))
        
    
    elif option == 5:
        if not quote_list:
            print("-----------------------------------------")
            print("There are no quotes in your book :(")
            print("-----------------------------------------")
            input("")
            print(menu)
            option = int(input("Enter a option: "))
        else:
            print("-----------------------------------------")
            print ("There are currently " + str(len(quote_list)) + " quote(s)!")
            DisplayList(quote_list)
            print("-----------------------------------------")
            input("")
            print(menu)
            option = int(input("""

Enter a option: """))

    elif option > 5:
        print("Invalid Option, Try Again.")
        input()
        print(menu)
        option = int(input("""

Enter a option: """))

else:
    print("Goodbye!")
    quit()






        
    

    

        


