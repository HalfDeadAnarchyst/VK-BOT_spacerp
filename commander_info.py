def command_info(event, line):

    infos = {
        'ссылка': 'ru.wikipedia.org',
        'смысл_жизни': '42',
        'помощь': 'Введите искомое слово, или введите "Джонни справка список" для вывода всех заголовков'
    }

    output = '\n'
    words = line.split(" ")
    if len(words) <= 2:
        return 'Укажите раздел для справки или введите "Джонни справка помощь"'

    if words[2] == "список":
        for key in infos.keys():
            output += key + "\n"

    if words[2] in infos:
        output += infos.get(words[2]) + "\n"

    return output
