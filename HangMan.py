import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def printList(x):
    plainText = ""
    for ch in x:
        plainText+=ch
    print(plainText)
randomList = ["day","weak","month","year"]
choosenWord = random.choice(randomList)
print(choosenWord)
guessWord = ""

for x in choosenWord:
    guessWord+="_"
print(guessWord)

gameover = False 
correctWord = []
count=0
while not gameover and count<7:
    userInput = input("Guess the word:- ")
    display = ""
    theTruth=False
    for x in choosenWord:
        if x == userInput:
            correctWord.extend(x)
            display+=x
        elif x in correctWord:
            display+=x
        else:
            display+="_"
    print(display)
    if "_" not in display:
        print("You win the match")
        gameover=True
    if userInput not in choosenWord and userInput not in correctWord:
        print(HANGMANPICS[count])
        count+=1


    
# count = 0
# while(count < len(choosenWord)):
#     userInput = input("Guess the word:- ")
#     for x in choosenWord:
#         if x == userInput:
#             indexNo = choosenWord.index(x)
#             guessWordList[indexNo] = x
#             count+=1
#     printList(guessWordList)

