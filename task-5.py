
from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_of_jokes = []
def get_jokes(n, flag = False):
    """Создаем переменную, в которую поместим n - количество загадок"""
    joke = []
    """Проверяем пустые списки или нет, для рандомного построения шустки"""
    for _ in range(n):
        if (len(nouns) != 0) and (len(adverbs) != 0) and (len(adjectives) != 0):
            random_nouns = choice(nouns)
            random_adverbs = choice(adverbs)
            random_adjective = choice(adjectives)
            joke.append(f'{random_nouns} {random_adverbs} {random_adjective}')
            """Проверяем переданную переменную. Выполняем проверку использованных слов со списком и удаляем их из него"""
            if flag == True:
                k = ''.join(joke)
                list_of_jokes = k.split()
                for noun in nouns:
                    for jokes in list_of_jokes:
                        if noun == jokes:
                            nouns.remove(noun)
                for adverb in adverbs:
                    for jokes in list_of_jokes:
                        if adverb == jokes:
                            adverbs.remove(adverb)
                for adjective in adjectives:
                    for jokes in list_of_jokes:
                        if adjective == jokes:
                            adjectives.remove(adjective)
        else:
            print('Оставшиеся шутки на сегодня: ')
            break
    print(joke)
    if (len(nouns) != 0) and (len(adverbs) != 0) and (len(adjectives) != 0):
        digit_by_text = input('Хотите повторить? ')
        if digit_by_text == 'да':
            kol = input('Введите количество шуток: ')
            get_jokes(int(kol), flag = True)
    else:
        print('Хорошего вам дня!')
            
get_jokes(3, flag = True)
