import random

#immutable tuples to keep the words
easy_wordbank = ("cat", "cars", "pooh", "toys", "game","tell","fun","let","why")
medium_wordbank=("aladdin", "godzilla","marvel","amazed","funny","loyal","regard")
hard_wordbank=("terminator","magnificent","awesome","yearn","follicular",\
"impressionable", "misrepresentation", "antiskepticism")


def display_hangman(tries):

    if tries==4:
        return("""
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """)
    elif tries==3:
        return("""
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """)
    elif tries==2:
        return(    """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """)
    elif tries == 1:
        return("""
                 --------
                 |      |
                 |      O
                 |     \|/
                 |      |
                 |     
                 -
              """)
    elif tries == 0:
        return("""
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
        print(display_hangman(tries))
    hangman(word, tries, secret_word)



def pick_word(difficulty):
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
    difficulty = input("Please choose if you want it easy, medium or hard: ").lower()
    word = pick_word(difficulty)
    secret_word = "_" * len(word)
    tries = 5
    hangman(word, tries, secret_word)
