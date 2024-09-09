# 1. Tuple Mastery in Python

# Task 1: Formatting Flight Itineraries
def format_itenerary(flights):
    result = ""
    for index in range(len(flights)):
        name, origin, destination = flights[index]
        result += f"Itenerary {index + 1}: {name} - From {origin} to {destination}\n"
    #end for
    return result
#end function

flights = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"), ("Charlie", "Shanghai", "New York")]
print(format_itenerary(flights))