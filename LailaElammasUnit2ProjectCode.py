import random  # to append variables and values and things

answers = []
score = []

h1 = "Erase the roots of economic suffering"
h2 = "Secure nourishment from field to fork"
h3 = "Safeguard lives through care and prevention"
h4 = "unlock minds through lifelong learning"
h5 = "Balance the scales for all identities"
h6 = "Turn the tap for dignity and hygiene"
h7 = "Power progress with sustainability"
h8 = "Drive opportunity without exploitation"
h9 = "Build smarter and connect further"
h10 = "Narrow the divides within and beyond borders"
h11 = "Rethink urban life for resilience"
h12 = "Consume wisely and produce sustainably"
h13 = "Defend the future from rising threats"
h14 = "Shield the blue world beneath"
h15 = "Guard the green and all who dwell there"
h16 = "Stand for fairness and fight corruption"
h17 = "Link efforts for global progress"

c1 = "No poverty"
c2 = "Zero hunger"
c3 = "Good health and well being"
c4 = "Quality education"
c5 = "Gender equality"
c6 = "Clean water and sanitation"
c7 = "Affordable and clean energy"
c8 = "Decent work and economic growth"
c9 = "Industry, innovation and infrastructure"
c10 = "Reduced inequality"
c11 = "Sustainable cities and communities"
c12 = "Responsible consumption and production"
c13 = "climate action"
c14 = "life below water"
c15 = "life on land"
c16 = "Peace, justice and strong institutions"
c17 = "Partnership for the goals"

allHints = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17]
corrections = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17]

print("Welcome to the SDG guessing game!")
print("The goal of this game is to guess what each SDG is based on the hint provided.")
print("You will get your score at the end of the game and if you failed or passed.")
print("If you want to exit the game write 'END' Good luck!")
print(" ")
print(" ")

playAgain = "Yes"

while playAgain != 'No':
    for hintIndex in range(len(allHints)):
        print("Here is your hint: ", allHints[hintIndex])
        answer = input("Guess the SDG name: ")
        answers.append(answer)
        if answer != corrections[hintIndex]:
            print("Your answer is incorrect")
            print("The correct answer is ", corrections[hintIndex])
            score.append('incorrect')
        elif answer == corrections[hintIndex]:
            print("Your answer is correct")
            score.append('correct')
        if answer == 'END':
            break

    if score.count('incorrect') >= 8:
        print("You failed the quizz")
        playAgain = input("Would you like to play again to get a higher score?")
    else:
        print("You passed the quizz")
        print("Here are your results: ")
        print(" ")
        print(score)
        print(answers)
