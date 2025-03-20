import os
import platform
import time

#Konsolu temizleyen fonksiyon (Tüm platformlarda)
def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

clear_console() # Konsolu temizler

username = input("Enter username: ")
clear_console()
print(f"Hello {username}! It is time to play HANG-MAN!")
time.sleep(3)
clear_console()
print("Let's play, shall we :)")
time.sleep(3)

word = "KARABEY" #adam asmaca kelimesi
guessWord = []

# Kelimeyi tamamlamaya çalıştığımız değişken
for num in range(0, len(word)):
    guessWord.append("-")

# İnput aldığımız değişken
inputWord = list()
for num in range(0, len(word)):
    inputWord.append("")

###################
####### OYUN
leftLives = 10
flag2 = 1
alreadyGuessed = False
inputWord = ""
flag3 = 1

while leftLives != 0:
    clear_console() # Konsolu temizler
    
    if "".join(guessWord) == word or inputWord.upper() == word.upper():
            print(f"\n\nCongrats {username}! You guessed the word right which was {word}!\n\n")
            break
    
    print("If you have a guess, DO the guess!\n")

    print(f"=-=-=-=-=-= {leftLives} lives left =-=-=-=-=-=\n")

    # Doldurduğumuz kelimeyi ekrana yazdır
    print("^^^^^^^^^^^^^^^^^^")
    for _ in range(0, len(word)):
        print(f"\t{guessWord[_]}")
    print("^^^^^^^^^^^^^^^^^^")

    if flag3 == 1:
        inputWord = input("Guess one letter of word: ")
    
    if alreadyGuessed:
        inputWord = input(f"You have already guessed letter {inputWord.upper()}, try ANOTHER letter this time: ")
        alreadyGuessed = False
    else:
        if flag2 == 0:
            inputWord = input(f"You guessed WRONG! The word doesn't contain the letter {inputWord.upper()}, try another letter: ")    
        else: 
            if len(inputWord) > 1 and flag3 == 0:
                inputWord = input("Please enter ONE latter, not multiple latter: ")
            elif flag3 == 0:
                inputWord = input(f"CORRECT! The word contains the letter {inputWord.upper()}, guess one more letter of word: ")

    flag3 = 0
    if len(inputWord) > 1 and inputWord != word:
        flag2 = 1
        continue

    flag = 0
    flag2 = 0
    for element in range(0, len(word)):
        if inputWord.lower() == word[element] or inputWord.upper() == word[element]:
            
            # Eğer harfi daha önce bildiyse
            if inputWord.upper() == guessWord[element]:
                alreadyGuessed = True

            guessWord[element] = inputWord.upper()
            flag = 1
            flag2 = 1

    if flag == 0:
        leftLives -= 1 # Canı 1 azalt
        if leftLives == 0: # Canı bittiyse oyunu bitir
            clear_console()
            print("\n\nYou DIED!\n\n")
            break

        print(f"WRONG!\nYou have {leftLives} left")