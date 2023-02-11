import random

#immutable tuples to keep the words that will be used in the game
easy_wordbank = ("cat", "cars", "pooh", "toys", "game","tell","fun","let","why")
medium_wordbank=("aladdin", "godzilla","marvel","amazed","funny","loyal","regard")
hard_wordbank=("terminator","magnificent","awesome","yearn","follicular",\
"impressionable", "misrepresentation", "antiskepticism")


#Functional Programming: All functions here are side-effect free functions

#function to display the hangman shape
def display_hangman(tries):
    """input: number of trials left
    output: string with shape of hangman"""
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
def hangman(word, tries, guessed_word):
    """input: two strings and an int
       output: None
       This function lets the user inputs a letter then checks if it's in the string word
       and keeps or reduces number of trials accordingly"""
    if tries == 0:
        print("You lost! The word was " + word + ".")
        return None
    if word == guessed_word:
        print("Congratulations! You saved the man!")
        return None
    print("Current word: " + guessed_word)
    print("You have " + str(tries) + " tries left.")
    letter = input("Enter a letter: ").lower()
    if letter in word:
        print("Correct!")
        #checking if char entered by user is in original string then adding it to guessed word if so
        #then converting the list into string again
        guessed_word = "".join([char if char == letter else guessed_word[i] for i, char in enumerate(word)])
    else:
        tries -= 1
        print(display_hangman(tries))
    hangman(word, tries, guessed_word)

#Functional Programming
#use of closure as well as high-order functions where
#word_bank function is used as a return value of pick_word function
def pick_word(difficulty):
    """input: string that defines the tuple to be used
        output: string of the word to be used in the game
        the pick word defines the word used in the game according to
        the difficulty defined by the user"""
    def word_bank(difficulty):
        """input: string that defines the tuple to be used
            output: tuple of words"""
        if difficulty == "easy":
            return easy_wordbank
        elif difficulty == "medium":
            return medium_wordbank
        elif difficulty == "hard":
            return hard_wordbank
        else:
            return None
    # random.choice will choose a random word from the tuple
    # according to difficulty defined by user
    return random.choice(word_bank(difficulty))

# This function sets up the game and calls the hangman function
def play_game():
    """input: none
       output: none
       this function initialises the game of hangman """
    difficulty = input("Please choose if you want it easy, medium or hard: ").lower()
    word = pick_word(difficulty)
    guessed_word = "_" * len(word)
    tries = 5
    hangman(word, tries, guessed_word)
    print(tries)
