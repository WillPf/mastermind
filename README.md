# Mastermind

### Video Demo:  [Mastermind](https://youtu.be/4s7dlVamy6k)

### Description:
For the final project of [CS50P]("https://cs50.harvard.edu/python/2022/project/), I made this mastermind game made with [PySimpleGUI]("https://docs.pysimplegui.com/en/latest/) for the GUI.
The rules are simple, there is a secret code which consists of a sequence of 4 colors (colors can be repeated) and you have to find the code in 10 steps max.
Each time you try a combination, you have clues to help you:
For every well placed ball, a "⚫️"is shown.
For every good color guessed but misplaced, a "⚪️"is shown.

### Structure of the code:
Since one of the requirements for this project is to have functions as the same indentation as main and in the same file, I kept the structure of the code simple.
I have a gui.py filefor the GUI and the project.py file for the backend.

### How it works:
When the program is launched, a random sequence is created out of a list of 6 colors with random.choice().
Then whenever the player clicks a ball, its color is added to a list, and when the list is of length 4, it's compared to the sequence and the clues are shown.
If the player reaches 10 tries without solving the sequence, the game is lost.
If the player finds the right combination, he wins the game.
Either way, the player is asked if he wants to play again, then another sequence is generated or the game ends.

#### Functions:
The create_sequence(colors) takes a list of colors as an argument and returns a list of 4 random colors.

The check_answer(sequence, player) takes 2 lists as arguments: the generated sequence, and the player guess.

```
1 def check_answer(seq, player):
2     copy_seq = seq.copy()
3     same_place = 0
4     same_color = 0
5     for i in range(len(copy_seq)):
6         if copy_seq[i] == player[i]:
7             same_place += 1
8     for color in player:
9         if color in copy_seq:
10            same_color += 1
11            copy_seq.pop(copy_seq.index(color))
12    same_color -= same_place
13    return same_place, same_color
```

On line 2 I create a copy of the sequence list so I can remove items from it without affecting the original list.
I then declare 2 variables for the well placed balls and the misplaced ones.
Then on line 5, a first loop is used to check the well placed balls by comparing the 2 lists with the same index.
On line 8, a second loop is used for checking the misplaced good color balls.
Each time a color is find, I remove it from the list so it doesn't get count multiple times if there is the same color more than once in the sequence.
Since it will count all the colors guessed, but the well placed colors are already counted, I substract the well placed balls from all the colors counted (line 12)
There is probably a more efficient way of doing it but this is the solution I found because I realized that coding mastermind is actually trickier that I thought and I had a lot of bugs when multiple colors are in the sequence for example.

The show_answer(seq, str) creates a popup showing the sequence and a different text depending on the player winning or losing.

I also added a stats function to save stats on a .txt file. It just write if the player has won or lost and how many guess he made to win the game.
If I'm being honest, I only implemented this to have another function to unit test it.
Because CS50P requires us to have 3 functions to unit test but I couldn't use it on the function that returns a popup, especially since the popup doesn't close automatically.

### Final words:
Well That's it.
Thank you CS50P.
I finished CS50 a couple of months ago, now I'm on my way to finish CS50P and I'm excited for the next one :)