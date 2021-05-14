digit_by_text = input('Введите цифру от 0 до 10 на английском языке для перевода на русский: ')
translation_dictionary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
def num_translate(figure):
    if figure in translation_dictionary:
        print(translation_dictionary[figure])
    else:
        figure = figure.lower()
        if figure in translation_dictionary:
            capital_letter = translation_dictionary[figure].capitalize()
            print(capital_letter)
        else:
            print(None)
            
num_translate(digit_by_text)
