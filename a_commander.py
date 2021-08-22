import random
from commander_info import command_info


def command_luck(event, line):
    if(random.random==1):
        return 'удача'
    else:
        return 'неудача'


def command_buy(event, line):
    return "Магазин закрыт на обед"


def command_help(event, line):
    return 'Помощь\nУспех\nКупить\nСправка'


# main commander
def commander(event):

    commands = {
        'купить': command_buy,
        'помощь': command_help,
        'успех': command_luck,
        'справка': command_info
    }

    output = "\n"

    lines = event.object.message["text"].split("\n")
    for line in lines:
        words = line.split(" ")
        if len(words) == 1:
            output += 'Введите "Джонни помощь" для выведения списка команд \n'
        elif words[1] in commands:
            output += commands.get(words[1])(event, line) + "\n"

#    if peer_id == user_id:
#        group_status = 0 #личные сообщения
#    elif peer_id == 2000000001:
#        group_status = 1 #разрешённая группа
#    else:
#        group_status = 2 #запрещённая группа
#        return "Запрещённая группа"
    namecheck = lines[0].split(" ")
    print(namecheck)
    if namecheck[0] == "джонни" or namecheck[0] == "джонни,":
        if output == "\n":
            output = "Команды не распознаны"
        return output
