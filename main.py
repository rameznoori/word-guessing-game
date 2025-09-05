import random

word_bank = ['simple', 'night', 'project', 'python', 'programming']
word = random.choice(word_bank)
guessed_word = ['_'] * len(word)
max_attempts = 15
attempts = max_attempts

hangman_stages = [
    """
    -----
    |   |
        | 
        |
        |
        |
--------------
""",
"""
    -----
    |   |
    O   |
        |
        |
        |
--------------
""",
"""
    -----
    |   |
    O   |
    |   |
        |
        |
--------------
""",
"""
    -----
    |   |
    O   |
   /|   |
        |
        |
--------------
""",
"""
    -----
    |   |
    O   |
   /|\\  |
        |
        |
--------------
""",
"""
    -----
    |   |
    O   |
   /|\\  |
   /    |
        |
--------------
""",
"""
    -----
    |   |
    O   |
   /|\\  |
   / \\  |
        |
--------------
"""
]

# Calculate how to map attempts left to hangman stages:
# There are 7 stages only, so reduceing number of attempts
def get_hangman_stage(attempts_left):
    stage_index = max_attempts - attempts_left
    # Clamping to max stage index to avoid index errors
    if stage_index >= len(hangman_stages):
        stage_index = len(hangman_stages) - 1
    return hangman_stages[stage_index]


while attempts > 0:
    print(f'\nCurrent word: {" ".join(guessed_word)}')
    print(get_hangman_stage(attempts))
    guess = input('Guess a letter: ').lower()

    if guess in word:
        guessed_word = [guess if c == guess else g for c, g in zip(word, guessed_word)]
        print('Great! Keep going...')
    else:
        attempts -= 1
        print(f'Wrong guess, Attempts left: {attempts}')

    if '_' not in guessed_word:
        print(f'\nCongrats! You guessed the word: {word}')
        break

if attempts == 0 and '_' in guessed_word:
    print(get_hangman_stage(0))
    print('\nYou\'ve run out of attempts! The word was: ' + word)
