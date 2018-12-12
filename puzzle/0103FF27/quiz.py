import codecs as c

quiz_name = "Famous People in Computing"
questions = [["Who invented the World Wide Web?", ["Steve Jobs", "John Von Neumann", "Sir Tim Berners-Lee", "Bill Gates"]],
             ["Who co-founded Apple?", ["Jobs and Wozniak", "Braben and Bell", "Brin and Page", "Gates and Allen"]],
             ["Who has been called the world's first computer programmer?", ["Bill Gates", "Sir Tim Berners-Lee", "Ada Lovelace", "Grace Hopper"]],
             ["Which mathematician invented Boolean Logic in the mid-1800s?", ["George Boole", "Isaac Newton", "Leonhard Euler", "John von Neumann"]],
             ["Who dropped out of Harvard to focus on starting up Facebook?", ["Steve Jobs", "Linus Torvalds", "Sir Clive Sinclair", "Mark Zuckerberg"]],
             ["Who invented the Analytical Engine and is considered to be the father of computing?", ["Steve Wozniak", "Charles Babbage", "Alan Turing", "Tommy Flowers"]]
            ]
a0 = "210203"
a1 = "251034"

s = 0

def display_question(question, answers, correct):
    print()
    print(question)
    print()
    for i in range(len(answers)):
        print(str(i + 1) + ".", answers[i])
    print()
    print("Answer by entering a number.")


def get_choice(num_answers):
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option selected: "))
            if 1 <= choice <= num_answers:
                option_valid = True
            else:
                print("Please enter a valid choice")
        except ValueError:
            print("Please enter a valid choice")
    return choice


def output(x):
    return((c.decode('Gel ntnva.', 'rot_13') * x) + (c.decode('Cnffpbqr RS27NO66', 'rot_13') * (not x)))

def run_quiz():
    global s
    print("=" * len(quiz_name))
    print(quiz_name)
    print("=" * len(quiz_name))
    for i in range(len(questions)):
        display_question(questions[i][0],questions[i][1],a0[a1.index(str(i))])
        option = get_choice(len(questions[i][1]))
        print()
        if option == int(a0[a1.index(str(i))]) + 1:
            print("CORRECT")
            s += 1
        else:
            print("WRONG")
    print()
    print("Quiz completed.")
    print("You scored", str(s), "out of", str(len(questions))+".")
    print(output(s % (36 ** 0.5) != 0 or s  == 0))


run_quiz()

