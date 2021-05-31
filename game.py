# -*- coding: utf-8 -*-

import random

word_list = ['КЛЮЧ', 'КНИГА', 'ЕНОТ', 'МАШИНКА', 'КОРОВА', 'ТЕЛЕЖКА', 'ШЛЕМ', 'КНОПКА', 'ШНУР', 'ЧЕРНЫЙ', 
'ВЛАСТЕЛИН', 'СКАЙП', 'ДУБ', 'ЧАСЫ', 'ТРУБА', 'ЕЛКА', 'ИНСТИТУТ', 'КОРОБКА', 'ТАБЛИЧКА', 'ВОДА', 'СКОВОРОДА', 
'МНОГОНОЖКА', 'ЕВРЕЙ', 'ТЕРМИТ', 'КАЧЕК', 'РУЛОН', 'МАГНИТОФОН', 'НОГА', 'СЛОН', 'МИКРОВОЛНОВКА', 'ТОРТ', 'МАК', 
'ДЫМ', 'ЧАЙКА', 'ВАЛЕТ', 'ПЛИНТУС', 'ШАПКА', 'ДИНОЗАВР', 'ТОРШЕР', 'БАЛАЛАЙКА', 'БАНКА', 'ЯХТА', 'ОВЦА', 'БАНАН', 
'ДУБ', 'АНИМЕ', 'РАДУГА', 'БУКВА', 'ВЕЛОСИПЕД', 'БАНДЖО', 'ГОЛУБЬ', 'ВИНТОВКА', 'КУБОК', 'ЖАСМИН', 'ТЕЛЕФОН', 
'АНДРОИД', 'ГОРА', 'ХАЛАТ', 'ЖЕТОН', 'ОБОД', 'МЫЛО', 'ЙОГ', 'ШИШКА', 'ДОЛЛАР', 'КОЛОНКА', 'КУБИК', 'ОМАР', 
'РАКЕТА', 'МОРКОВКА', 'ЗЕРКАЛО', 'МОЛОТ', 'ВОЗДУХ', 'ЗМЕЙ', 'ЁЖ', 'ПАЛЬМА', 'МАСЛО', 'ДИДЖЕЙ', 'МЕШОК', 'ТЮБИК', 
'МОЗГ', 'ПОЕЗД', 'РОЗЕТКА', 'ПАРАШЮТИСТ', 'БЕЛКА', 'ШПРОТЫ', 'САМОСВАЛ', 'ПАЗЛ', 'БУТЫЛКА', 'КРЕМЛЬ', 'ПИЦЦА', 
'МАКАРОНЫ', 'КОВЕР', 'ЗУБЫ', 'ЯРЛЫК', 'КАШАЛОТ', 'МАРС', 'ШАКАЛ', 'ПОМАДА', 'ДЖИП', 'ЛЕЩ', 'КАМЕНЬ', 'ДИСК']


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
            
# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
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
    print('Давайте играть в угадайку слов!')
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
                print('Поздравляем, вы угадали слово! Вы победили!')
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
            print('Поздравляем, вы угадали слово! Вы победили!')
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