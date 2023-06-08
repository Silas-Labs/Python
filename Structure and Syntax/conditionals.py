is_male = False
is_tall = False

#IF
print("----IF start---")
if is_male:
    print("You're a male")
if is_male and is_tall:
    print("Tall male")

if is_male or is_tall:
    print("Either tall or Male or both")
elif not(is_male) and not(is_tall):
    print("Not a tall male")

print("----IF end---")