(1) load the words file, choose a word from file and set that word for hangman.
(2) start the CLI for hangman game
    a. game instructions
    b. user display, number of tries. Player gets 8 tries. 
    c. show user the number of letters in word
        h e l l o -> h _ _ _ o
    d. user see full list of lowercase alphabet
        a played letter is not counted against the 8 tries but a letter that is not in word is considered a miss. 
        ask user for input. declare if user wins or loses. 

----------------------------------
It's Hangman! find the out the secret word!

number to tries left: 8
letters to choose from: abcdefghijklmnopqrstuvwxyz

word: _ _ _ _ _  

Enter a letter: o

-----------------------------------
number to tries left: 8
letters to choose from: abcdefghijklmn_pqrstuvwxyz

word: _ o _ _ _  

Enter a letter: m

-----------------------------------
number to tries left: 7
letters to choose from: abcdefghijkl_n_pqrstuvwxyz

word: _ o _ _ _  

Enter a letter: m

-----------------------------------
Error! you already tried "m"

number to tries left: 7
letters to choose from: abcdefghijkl_n_pqrstuvwxyz

word: _ o _ _ _  

Enter a letter: o

-----------------------------------
Error! you already tried "o"

number to tries left: 7
letters to choose from: abcdefghijkl_n_pqrstuvwxyz

word: _ o _ _ _  

Enter a letter: w

-----------------------------------
number to tries left: 7
letters to choose from: abcdefghijkl_n_pqrstuv_xyz

word: w o _ _ _  

Enter a letter: r

-----------------------------------
number to tries left: 7
letters to choose from: abcdefghijkl_n_pq_stuv_xyz

word: w o r _ _  

Enter a letter: l

-----------------------------------
number to tries left: 7
letters to choose from: a b c d e f g h i j k _ _ n _ p q _ s t u  v _ x y z

word: w o r l _  

Enter a letter: d

-----------------------------------
congratulations, you won!

# << -- OR lose condition -- >>

-----------------------------------
number to tries left: 7
letters to choose from: abcdefghijkl_n_pqrstuvwxyz

word: _ o _ _ _  

Enter a letter: a

-----------------------------------
number to tries left: 6
letters to choose from: _ b c d e f g h i j k l _ n _ p q r s t u v w x y z

word: _ o _ _ _  

Enter a letter: a

-----------------------------------
You lose, but feel free to try again!



# data structure
import random

filename = words.txt
loadwords(filename)