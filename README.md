# Hangman

Objectives
The game starts with a menu where a player can choose to either play or exit.
Type "play" to play the game, "exit" to quit: and this message is shown again if the player inputs something else.
If the user chooses to play, the game begins.

Example
The greater-than symbol followed by space (> ) represents the user input. Note that it's not part of the output.

H A N G M A N
Type "play" to play the game, "exit" to quit: > play

----------
Input a letter: > a

-a-a------
Input a letter: > i

-a-a---i--
Input a letter: > o
That letter doesn't appear in the word

-a-a---i--
Input a letter: > o
You've already guessed this letter

-a-a---i--
Input a letter: > p

-a-a---ip-
Input a letter: > p
You've already guessed this letter

-a-a---ip-
Input a letter: > h
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > k
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > a
You've already guessed this letter

-a-a---ip-
Input a letter: > z
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > t

-a-a---ipt
Input a letter: > x
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > b
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > d
That letter doesn't appear in the word

-a-a---ipt
Input a letter: > w
That letter doesn't appear in the word
You lost!

Type "play" to play the game, "exit" to quit: > exit
