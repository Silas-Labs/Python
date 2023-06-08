# WHILE
print("---WHILE start---")
i = 1
while i <= 10:
    print(i)
    i+=1
print("---WHILE end---")

# FOR
print("-- FOR START--")
for letter in "Giraffe Academy":
    print(letter)

print("--2--")
friends = ["Caleb","Manu","Shalom"]
for friend in friends:
    print(friend)
    
print("--3--")
for friend in range(len(friends)):
    print(friends[friend])

#a range of numbers upto but not including 10
print("--4--")
for index in range(10):
    print(index)

#range of numbers from 3 to 9
for index in range(3,10):
    print(index)