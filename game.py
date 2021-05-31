import random

word_list = ['ÊËŞ×', 'ÊÍÈÃÀ', 'ÅÍÎÒ', 'ÌÀØÈÍÊÀ', 'ÊÎĞÎÂÀ', 'ÒÅËÅÆÊÀ', 'ØËÅÌ', 'ÊÍÎÏÊÀ', 'ØÍÓĞ', '×ÅĞÍÛÉ', 
'ÂËÀÑÒÅËÈÍ', 'ÑÊÀÉÏ', 'ÄÓÁ', '×ÀÑÛ', 'ÒĞÓÁÀ', 'ÅËÊÀ', 'ÈÍÑÒÈÒÓÒ', 'ÊÎĞÎÁÊÀ', 'ÒÀÁËÈ×ÊÀ', 'ÂÎÄÀ', 'ÑÊÎÂÎĞÎÄÀ', 
'ÌÍÎÃÎÍÎÆÊÀ', 'ÅÂĞÅÉ', 'ÒÅĞÌÈÒ', 'ÊÀ×ÅÊ', 'ĞÓËÎÍ', 'ÌÀÃÍÈÒÎÔÎÍ', 'ÍÎÃÀ', 'ÑËÎÍ', 'ÌÈÊĞÎÂÎËÍÎÂÊÀ', 'ÒÎĞÒ', 'ÌÀÊ', 
'ÄÛÌ', '×ÀÉÊÀ', 'ÂÀËÅÒ', 'ÏËÈÍÒÓÑ', 'ØÀÏÊÀ', 'ÄÈÍÎÇÀÂĞ', 'ÒÎĞØÅĞ', 'ÁÀËÀËÀÉÊÀ', 'ÁÀÍÊÀ', 'ßÕÒÀ', 'ÎÂÖÀ', 'ÁÀÍÀÍ', 
'ÄÓÁ', 'ÀÍÈÌÅ', 'ĞÀÄÓÃÀ', 'ÁÓÊÂÀ', 'ÂÅËÎÑÈÏÅÄ', 'ÁÀÍÄÆÎ', 'ÃÎËÓÁÜ', 'ÂÈÍÒÎÂÊÀ', 'ÊÓÁÎÊ', 'ÆÀÑÌÈÍ', 'ÒÅËÅÔÎÍ', 
'ÀÍÄĞÎÈÄ', 'ÃÎĞÀ', 'ÕÀËÀÒ', 'ÆÅÒÎÍ', 'ÎÁÎÄ', 'ÌÛËÎ', 'ÉÎÃ', 'ØÈØÊÀ', 'ÄÎËËÀĞ', 'ÊÎËÎÍÊÀ', 'ÊÓÁÈÊ', 'ÎÌÀĞ', 
'ĞÀÊÅÒÀ', 'ÌÎĞÊÎÂÊÀ', 'ÇÅĞÊÀËÎ', 'ÌÎËÎÒ', 'ÂÎÇÄÓÕ', 'ÇÌÅÉ', '¨Æ', 'ÏÀËÜÌÀ', 'ÌÀÑËÎ', 'ÄÈÄÆÅÉ', 'ÌÅØÎÊ', 'ÒŞÁÈÊ', 
'ÌÎÇÃ', 'ÏÎÅÇÄ', 'ĞÎÇÅÒÊÀ', 'ÏÀĞÀØŞÒÈÑÒ', 'ÁÅËÊÀ', 'ØÏĞÎÒÛ', 'ÑÀÌÎÑÂÀË', 'ÏÀÇË', 'ÁÓÒÛËÊÀ', 'ÊĞÅÌËÜ', 'ÏÈÖÖÀ', 
'ÌÀÊÀĞÎÍÛ', 'ÊÎÂÅĞ', 'ÇÓÁÛ', 'ßĞËÛÊ', 'ÊÀØÀËÎÒ', 'ÌÀĞÑ', 'ØÀÊÀË', 'ÏÎÌÀÄÀ', 'ÄÆÈÏ', 'ËÅÙ', 'ÊÀÌÅÍÜ', 'ÄÈÑÊ']


def get_word():
    return word_list[random.randrange(len(word_list))].upper()

def not_again():
    while True:
        s = input().lower()
        if s == 'y':
            return False
        elif s == 'n':
            return True
        print("Don't undesrtand you")
            
# ôóíêöèÿ ïîëó÷åíèÿ òåêóùåãî ñîñòîÿíèÿ
def display_hangman(tries):
    stages = [  # ôèíàëüíîå ñîñòîÿíèå: ãîëîâà, òîğñ, îáå ğóêè, îáå íîãè
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # ãîëîâà, òîğñ, îáå ğóêè, îäíà íîãà
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # ãîëîâà, òîğñ, îáå ğóêè
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # ãîëîâà, òîğñ è îäíà ğóêà
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # ãîëîâà è òîğñ
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # ãîëîâà
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # íà÷àëüíîå ñîñòîÿíèå
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
def check_string():
    while True:
        guess = input("Add your guess ")
        if guess.isalpha():
            break
        print("Don't understand you")
    return guess.upper()
    


def play(word):
    print('Äàâàéòå èãğàòü â óãàäàéêó ñëîâ!')
    word_completion = ['_' for i in range(len(word))] 
    guessed_letters = []
    guessed_words = []    
    prompt = False
    tries = 6      
    while True:
        print(display_hangman(tries))
        for i in range(len(word)):
            print(word_completion[i], end=' ')
        print()
        if tries == 0:
            print('You lose. My word was', word)
            break
        if prompt == False:
            print("if you want to get prompt, add 'prompt'")                   
            
        guess = check_string()
        if guess in guessed_letters or guess in guessed_words:
            print("You've tried it")
            continue
        if len(guess) == 1:
            if guess in word:
                for i in range(len(word)):
                    if guess == word[i]:
                        word_completion[i] = guess
                print("Letter '", guess, "' is in my word ", sep='')
            else:
                print("Letter '", guess, "' isn't in my word ", sep='')
                tries -= 1
            guessed_letters.append(guess)
            if not '_' in word_completion:
                print('Ïîçäğàâëÿåì, âû óãàäàëè ñëîâî! Âû ïîáåäèëè!')
                break
            continue
        if guess == 'PROMPT':
            if prompt == True:
                print("No more, man :D")
            count = 0
            c = list()
            for i in range(len(word)):
                if word_completion[i] == '_':
                    c.append(i)
                    count += 1
            if count > 1:
                print("You get prompt")
                random_i = random.choice(c)
                word_completion[i] = word[i]
                guessed_letters.append(word[i])
            else:
                print("You need to guess last letter by yourself")
            prompt = True
            continue
        if guess == word:
            print('Ïîçäğàâëÿåì, âû óãàäàëè ñëîâî! Âû ïîáåäèëè!')
            print(word)
            break
        else:
            print("No. I have another word ")
            tries -= 1
        guessed_words.append(guess)

while True:
    word = get_word()
    play(word)
    print("Press 'y' if you want to play it again or press 'n' if you don't want do it")
    if not_again():
        break
print('Game Over')