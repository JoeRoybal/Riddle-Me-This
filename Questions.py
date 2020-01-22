
import time
import sys


Trials = ["Riddle Me This", "Puzzle Time", "Trivia Time", "Flex That Logic", "Math"]
challenge = 1
puzzle = 1
tt = 1
logic = 1
problem = 1


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
    if ans == 'ex1t':
        sys.exit("END GAME")
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
        if answer == 'ex1t':
            sys.exit("END GAME")
        else:
            print("Need a valid answer")
            riddle(challenge)
        riddleMeThis()
    if (challenge == 2):
        answer = input("You have a single match and are in a pitch black room with a candle, an oil lamp, and a gas stove. Which do you light first?")
        if answer == 'match':
            print("Correct")
            challenge += 1
            riddleMeThis(challenge)
        if answer == 'ex1t':
            sys.exit("END GAME")
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
        if answer == 'ex1t':
            sys.exit("END GAME")
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
        if challenge == 1:
            print("""\
         :::::::::  ::::::::::: :::::::::  :::::::::  :::        ::::::::::          :::   :::   :::::::::: 
        :+:    :+:     :+:     :+:    :+: :+:    :+: :+:        :+:                :+:+: :+:+:  :+:         
       +:+    +:+     +:+     +:+    +:+ +:+    +:+ +:+        +:+               +:+ +:+:+ +:+ +:+          
      +#++:++#:      +#+     +#+    +:+ +#+    +:+ +#+        +#++:++#          +#+  +:+  +#+ +#++:++#      
     +#+    +#+     +#+     +#+    +#+ +#+    +#+ +#+        +#+               +#+       +#+ +#+            
    #+#    #+#     #+#     #+#    #+# #+#    #+# #+#        #+#               #+#       #+# #+#             
   ###    ### ########### #########  #########  ########## ##########        ###       ### ##########       
       
          ::::::::::: :::    ::: ::::::::::: :::::::: 
             :+:     :+:    :+:     :+:    :+:    :+: 
            +:+     +:+    +:+     +:+    +:+         
           +#+     +#++:++#++     +#+    +#++:++#++   
          +#+     +#+    +#+     +#+           +#+    
         #+#     #+#    #+#     #+#    #+#    #+#     
        ###     ###    ### ########### ########       

        """)
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
        if answer == 'ex1t':
            sys.exit("END GAME")
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
        if answer == 'ex1t':
            sys.exit("END GAME")
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
        if answer == 'ex1t':
            sys.exit("END GAME")
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
        if puzzle == 1:
            print("""\
                     _        _        _        _        _        _        _        _        _        _    
                   _( )__   _( )__   _( )__   _( )__   _( )__   _( )__   _( )__   _( )__   _( )__   _( )__ 
                 _|     _|_|     _|_|     _|_|     _|_|     _|_|     _|_|     _|_|     _|_|     _|_|     _|
                (_ P _ (_(_ U _ (_(_ Z _ (_(_ Z _ (_(_ L _ (_(_ E _ (_(_ T _ (_(_ I _ (_(_ M _ (_(_ E _ (_ 
                  |_( )__| |_( )__| |_( )__| |_( )__| |_( )__| |_( )__| |_( )__| |_( )__| |_( )__| |_( )__|                                                                                                                                                                      
                              """)
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
        if answer == 'ex1t':
            sys.exit("END GAME")
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
        if answer == 'ex1t':
            sys.exit("END GAME")
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
        if answer == 'ex1t':
            sys.exit("END GAME")
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
        if tt == 1:
            print("""
             /$$$$$$$$        /$$            /$$                 /$$$$$$$$ /$$                        
            |__  $$__/       |__/           |__/                |__  $$__/|__/                        
               | $$  /$$$$$$  /$$ /$$    /$$ /$$  /$$$$$$          | $$    /$$ /$$$$$$/$$$$   /$$$$$$ 
               | $$ /$$__  $$| $$|  $$  /$$/| $$ |____  $$         | $$   | $$| $$_  $$_  $$ /$$__  $$
               | $$| $$  \__/| $$ \  $$/$$/ | $$  /$$$$$$$         | $$   | $$| $$ \ $$ \ $$| $$$$$$$$
               | $$| $$      | $$  \  $$$/  | $$ /$$__  $$         | $$   | $$| $$ | $$ | $$| $$_____/
               | $$| $$      | $$   \  $/   | $$|  $$$$$$$         | $$   | $$| $$ | $$ | $$|  $$$$$$$
               |__/|__/      |__/    \_/    |__/ \_______/         |__/   |__/|__/ |__/ |__/ \_______/
                                                                                          
                                                                                          
                                                                                          
            """)
        print("Trivia Time: Trivia ")
        print(tt)
        triv(tt)
def flex(logic):
    if (logic == 1):
        print("A murderer is condemned to death. He has to choose between three rooms."+
       "The first is full of raging fires, the second is full of assassins with loaded"+
       "guns, and the third is full of lions that haven't eaten in 3 years.")
        answer = input("Which room is safest for him? (First, Second, Third)")
        if answer == 'Third':
            print("The third room, because those lions haven't eaten in three years, so they are dead.")
            logic += 1
            flex(logic)
        if answer == 'ex1t':
            sys.exit("END GAME")
        else:
            print("Need a valid answer")
            flex(logic)
        flexThatLogic(logic)
    if (logic == 2):
        answer = input("Five men were eating apples, A finished before B,"+
                       " but behind C. D finished before E, but behind B. "+ 
                       "What was the finishing order?")
        if answer == 'cabde':
            print("Correct")
            logic += 1
            flex(logic)
        if answer == 'ex1t':
            sys.exit("END GAME")
        elif():
            print("Need a valid answer")
            flex(logic)
        flexThatLogic(logic)
    if (tt == 3):
        answer = input("Which bird does not belong in this group? Finch, gull, eagle, ostrich, or sparrow?")
        if answer == 'ostrich':
            print("Correct, The Ostrich can't fly.")
            logic += 1
            flex(logic)
        if answer == 'ex1t':
            sys.exit("END GAME")
        elif():
            print("Need a valid answer")
            flex(logic)
    if (logic > 3):
        flexThatLogic(logic)
def flexThatLogic(logic):
    if logic == 4:
        print("Logic has been flexed")
        Trials.remove("Flex That Logic")
        ultimateChoice()
    if logic !=4:
        if logic == 1:
            print("""
                                                                                          
                @@@@@@@@  @@@       @@@@@@@@  @@@  @@@     @@@@@@@  @@@  @@@   @@@@@@   @@@@@@@     
                @@@@@@@@  @@@       @@@@@@@@  @@@  @@@     @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@     
                @@!       @@!       @@!       @@!  !@@       @@!    @@!  @@@  @@!  @@@    @@!       
                !@!       !@!       !@!       !@!  @!!       !@!    !@!  @!@  !@!  @!@    !@!       
                @!!!:!    @!!       @!!!:!     !@@!@!        @!!    @!@!@!@!  @!@!@!@!    @!!       
                !!!!!:    !!!       !!!!!:      @!!!         !!!    !!!@!!!!  !!!@!!!!    !!!       
                !!:       !!:       !!:        !: :!!        !!:    !!:  !!!  !!:  !!!    !!:       
                :!:        :!:      :!:       :!:  !:!       :!:    :!:  !:!  :!:  !:!    :!:       
                 ::        :: ::::   :: ::::   ::  :::        ::    ::   :::  ::   :::     ::       
                 :        : :: : :  : :: ::    :   ::         :      :   : :   :   : :     :        
                                                                                    
                                                                                    
                @@@        @@@@@@    @@@@@@@@  @@@   @@@@@@@                                        
                @@@       @@@@@@@@  @@@@@@@@@  @@@  @@@@@@@@                                        
                @@!       @@!  @@@  !@@        @@!  !@@                                             
                !@!       !@!  @!@  !@!        !@!  !@!                                             
                @!!       @!@  !@!  !@! @!@!@  !!@  !@!                                             
                !!!       !@!  !!!  !!! !!@!!  !!!  !!!                                             
                !!:       !!:  !!!  :!!   !!:  !!:  :!!                                             
                 :!:      :!:  !:!  :!:   !::  :!:  :!:                                             
                 :: ::::  ::::: ::   ::: ::::   ::   ::: :::                                        
                : :: : :   : :  :    :: :: :   :     :: :: :    
                
            """)
            print("Flex That Logic: Logic ")
            print(logic)
            flex(logic)
        elif():
            print("Flex That Logic: Logic ")
            print(logic)
            flex(logic)
def math(problem):
    if (problem == 1):
        answer = input("Whats the next number in this sequence: 4181, 6765, 10946, 17711, 28657, 46368, 75025")
        if answer == '121393':
            print("Correct")
            problem += 1
            math(problem)
        if answer == 'ex1t':
            sys.exit("END GAME")
        else:
            print("Need a valid answer")
            math(problem)
        mathTime(problem)
    if (problem == 2):
        answer = input("356370373257098342543769093 mod 2")
        if answer == '1':
            print("Correct")
            problem += 1
            math(problem)
        if answer == 'ex1t':
            sys.exit("END GAME")
        elif():
            print("Need a valid answer")
            math(problem)
        mathTime(problem)
    if (problem == 3):
        answer = input("Can you fill the blank space; 19=8, 6=3, 70=7, 8=5, 4=4, 60=5, 15=7, 16=?")
        if answer == '7':
            print("Correct")
            problem += 1
            math(problem)
        if answer == 'ex1t':
            sys.exit("END GAME")
        elif():
            print("Need a valid answer")
            math(problem)
    if (problem > 3):
        mathTime(problem)
def mathTime(problem):
    if problem == 4:
        print("Math Problems Solved")
        Trials.remove("Math")
        ultimateChoice()
    if problem !=4:
        if problem == 1:
            print("""
                   
            '##::::'##::::'###::::'########:'##::::'##:
             ###::'###:::'## ##:::... ##..:: ##:::: ##:
             ####'####::'##:. ##::::: ##:::: ##:::: ##:
             ## ### ##:'##:::. ##:::: ##:::: #########:
             ##. #: ##: #########:::: ##:::: ##.... ##:
             ##:.:: ##: ##.... ##:::: ##:::: ##:::: ##:
             ##:::: ##: ##:::: ##:::: ##:::: ##:::: ##:
            ..:::::..::..:::::..:::::..:::::..:::::..::                                                                                   
            """)
        print("Math Time: Problem ")
        print(problem)
        math(problem)



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
     if choice == 'Flex That Logic':
        flexThatLogic(logic)
        complete = 1
     if choice == 'Math':
        mathTime(problem)
        complete = 1
     if choice == 'ex1t':           
        sys.exit("END GAME")
     elif complete == 0:
        print("I need a vaild answer")
        ultimateChoice()





print("Hello")
time.sleep(1) 
ans = input("Do you want to play a game?" '\n')
initiation(ans)

print("In order to get out of this safetly you will need to complete some tasks.")
time.sleep(1)
print("Choose one on these games, beat three and you win." '\n' '\n')

ultimateChoice()