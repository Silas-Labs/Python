try:
    number = int(input("Enter a number: "))
    print(number/0)
except: # But this is too broad
    print("Invalid input")

print("-Concise Error Handling--")
try:
    number = int(input("Enter a number: "))
    divisor = int(input("Enter a number: "))
    print(number/divisor)
except ZeroDivisionError: # Dvision by 0 error
    print("Division by 0")
except ValueError: # Wrong Value
    print("Invalid input")
except:
    print("Some other error")