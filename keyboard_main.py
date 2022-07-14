from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Сделать запись'),
            KeyboardButton(text='Получить результаты')

        ],

    ], resize_keyboard=True
)


keyboard_yesno = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Да, хочу'),
            KeyboardButton(text='Нет, не хочу')

        ],

    ], resize_keyboard=True
)


keyboard_econdition = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Новая мишень'),
            KeyboardButton(text='Возобновление переработки')

        ],

    ], resize_keyboard=True
)

SHB_start = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='0'),
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3')
        ],[
            KeyboardButton(text='4'),
            KeyboardButton(text='5'),
            KeyboardButton(text='6'),
            KeyboardButton(text='7')
        ],
    [
            KeyboardButton(text='8'),
            KeyboardButton(text='9'),
            KeyboardButton(text='10'),
        ],

    ], resize_keyboard=True
)

SHB = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='0'),
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3')
        ],[
            KeyboardButton(text='4'),
            KeyboardButton(text='5'),
            KeyboardButton(text='6'),
            KeyboardButton(text='7')
        ],
    [
            KeyboardButton(text='8'),
            KeyboardButton(text='9'),
            KeyboardButton(text='10'),
        ],
        [
            KeyboardButton(text="Незавершенная переработка")
        ]



    ], resize_keyboard=True
)


DPK = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3')
        ],[
            KeyboardButton(text='4'),
            KeyboardButton(text='5'),
            KeyboardButton(text='6'),
            KeyboardButton(text='7')
        ],

    ], resize_keyboard=True
)


questionYesNo = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Нет вопросов')

        ],

    ], resize_keyboard=True
)

questionReflex = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Да, хочу отрефлексировать'),
            KeyboardButton(text='Не сейчас'),


        ],

    ], resize_keyboard=True
)

ansKeyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Все'),
            KeyboardButton(text='По клиенту'),


        ],

    ], resize_keyboard=True
)