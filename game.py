import random

word_list = ['����', '�����', '����', '�������', '������', '�������', '����', '������', '����', '������', 
'���������', '�����', '���', '����', '�����', '����', '��������', '�������', '��������', '����', '���������', 
'����������', '�����', '������', '�����', '�����', '����������', '����', '����', '�������������', '����', '���', 
'���', '�����', '�����', '�������', '�����', '��������', '������', '���������', '�����', '����', '����', '�����', 
'���', '�����', '������', '�����', '���������', '������', '������', '��������', '�����', '������', '�������', 
'�������', '����', '�����', '�����', '����', '����', '���', '�����', '������', '�������', '�����', '����', 
'������', '��������', '�������', '�����', '������', '����', '��', '������', '�����', '������', '�����', '�����', 
'����', '�����', '�������', '����������', '�����', '������', '��������', '����', '�������', '������', '�����', 
'��������', '�����', '����', '�����', '�������', '����', '�����', '������', '����', '���', '������', '����']


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
            
# ������� ��������� �������� ���������
def display_hangman(tries):
    stages = [  # ��������� ���������: ������, ����, ��� ����, ��� ����
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # ������, ����, ��� ����, ���� ����
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # ������, ����, ��� ����
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # ������, ���� � ���� ����
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # ������ � ����
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # ������
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # ��������� ���������
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
    print('������� ������ � �������� ����!')
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
                print('�����������, �� ������� �����! �� ��������!')
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
            print('�����������, �� ������� �����! �� ��������!')
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