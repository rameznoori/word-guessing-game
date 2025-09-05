import random

word_bank = ['simple', 'night', 'project', 'python', 'programming']
word = random.choice(word_bank)
guessed_word = ['_'] * len(word)
attempts = 15

while attempts > 0:
    print(f'\nCurrent word: {" ".join(guessed_word)}')
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
    print('\nYou\'ve run out of attempts! The word was: ' + word)
