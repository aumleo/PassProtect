import random 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word = ['forest', 'butter', 'tea']
chosen_word= random.choice(word)
lives=6

print(f'word ={chosen_word}')

display=[]
for chr in chosen_word:
    display.append('_')

while display.count('_')>0:

    guess=input('Guess: ').lower()

    for position in range(len(chosen_word)):
        if guess==chosen_word[position]:
            display[position]=guess
    if guess not in chosen_word:
        lives-=1
        if lives== 0:
            print(stages[lives])
            print('YOU LOSE')
            break
            
             
    else:
        print (''.join(display))
        if '_' not in display:
            print('YOU WIN')
            break
    
    print (stages[lives])



