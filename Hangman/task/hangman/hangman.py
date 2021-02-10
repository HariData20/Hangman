# Write your code here
# Write your code here
import random
import sys

print('H A N G M A N')

words = ['python', 'java', 'kotlin', 'javascript']
chosen = random.choice(words)
'''
Stage 4
to_print = chosen[:3] + '-' * (len(chosen) - 3)
word = input(f'Guess the word: {to_print}')
words = ['python', 'java', 'kotlin', 'javascript']
if word == chosen:
    print('You survived!')
else:
    print('You lost!')'''

# Stage 5

len_ = len(chosen)
display_str = '-' * len_
i = 0
index_ = 0
list_input = []
while True:
    print('Type "play" to play the game, "exit" to quit:')
    choice = input()
    if choice == 'exit':
        sys.exit()
    elif choice == 'play':
        while i < 8:
            print()
            print(display_str)
            c = input("Input a letter: ")
            if len(c) != 1 and len(c) > 0:
                print('You should input a single letter')
                continue
            elif c.isupper() or not c.isalpha():
                print("It is not an ASCII lowercase letter")
                continue
            elif c in list_input or c in display_str:
                print("You already typed this letter")
                continue

            if c in chosen:

                if chosen.count(c) == 1:
                    index_ = chosen.find(c)
                    display_str = display_str[:index_] + c + display_str[index_ + 1:]
                    if display_str == chosen:
                        print(f'You guessed the word {chosen}!\nYou survived!')
                        sys.exit()

                else:
                    index_ = chosen.find(c)
                    display_str = display_str[:index_] + c + display_str[index_ + 1:]
                    for _ in range(chosen.count(c) - 1):
                        index_ = chosen.find(c, index_ + 1, len_)
                        display_str = display_str[:index_] + c + display_str[index_ + 1:]
                    if display_str == chosen:

                        print(f'You guessed the word {chosen}!\nYou survived!')
                        sys.exit()

            else:
                i += 1
                list_input.append(c)
                print("No such letter in the word")

        if display_str == chosen:
            print(chosen)
            print(f'You guessed the word {chosen}!\nYou survived!')

        else:
            print('You lost!')
