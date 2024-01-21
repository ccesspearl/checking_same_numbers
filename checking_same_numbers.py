# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False. 

# Pseudocode 

# Create a check function 
def check(given_list): 

# Inside the function, create a print syntax that will show the given list 
    print("Given list:", given_list)

# Inside the function, use the return syntax 
    return given_list[0] == given_list[-1]

# Create a variable for given list and check it 
result = check([1,2,3,4,1])

# Print the result 
print("result is", result)

# Create a variable for given list and check it 
result2 = check([3,6,8,0,1])

# Print the result 
print("result is", result2)