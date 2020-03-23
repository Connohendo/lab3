# Programming Lab 3 code

# Fibonacci example module code

def fib(n):         # Write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()
    
    
def fib2(n):        # Return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
    
# Checks if a string is a palindrome
def palindrome(string):
    print(string)           # Prints the entered word for a referral 
    reverse = string[::-1]  # Reverses the entered word using list functions and sets the output as "reverse"
    if reverse == string:   # Checks if reverse is equal to the original input 
        print("You have entered a palindrome.") # Prints the result aswell as reverse to show the final product 
        print(reverse)
    if reverse != string:   # Checks if reverse is not equal to string(original input) the prints the result aswell as final prduct
        print("Your entry is not a palindrome.")
        print(reverse)


