import random
import string

filename = '.\hangman\words.txt'
fhand = open(filename)
for line in fhand:
    word_list = line.split()

secretWord = random.choice(word_list)

def myword_display(secretWord, myword):
    """
    input str + list
    return display str
    """
    display_word = ''
    for l in secretWord:
        if l in myword:
            display_word += l
        else: 
            display_word += ' _ '

    return display_word

lifeline = 8
alpha = list(string.ascii_lowercase)
myword = []

print('------------------------------------')
print('It\'s Hangman! Find out the secret word to win!')

while lifeline > 0:
    print('\n\nNumber to lives left:', lifeline)
    print('Letters to choose from:', alpha)

    print('\nword:', myword_display(secretWord, myword))  

    try:
        user_input = input('Enter a letter: ')
        if user_input.lower() in alpha:
            alpha.remove(user_input.lower())
            myword.append(user_input.lower())
            if user_input.lower() not in secretWord:
                lifeline -= 1
        else:
            print('Invalid input or letter already been choosen')
    except:
        print('Invalid input or letter already been choosen')

    try:
        if len(secretWord) == len(myword_display(secretWord, myword).strip()):
            print('Congratulations, you won!, the word was',secretWord)
            break
        elif lifeline == 0:
            print("You lose, the word was",secretWord)
    except:
        raise('program error')