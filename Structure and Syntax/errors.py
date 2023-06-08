try:
    number = int(input("Enter a number: "))
    print(number)
except: # But this is too broad
    print("Invalid input")

print("-Concise Error Handling--")
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError: # Dvision by 0 error
    print("Invalid input")
except ValueError: # Wrong Value
    print("Invalid input")
except:
    print("Some other error")