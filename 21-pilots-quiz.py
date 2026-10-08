# Twenty One Pilots Quiz Game

questions = ("What is the name of the fictional city ruled by the bishops, where the band's lore takes place?: ",
             "How many bishops rule Dema?: ",
             "What is the name of the protagonist who tries to escape from Dema?: ",
             "Which character represents Tyler's insecurities and gives its name to the 2015 album?: ",
             "What is the name of the religion created by the bishops to control the people of Dema?: ",
             "What is the name of the resistance group that opposes the bishops?: ",
             "Which color marks the Trench era and the Banditos' visual identity?: ",
             "The anagram of \"Scaled and Icy\", a lore clue from 2021, forms which phrase?: ",
             "What is the name of Dema's leading bishop, who appears in the title of a Trench song?: ",
             "In what year was the album Clancy released?: "
             )
options = (("A. Nico", "B. Dema", "C. Vialism", "D. Banditos"),
           ("A. Five", "B. Seven", "C. Nine", "D. Twelve"),
           ("A. Clancy", "B. Nico", "C. Blurryface", "D. Ned"),
           ("A. Clancy", "B. Nico", "C. Blurryface", "D. Keons"),
           ("A. Vialism", "B. Denialism", "C. Dematism", "D. Nicoism"),
           ("A. The Niners", "B. The Vialists", "C. The Trenchers", "D. The Banditos"),
           ("A. Red", "B. Yellow", "C. Blue", "D. Green"),
           ("A. Dema Is Fallen", "B. Nico Is Alive", "C. Clancy Is Dead", "D. Trench Is Home"),
           ("A. Keons", "B. Nico", "C. Andre", "D. Clancy"),
           ("A. 2018", "B. 2021", "C. 2015", "D. 2024"))
answers =("B", "C", "A", "C", "A", "D", "B", "C", "B", "D")
guesses = []
score = 0
question_num = 0

print("---------------------------------------")
print("Welcome to Twenty One Pilots Lore Quiz")
print("---------------------------------------")

for question in questions:
    print("---------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("---------------------------------------")
        print("Correct!")
    else:
        print("---------------------------------------")
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1

print("---------------------------------------")
print("               RESULTS                 ")
print("---------------------------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
