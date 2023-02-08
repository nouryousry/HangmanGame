# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_story(name,pronouns):
    gender="girl" if pronouns=="she/her" else "boy" if pronouns=="he/him" else "person"
    pronouns=pronouns.split("/")
    print(f'Once upon a time, there was a {gender} whose name is {name}, while {pronouns[0]} was walking in the forest all alone.\n '
          f'{name} was brave but the forest was still scary. While walking, {pronouns[0]} heard the sound of little kitten.\n'
          f'{pronouns[0]} ran quickly to see this little kitten. Turns out, the kitten was on the tree and scared to come down.\n'
          f'Luckily for the cat, {name} was a climber so {pronouns[0]} climbed up the tree and saved the kitten. The cat was very happy and kept\n '
          f'playing with {name} and followed {pronouns[1]} home and they became friends forever.')


if __name__ == '__main__':
    name=input("Please enter the name of the hero: ")
    pronouns=input("Please enter pronouns of the hero separated by / : ")
    print_story(name, pronouns)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
