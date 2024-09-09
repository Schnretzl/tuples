# 1. Tuple Mastery in Python

# Task 1: Formatting Flight Itineraries
def format_itenerary(flights):
    result = ""
    for index in range(len(flights)):
        result += f"Itenerary {index + 1}: {flights[index][0]} - From {flights[index][1]} to {flights[index][2]}\n"
    #end for
    return result
#end function

flights = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"), ("Charlie", "Shanghai", "New York")]
print(format_itenerary(flights))