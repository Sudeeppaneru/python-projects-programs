# Mad Libs Game

A simple **Mad Libs** game written in Python. The program asks the player to enter different types of words, then uses those words to create a funny story.

## Features

* Interactive command-line game
* Asks the user for:

  * 3 nouns
  * 1 plural noun
  * 3 adjectives
* Generates a unique story based on the user's input
* Beginner-friendly Python project

## Requirements

* Python 3.x

No external libraries are required.

## How to Run

1. Make sure Python is installed on your computer.
2. Clone or download this project.
3. Open a terminal in the project directory.
4. Run:

```bash
python madlibs.py
```

## How to Play

The program will ask you to enter different words.

For example:

```text
Enter a noun: restaurant
Enter a noun: argument
Enter a plural noun: rules
Enter an adjective: bitter
Enter an adjective: temporary
Enter an adjective: lasting
Enter a noun: agreement
```

The program then creates a story using your answers.

## Example Output

```text
Once dining restaurant used to be war argument. I thought the battles about correct table rules would never end. It was us kids versus Mom, and It seemed like a fight that would last to the bitter end. But tonight Dad finally declared a/an temporary truce, and we negotiated a/an lasting peace agreement.
```

## Concepts Used

This project demonstrates several basic Python concepts:

* `input()` for getting user input
* Variables
* **f-strings** for inserting variables into strings
* `print()` for displaying output
* Basic string manipulation

## Project Structure

```text
madlibs/
├── madlibs.py
└── README.md
```
