[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=nouryousry_HangmanGame&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=nouryousry_HangmanGame) [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=nouryousry_HangmanGame&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=nouryousry_HangmanGame) [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=nouryousry_HangmanGame&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=nouryousry_HangmanGame) [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=nouryousry_HangmanGame&metric=bugs)](https://sonarcloud.io/summary/new_code?id=nouryousry_HangmanGame) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=nouryousry_HangmanGame&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=nouryousry_HangmanGame) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=nouryousry_HangmanGame&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=nouryousry_HangmanGame)[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=nouryousry_HangmanGame&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=nouryousry_HangmanGame)
# HangmanGame
This is the game of hangman created using python and will later include GUI as well. You will find below all the points created up till now for the project and where they could be found.

## 1.Git
All commit activity for this repository could be found [here](https://github.com/nouryousry/HangmanGame/graphs/commit-activity)

## 2.UML
[Use case diagram](https://github.com/nouryousry/HangmanGame/blob/main/UML/use_case_diagram.png)  
[Activity diagram](https://github.com/nouryousry/HangmanGame/blob/main/UML/Activity%20Diagram.png)  
[Component diagram](https://github.com/nouryousry/HangmanGame/blob/main/UML/componend%20diagram.png)  

Usecase and component diagrams were created by planttext and activity diagram was created using asta. planttexts and asta template could be found at the [UML folder](https://github.com/nouryousry/HangmanGame/tree/main/UML)

## 3.DDD
[Event storming](https://github.com/nouryousry/HangmanGame/blob/main/DDD/Brainstorming.png)  
[Core Domain Chart](https://github.com/nouryousry/HangmanGame/blob/main/DDD/Core_domain_chart.png)  
[Relations Chart](https://github.com/nouryousry/HangmanGame/tree/main/DDD)  

## 4.Metrics  
Metrics could be found as tags at the top of this readme file. They were created using Sonarcloud.

## 5.Clean Code Development
- I have added all principles that I had in mind when developing this code in this [cheat sheet](https://github.com/nouryousry/HangmanGame/blob/main/Cheat%20Sheet.pdf)
- Any line of code that will not be easily interpreted had a comment above it to explain it (cheat sheet #2)
- All variables have meaningful names that relate to their role (cheat sheet #1)
- All functions have docstrings defining input, output as well as short description (cheat sheet #3)
- No code is repeated
- Meaningful function names (cheat sheet #10)

## 6.Build Management
I have used pybuilder to manage the builds, the file used could be found [here](https://github.com/nouryousry/HangmanGame/blob/main/build.py) as well as a [screenshot](https://github.com/nouryousry/HangmanGame/blob/main/successful_build.png) of first successful build

## 7.Unit Tests
Multiple unit tests were used and were integrated by pybuilder to run each time before creating a build.  
The unittests file could be found [here](https://github.com/nouryousry/HangmanGame/blob/main/src/unittest/python/hangman_unittests.py)

## 8.Continuous Delivery
For continuous delivery, Github Actions was used. It integrated well with Python and pybuilder and creates a [workflow](https://github.com/nouryousry/HangmanGame/actions) every time I push which in turn creates a build using pybuilder   
The script used could be found [here](https://github.com/nouryousry/HangmanGame/blob/main/.github/workflows/python-app.yml)

## 9.IDE
I have used [pycharm](https://www.jetbrains.com/pycharm/) as IDE. It integrates well with Github and is easy to use. It also has a dark theme which is pretty comfy for me.  
Best shortcut that I tend to use alot is **Ctrl+Alt+Shift+Click** and drag the mouse over the desired parts of code to put multiple cursors at the same time.  
It's usually useful when indenting or adding/ deleting hash for comments.  
Also, **shift+tab** inindents a line, which is useful when adding wrong indents for a line of code.

## 10.DSL
For DSL, I have added a separate piece of code. It's a creates personalised bedtime story for kids based on the name and the gender that was entered by the user.  
The code could be viewed [here](https://github.com/nouryousry/HangmanGame/blob/main/DSL/main.py)

## 11.Functional Programming
The [hangman file](https://github.com/nouryousry/HangmanGame/blob/main/src/main/python/hangman.py) had been re-factored to turn into functional programming.  
All the functions are side-effect free and also has an [higher-order function](https://github.com/nouryousry/HangmanGame/blob/main/src/main/python/hangman.py#L96) with closures.

