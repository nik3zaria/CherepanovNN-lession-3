employee_names = ("Иван Сергеевич", "Мария Петровна", "Петр Ильич", "Илья Максимов", "Анастасия Сергеевна", "Юлия Владимировна")
def thesaurus(employee_names):
    employee_names_sorted = {}
    dictionary_of_names = {}
    for name in employee_names:
        key = name[0].capitalize()
        if key not in dictionary_of_names:
            dictionary_of_names[key] = []
        dictionary_of_names[key].append(name)
    employee_names_key = sorted(dictionary_of_names, key=dictionary_of_names.get)
    for x in employee_names_key:
        employee_names_sorted[x] = dictionary_of_names[x]
    return print(dictionary_of_names, end = ' --> '), print(employee_names_sorted)
print(thesaurus(employee_names))
