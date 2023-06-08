from Questions import Questions

question_prompts = [
    "What color are Apples? \n(a)Red/Green\n(b)Purple\n(c)Orange\n\n",
    "What color are Bananas? \n(a)Teal\n(b)Magenta\n(c)Yellow\n\n",
    "What color are Strawberries? \n(a)Yellow\n(b)Red\n(c)Blue\n\n"
]

questions = [
    Questions(question_prompts[0],"a"),
    Questions(question_prompts[1],"c"),
    Questions(question_prompts[2],"b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        user_answer = input(question.prompt)
        if question.answer == user_answer:
            score += 1
    print("You Scored "+str(score)+"/"+str(len(questions)) )

print(run_test(questions))