import math
import random
import re

easy_wordbank = ["cat", "cars", "pooh", "toys", "game","tell","fun"]
medium_wordbank=["aladdin", "godzilla","marvel","amazed","funny"]
hard_wordbank=["terminator","magnificent","awesome","yearn","follicular"]


class Hangman:
    wins=0
    losses=0

    def display(self):
        statement=""
        for char in self.guessed_word:
                statement += char + " "
        print(statement)

    def check_done(self):
        done = True
        for term in display_terms:
            for char in term:
                if char == "_":
                    done = False
        return done
    def choose_difficulty(self):
        difficulty=input("Please choose if you want it easy, medium or hard: ")
        while difficulty not in ("easy","medium","hard"):
            print("wrong input")
            difficulty = input("Please choose if you want it easy, medium or hard: ")
        return difficulty

    def pick_word(self):
        dif=self.choose_difficulty()
        if dif=="easy":
            word_id = random.randrange(0, len(easy_wordbank)-1)
            return easy_wordbank[word_id]
        elif dif=="medium":
            word_id = random.randrange(0, len(medium_wordbank)-1)
            return medium_wordbank[word_id]
        elif dif=="hard":
            word_id = random.randrange(0, len(hard_wordbank)-1)
            return hard_wordbank[word_id]

    def choose_letter(self):
        letter=input("Choose a letter: ")
        while re.search('[a-zA-Z]',letter)==False or len(letter)!=1:
            print("You entered a wromg character, try again!")
            letter = input("Choose a letter: ")
        self.check_letter(letter)

    def check_letter(self,letter):
        if letter in self.word:
            index=self.word.find(letter)
            while index!=-1:
                self.guessed_word=self.guessed_word[0:index]+letter+self.guessed_word[index+1:]
                index=self.word.find(letter,index+1)
            self.guesses-=1
            if self.guesses==0:
                Hangman.wins+=1
                self.won=True
                print("Congratulations! You saved the man!")
                print("Your score is " + str(Hangman.wins) + " wins and " + str(Hangman.losses) + " losses.")
            #self.check_win()

        else:
            self.mistakes+=1
            self.display_hangman()
            if self.mistakes==4:
                self.lost=True
                Hangman.losses+=1
                print("You have lost the game!")
                print("Your score is "+str(Hangman.wins)+" wins and "+str(Hangman.losses)+" losses.")

    def display_hangman(self):

        if self.mistakes==1:
            print("""
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """)
        elif self.mistakes==2:
            print("""
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """)
        elif self.mistakes==3:
            print(    """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """)
        elif self.mistakes == 4:
            print("""
                     --------
                     |      |
                     |      O
                     |     \|/
                     |      |
                     |     
                     -
                  """)
        elif self.mistakes == 5:
            print("""
                     --------
                     |      |
                     |      O
                     |     \|/
                     |      |
                     |     /|\ 
                     -
                  """)

    def __init__(self):
        self.word=self.pick_word()
        self.guessed_word=""
        self.guessed_word="_"*len(self.word)
        self.mistakes=0
        self.guesses=len(set(self.word))
        self.won=False
        self.lost=False
        while self.lost==False and self.won==False:
            self.display()
            self.choose_letter()



def main():
    Hangman()


if __name__ == "__main__":
    main()



