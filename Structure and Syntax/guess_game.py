print("---GUESSING GAME---")
guess = ""
secret_word = "giraffe"
guess_count = 0

while guess != secret_word and guess_count < 3:
    guess = input("Enter guess: ")
    guess_count +=1
    print("This is your " + str(guess_count) +" try")

if guess == secret_word:
    print("You win")
elif guess_count >= 3:
    print("Out of tries")
else:
    print("An error occured")