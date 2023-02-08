import random

#immutable tuples to keep the words
easy_wordbank = ("cat", "cars", "pooh", "toys", "game","tell","fun")
medium_wordbank=("aladdin", "godzilla","marvel","amazed","funny")
hard_wordbank=("terminator","magnificent","awesome","yearn","follicular",\
"impressionable", "misrepresentation", "antiskepticism")


def display(guessed_word):
    statement=""
    for char in guessed_word:
            statement += char + " "
    print(statement)

def check_done(display_terms):
    done = True
    for term in display_terms:
        for char in term:
            if char == "_":
                done = False
    return done





def check_letter(letter,word,guessed_word):
    if letter in word:
        index=word.find(letter)
        while index!=-1:
            guessed_word=guessed_word[0:index]+letter+guessed_word[index+1:]
            index=word.find(letter,index+1)
        guesses-=1
        if guesses==0:
            wins+=1
            won=True
            print("Congratulations! You saved the man!")
            print("Your score is " + str(wins) + " wins and " + str(losses) + " losses.")
        #self.check_win()

    else:
        mistakes+=1
        display_hangman()
        if mistakes==4:
            lost=True
            losses+=1
            print("You have lost the game!")
            print("Your score is "+str(wins)+" wins and "+str(losses)+" losses.")

def display_hangman(tries):

    if tries==4:
        print("""
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """)
    elif tries==3:
        print("""
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """)
    elif tries==2:
        print(    """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """)
    elif tries == 1:
        print("""
                 --------
                 |      |
                 |      O
                 |     \|/
                 |      |
                 |     
                 -
              """)
    elif tries == 0:
        print("""
                 --------
                 |      |
                 |      O
                 |     \|/
                 |      |
                 |     /|\ 
                 -
            """)





# This function implements the game logic for hangman and is recursive in nature
def hangman(word, tries, secret_word):
    if tries == 0:
        print("You lost! The word was " + word + ".")
        return None
    if word == secret_word:
        print("Congratulations! You saved the man!")
        return None
    print("Current word: " + secret_word)
    print("You have " + str(tries) + " tries left.")
    letter = input("Enter a letter: ").lower()
    if letter in word:
        print("Correct!")
        word_list = [char if char == letter else secret_word[i] for i, char in enumerate(word)]
        secret_word = "".join(word_list)
    else:
        tries -= 1
        display_hangman(tries)
    hangman(word, tries, secret_word)



def pick_word():
    difficulty=input("Please choose if you want it easy, medium or hard: ").lower()
    def word_bank(difficulty):
        if difficulty == "easy":
            return easy_wordbank
        elif difficulty == "medium":
            return medium_wordbank
        elif difficulty == "hard":
            return hard_wordbank
        else:
            return None
    return random.choice(word_bank(difficulty))

# This function sets up the game and calls the hangman function
def play_game():
    word = pick_word()
    secret_word = "_" * len(word)
    tries = 5
    hangman(word, tries, secret_word)


def main():
    play_game()


if __name__ == "__main__":
    main()



