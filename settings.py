import os

# tg id админов
dima: str = "992863889"

# Список id админов
admins: list[str] = [dima]

# где хранятся данные. тк я не умею в субд, то это просто json
baza = 'baza.json'
logs = 'logs.json'
userdata = 'users.json'

# tg канал для логов
log_channel_id = ''

# # игнорить ли сообщения, присланные во время отключения бота
# ignor: bool = False

# проверить все ли ок
file_list = [baza, logs, userdata]
for file in file_list:
    if not os.path.isfile(file):
        if file.endswith('json'):
            with open(file, 'w', encoding='utf-8') as f:
                print('Отсутствующий файл создан:', file)
                print('{}', file=f)


print('OK')
