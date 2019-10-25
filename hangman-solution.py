import random
from string import ascii_lowercase

def getWord():
    i=0
    with open('wordlist.txt', 'r') as f:
        for word in f:
            i=i+1
            if random.randint(1, i) == 1:
                pickedWord = word
    return pickedWord


def askAttempts():
    while True:
        num = input('How many incorrect attempts do you want? [1-25] ')
        try:
            num = int(num)
            if 1 <= num <= 25:
                return num
            else:
                print('{0} is not between 1 and 25'.format(num))
        except ValueError:
            print('{0} is not an integer between 1 and 25'.format(num))


def display(word, idxs):
    displayed_word = ''.join(
        [letter if idxs[i] else '*' for i, letter in enumerate(word)])
    return displayed_word.strip()


def askLetter(remaining_letters):
    """Get the user-inputted next letter."""
    if len(remaining_letters) == 0:
        raise ValueError('There are no remaining letters')
    while True:
        next_letter = input('Choose the next letter: ').lower()
        if len(next_letter) != 1:
            print('{0} is not a single character'.format(next_letter))
        elif next_letter not in ascii_lowercase:
            print('{0} is not a letter'.format(next_letter))
        elif next_letter not in remaining_letters:
            print('{0} has been guessed before'.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter


def main():
    attemptsLeft = askAttempts()
    word = getWord()
    idxs = [letter not in ascii_lowercase for letter in word]
    remaining_letters = set(ascii_lowercase)
    wrong_letters = []
    solved = False
    while attemptsLeft > 0 and not solved:
        print('Word: {0}'.format(display(word, idxs)))
        print('Attempts Remaining: {0}'.format(attemptsLeft))
        print('Previous Guesses: {0}'.format(' '.join(wrong_letters)))
        next_letter = askLetter(remaining_letters)
        if next_letter in word:
            print('{0} is in the word!'.format(next_letter))
            for i in range(len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
            print('{0} is NOT in the word!'.format(next_letter))
            attemptsLeft = attemptsLeft-1
            wrong_letters.append(next_letter)
        if False not in idxs:
            solved = True
        print()
    print('The word is {0}'.format(word))
    if solved:
        print('Congratulations! You won!')
    else:
        print('Try again next time!')
    retry = input('Enter y/Y to try again ')
    return retry.lower() == 'y'


if __name__ == '__main__':
    while main():
        print()
