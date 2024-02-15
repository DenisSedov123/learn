documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_name():
    number = input('Введите номер документа ')
    for data in documents:
        if data.get("number") == number:
            return data.get('name')
    return 'Документа с таким номером нет'


def get_shelf():
    number = input('Введите номер документа ')
    for key in directories:
        if number in directories.get(key):
            return f'Документ хранится на полке: {key}'
    return 'Документ не найден в базе.'

def get_key(d, value):
    for k, v in d.items():
        if value in v:
            return k
def get_list():
    for c in documents:
        doc_type = c['type']
        number = c['number']
        name = c['name']
        return '№: {1}, тип: {0}, владелец: {2} полка хранения: {3}'.format(doc_type, number, name, get_key(directories,
                                                                                                   number))



def add_shelf():
    shelf = input('Введите номер полки: ')
    if shelf not in directories:
        directories[shelf] = []
        print(f'Полка добавлена. Текущий перечень полок:{", ".join(list(directories.keys()))}')
    else:
        print(f'Такая полка уже существует. Текущий перечень полок: {", ".join(list(directories.keys()))}')

def del_shelf():
    shelf = input('Введите номер полки: ')
    if shelf in directories.keys() and len(directories.values()) > 0:
        print(len(directories.values()))
        print(f'На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: {", ".join(list(directories.keys()))} ')
    elif shelf in directories.keys() and len(directories.values()) == 0:
        print(f'Полка удалена. Текущий перечень полок: {", ".join(list(directories.keys()))}')



while True:
    comand = input('Введите название команды ')

    if comand == 'p':
        print(get_name())

    elif comand == 's':
        print(get_shelf())

    elif comand == 'l':
        print(get_list())

    elif comand == 'ads':
        print(add_shelf())
    elif comand == 'ds':
        print(del_shelf())
    elif comand == 'ad'
        add_doc()
    elif comand == 'q':
        break


