import random  # to append variables and values and things

answers = []
score = []

h1 = "Erase the roots of economic suffering"
h2 = "secure nourishment from field to fork"
h3 = "safeguard lives through care and prevention"
h4 = "unlock minds through lifelong learning"
h5 = "balance the scales for all identities"
h6 = "turn the tap for dignity and hygiene"
h7 = "power progress with sustainability"
h8 = "drive opportunity without exploitation"
h9 = "build smarter and connect further"
h10 = "narrow the divides within and beyond borders"
h11 = "rethink urban life for resilience"
h12 = "consume wisely and produce sustainably"
h13 = "defend the future from rising threats"
h14 = "shield the blue world beneath"
h15 = "guard the green and all who dwell there"
h16 = "stand for fairness and fight corruption"
h17 = "link efforts for global progress"

c1 = "No poverty"
c2 = "Zero poverty"
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

allHints = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15 ,h16, h17]
corrections = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17]

print("Welcome to the SDG guessing game!")
print("The goal of this game is to guess what each SDG is based on the hint provided.")
print("You will get your score at the end of the game and if you failed or passed.")
print("If you want to exit the game write 'END' Good luck!")

while answers != 'END':
    for _ in range(17):
        print("Here is your hint: ", [allHints])
        input("Guess the SDG name: ")

