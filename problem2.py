# 2. Python Data Structure Challenges in Real-World Scenarios

# Task 1: Library System Enhancement
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book():
    try:
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
    except:
        print("Invalid input. Please try again.")
        return
    #end try
    
    if (title, author) in library:
        print("The book is already in the library.")
    else: 
        library.append((title, author))
        print("The book has been added to the library.")
    #end if
#end function

add_book()