
import time

Trials = ["Riddle Me This", "Puzzle Time", "Trivia Time", "Flex That Logic", "Math"]
challenge = 1
puzzle = 1
tt = 1

def initiation(ans):
    complete = 0
    if ans == 'yes':
        complete = 1
    if ans == 'y':
        complete = 1
    if ans == 'Y':
        complete = 1
    if ans == 'Yes':
        complete = 1
    if ans == 'no':
        print("Too bad, you have to anyway")
        complete = 1
    if ans == 'No':
        print("Too bad, you have to anyway")
        complete = 1
    if ans == 'n':
        print("Too bad, you have to anyway")
        complete = 1
    if ans == 'N':
        print("Too bad, you have to anyway")
        complete = 1
    elif complete == 0:
        print("I need a vaild answer")
        ans = input("Do you want to play a game?")
        initiation (ans)
def riddle(challenge):
    if (challenge == 1):
        answer = input("David's father has three sons : Snap, Crackle and _____ ?")
        if answer == 'David':
            print("Correct")
            challenge += 1
            riddleMeThis(challenge)
        else:
            print("Need a valid answer")
            riddle(challenge)
        riddleMeThis()
    if (challenge == 2):
        answer = input("What room do ghosts avoid?")
        if answer == 'living room':
            print("Correct")
            challenge += 1
            riddleMeThis(challenge)
        elif():
            print("Need a valid answer")
            riddle(challenge)
        riddleMeThis(challenge)
    if (challenge == 3):
        answer = input("What belongs to you, but other people use it more than you?")
        if answer == 'your name':
            print("Correct")
            challenge += 1
            riddleMeThis(challenge)
        elif():
            print("Need a valid answer")
            riddle(challenge)
        riddleMeThis(challenge)
def riddleMeThis(challenge):
    if challenge == 4:
        print("Riddle Me This chanllenges cleared")
        Trials.remove("Riddle Me This")
        ultimateChoice()
    if challenge !=4:
        print("Riddle Me This: Challenge ")
        print(challenge)
        riddle(challenge)
def puzzleTest(puzzle):
    if (puzzle == 1):
        answer = input("0001 1010 0100 in base 10")
        if answer == '420':
            print("Correct")
            puzzle += 1
            puzzleTest(puzzle)
        else:
            print("Need a valid answer")
            puzzleTest(puzzle)
        puzzleTime(puzzle)
    if (puzzle == 2):
        answer = input("1101 1110 1010 1101 in base 16")
        if answer == 'DEAD':
            print("Correct")
            puzzle += 1
            puzzleTest(puzzle)
        elif():
            print("Need a valid answer")
            puzzleTest(puzzle)
        puzzleTime(puzzle)
    if (puzzle == 3):
        answer = input("FDHVDU        Key: 3")
        if answer == 'Caesar':
            print("Correct")
            puzzle += 1
            puzzleTest(puzzle)
        elif():
            print("Need a valid answer")
            puzzleTest(puzzle)
    if (puzzle > 3):
        puzzleTime(puzzle)
def puzzleTime(puzzle):
    if puzzle == 4:
        print("Puzzle Time puzzles cleared")
        Trials.remove("Puzzle Time")
        ultimateChoice()
    if puzzle !=4:
        print("Puzzle Time: Puzzle ")
        print(puzzle)
        puzzleTest(puzzle)

def triv(tt):
    if (tt == 1):
        answer = input("Name of the world's biggest island")
        if answer == 'Greenland':
            print("Correct")
            tt += 1
            triv(tt)
        else:
            print("Need a valid answer")
            triv(tt)
        triviaTime(tt)
    if (tt == 2):
        answer = input("How many bones are in the human body")
        if answer == '206':
            print("Correct")
            tt += 1
            triv(tt)
        elif():
            print("Need a valid answer")
            triv(tt)
        triviaTime(tt)
    if (tt == 3):
        answer = input("Melting point of Steel in Fahrenheit")
        if answer == '2500':
            print("Correct")
            tt += 1
            triv(tt)
        elif():
            print("Need a valid answer")
            triv(tt)
    if (tt > 3):
        triviaTime(tt)
def triviaTime(tt):
    if tt == 4:
        print("Trivia Time facts answered")
        Trials.remove("Trivia Time")
        ultimateChoice()
    if tt !=4:
        print("Trivia Time: Trivia ")
        print(tt)
        triv(tt)

def ultimateChoice():
     choice = input(Trials)
     print('\n')
     complete = 0
     if choice == 'Riddle Me This':
        riddleMeThis(challenge)
        complete = 1
     if choice == 'Puzzle Time':
        puzzleTime(puzzle)
        complete = 1
     if choice == 'Trivia Time':
        triviaTime(tt)
        complete = 1
     if choice == 'Flex that Logic':
        flexThatLogic()
        complete = 1
     if choice == 'Math':
        math()
        complete = 1
     elif complete == 0:
        print("I need a vaild answer")
        ultimateChoice()



def flexThatLogic():
    print("Flex That Logic" '\n')

def math():
    print("Math" '\n')


print("Hello")
time.sleep(2) 
ans = input("Do you want to play a game?" '\n')
initiation(ans)

print("In order to get out of this safetly you will need to complete some tasks.")
time.sleep(2)
print("Choose one on these games, beat three and you win." '\n' '\n')

ultimateChoice()