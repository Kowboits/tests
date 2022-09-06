documents = [
        {"type": "passport", "number": '2207 876234', "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}
help = ['p – выведет имя человека по номеру документа',
       's –  выведет номер полки, на которой находится документ',
       'l – список всех документов',
       'a – добавит новый документ в каталог и в перечень полок',
       'd – удалит документ из каталога и из перечня полок.',
        'm – переместит документ с текущей полки на целевую.',
        'as – добавление новой полки',
        'pd - печать перечня полок',
        'q - выход']

def help_print(): #Вызов справки
    print(*help, sep= '\n')
    return ''

def print_selfs(): # Печать полок
    print(directories)
    return ''

def name_serch(): # поиск имени по номеру документа
    doc_number = input('Введите номер документа:')
    for doc in  documents:
        if doc_number == doc["number"]:
            return (f'Документ на имя: {doc["name"]}')
            break
    else:
        return ('Документа с таким номером не найдено')

def shelf_search(): # поиск полки по номеру документа
    doc_number = input('Введите номер документа:')
    for shelf in directories.keys():
        if doc_number in directories[shelf]:
            return (f'Документ на полке №:{shelf}')
            break
    else:
        return ('Документа с таким номером не найдено')

def list_print(): # вывод всех данных из списка документов
    for doc in documents:
        full_list = []
        for i in doc.keys():
            full_list.append(doc[i])
        print(*full_list)
    return ''

def documents_update(): # добавление новой записи в список данных
    doc_type = input('Введите тип документа:')
    doc_num = input('Введите номер документа:')
    new_name = input('Введите ФИО(полностью) через пробел:')
    self_storage = input('Введите номер полки для храниения:')
    if self_storage in directories.keys():
        documents.append({"type": doc_type, "number": doc_num, "name": new_name})
        directories[self_storage].append(doc_num)
    else:
        return ('Некорректный номер полки')
    return ('база данных обновлена')

def doc_remove(): # удаление записи из базы
    doc_number = input('Введите номер документа:')
    for doc in documents:
        if doc_number == doc["number"]:
            documents.remove(doc)
            break
    else:
        return ('Введен некорректный номер документа')
    for shelf in directories.keys():
        if doc_number in directories[shelf]:
            directories[shelf].remove(doc_number)
    return ('данные обновлены')

def doc_movement(): #Перемещение документа с полки на полку
    doc_number = input('Введите номер документа:')
    new_shelf = input('Введите на которую переместить документ:')
    for shelf in directories.keys():
        if doc_number in directories[shelf] and new_shelf in directories.keys():
            directories[shelf].remove(doc_number)
            break
    else:
        return ('Ошибка: проверьте номер документа или номер полки для перемещения')
    if new_shelf in directories.keys():
        directories[new_shelf].append(doc_number)
        return ('Данные обновлены')

def add_self(): #Добавление новой полки
    new_self = input('Ведите номер полки для добавления:')
    if new_self not in directories.keys():
        directories[new_self] = []
        return ('Полка добавлена')
    else:
        return ("Такая полка уже сужествует")



instructions = {
    'p': name_serch,
    's': shelf_search,
    'l': list_print,
    'a': documents_update,
    'd': doc_remove,
    'm': doc_movement,
    'as': add_self,
    'h': help_print,
    'pd': print_selfs

}
# print('Для вызова справки введите h')
# request = ''
# while request.lower() != 'q':
#     request = input('Введите команду:')
#     if request.lower() in instructions.keys():
#         print(instructions[request.lower()]())