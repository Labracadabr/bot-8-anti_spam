import json
from aiogram.types import Message
from aiogram.filters import BaseFilter
from aiogram.filters.state import State, StatesGroup
# import requests
# import os
from settings import *
from aiogram import Router, Bot, F, types
from config import Config, load_config


router: Router = Router()
config: Config = load_config()
TKN: str = config.tg_bot.token
bot: Bot = Bot(token=config.tg_bot.token)

# Запись данных item в указанный json file по ключу key
def log(file, key, item):
    with open(file, encoding='utf-8') as f:
        data = json.load(f)

    data.setdefault(str(key), []).append(item)

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# Запись данных item в указанный json file по ключу key
async def log(file, key, item):
    try:  # сохр в жсон
        with open(file, 'r+', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:  # если жсона нет
        data = {}
    data.setdefault(str(key), []).append(item)
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    log_text = str(key)+' '+str(item)
    print(log_text)

    try:  # дублировать логи в тг-канал
        await bot.send_message(chat_id=log_channel_id, text=log_text) if log_channel_id else None
    except Exception as e:
        print('channel error', e)


# Фильтр, проверяющий доступ юзера
class Access(BaseFilter):
    def __init__(self, access: list[str]) -> None:
        # В качестве параметра фильтр принимает список со строками
        self.access = access

    async def __call__(self, message: Message) -> bool:
        user_id_str = str(message.from_user.id)
        return user_id_str in self.access


# # Состояния FSM
# class FSM(StatesGroup):
#     # Состояния, в которых будет находиться бот в разные моменты взаимодействия с юзером
#     policy = State()            # Состояние ожидания соглашения с policy
#     platform_user_id = State()  # Состояние ожидания ввода id
#     upload_photo = State()      # Состояние ожидания загрузки фото
#     upload_2_photo = State()    # Состояние ожидания загрузки ДВУХ фото
#     waiting_verif = State()     # Юзер всё скинул и ждет код

