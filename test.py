from aiogram import Bot, executor, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboard_main import keyboard_menu, keyboard_yesno, keyboard_econdition, SHB, DPK, questionYesNo, ansKeyboard, questionReflex, SHB_start
from datetime import datetime
from Database import Database

db = Database('db.db')

class Register(StatesGroup):
    time = State()
    client_name = State()
    topic = State()
    QUESTION1 = State()
    moment = State()
    negative = State()
    positive = State()
    dpk = State()
    emotions = State()
    shsb = State()
    tel = State()
    shsb1 = State()
    pk = State()
    dpk1 = State()
    phase = State()
    shsb11 = State()
    shsb12 = State()
    pk1 = State()
    dpk11 = State()
    rate = State()
    extra = State()
    supervis = State()
    reflex = State()
    feelings = State()
    result = State()
    makeBetter = State()
    ans = State()

storage = MemoryStorage()

token_id = token_id
bot = Bot(token=token_id)
dp = Dispatcher(bot, storage=storage)



@dp.message_handler(text="Да, хочу")
async def reg(message: types.Message):
    await message.answer("Введите псевдоним клиента")
    await Register.client_name.set()

@dp.message_handler(state=Register.QUESTION1)
async def new(message: types.Message):
    if message.text == "Новая мишень":
        await message.answer("Какая картина представляет наихудший момент?")
        await Register.moment.set()
    elif message.text == 'Возобновление переработки':
        await message.answer("Фаза 8")
        await Register.phase.set()

@dp.message_handler(state=Register.client_name)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(client_name=answer)
    await message.answer("С какой темой клиента Вы работали?")

    await Register.topic.set()


@dp.message_handler(state=Register.topic)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(time=datetime.now().strftime("%m/%d/%Y, %H:%M"))
    await state.update_data(topic=answer)
    await message.answer("Выберите:", reply_markup=keyboard_econdition)
    await Register.QUESTION1.set()






@dp.message_handler(state=Register.moment)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(moment=answer)
    await message.answer("Негативная когниция")
    await Register.negative.set()


@dp.message_handler(state=Register.negative)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(negative=answer)
    await message.answer("Позитивная когниция")
    await Register.positive.set()


@dp.message_handler(state=Register.positive)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(positive=answer)
    await message.answer("ДПК", reply_markup=DPK)
    await Register.dpk.set()


@dp.message_handler(state=Register.dpk)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(dpk=answer)
    await message.answer("Эмоции")
    await Register.emotions.set()


@dp.message_handler(state=Register.emotions)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(emotions=answer)
    await message.answer("ШСБ в начале", reply_markup=SHB_start)
    await Register.shsb.set()

@dp.message_handler(state=Register.shsb)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(shsb=answer)
    await message.answer("Телесные ощущения")
    await Register.tel.set()


@dp.message_handler(state=Register.tel)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(tel=answer)
    await message.answer("ШСБ финальное", reply_markup=SHB)
    await Register.shsb1.set()


@dp.message_handler(state=Register.shsb1)
async def new(message: types.Message, state: FSMContext):
    global res
    if message.text == "Незавершенная переработка":
        answer = message.text
        await state.update_data(shsb1=answer)

        # data = await state.get_data()
        # moment = data.get("moment")
        # negative = data.get("negative")
        # positive = data.get("positive")
        # dpk = data.get("dpk")
        # emotions = data.get("emotions")
        # shsb = data.get("shsb")
        # tel = data.get("tel")
        # shsb1 = data.get("shsb1")

        await Register.rate.set()
        await message.answer("Как прошла сессия EMDR? Что важного про процесс запомнить?")
    else:
        answer = message.text

        await state.update_data(shsb1=answer)
        await message.answer("ПК в финале")
        await Register.pk.set()


@dp.message_handler(state=Register.pk)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(pk=answer)
    await message.answer("ДПК")
    await Register.dpk1.set()



@dp.message_handler(state=Register.dpk1)
async def new(message: types.Message, state: FSMContext):
    global res
    answer = message.text

    await state.update_data(dpk1=answer)
    # data = await state.get_data()
    # moment = data.get("moment")
    # negative = data.get("negative")
    # positive = data.get("positive")
    # dpk = data.get("dpk")
    # emotions = data.get("emotions")
    # shsb = data.get("shsb")
    # tel = data.get("tel")
    # shsb1 = data.get("shsb1")
    # pk = data.get("pk")
    # dpk1 = data.get("dpk1")

    await message.answer("Как прошла сессия EMDR? Что важного про процесс запомнить?")
    await Register.rate.set()





@dp.message_handler(state=Register.phase)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(phase=answer)
    await message.answer("ШСБ в начале", reply_markup=SHB_start)
    await Register.shsb11.set()

@dp.message_handler(state=Register.shsb11)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(shsb11=answer)
    await message.answer("ШСБ финальное", reply_markup=SHB)
    await Register.shsb12.set()

@dp.message_handler(state=Register.shsb12)
async def new(message: types.Message, state: FSMContext):
    global res
    if message.text == "Незавершенная переработка":
        answer = message.text
        await state.update_data(shsb12=answer)

        # data = await state.get_data()
        #
        # phase = data.get("phase")
        # shsb11 = data.get("shsb11")
        # shsb12 = data.get("shsb12")

        # await state.finish()
        await Register.rate.set()
    else:
        answer = message.text

        await state.update_data(shsb1=answer)
        await message.answer("ПК в финале")
        await Register.pk1.set()

@dp.message_handler(state=Register.pk1)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(pk1=answer)
    await message.answer("ДПК", reply_markup=SHB)
    await Register.dpk11.set()

@dp.message_handler(state=Register.dpk11)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(dpk11=answer)

    await state.finish()
    await message.answer("Как прошла сессия EMDR? Что важного про процесс запомнить?")
    await Register.rate.set()


@dp.message_handler(state=Register.rate)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(rate=answer)
    await message.answer("Есть ли дополнительные воспоминания , отмеченные для последующей работы?")
    await Register.extra.set()

@dp.message_handler(state=Register.extra)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(extra=answer)
    await message.answer("Есть ли вопрос на супервизию?\nЕсли есть, просто введите его", reply_markup=questionYesNo)
    await Register.supervis.set()

@dp.message_handler(state=Register.supervis)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(supervis=answer)
    await message.answer("Хотите отрефлексировать сессию глубже?", reply_markup=questionReflex)
    await Register.reflex.set()


@dp.message_handler(state=Register.reflex)
async def new(message: types.Message, state: FSMContext):
    global res
    answer = message.text
    await state.update_data(reflex=answer)
    if answer == "Да, хочу отрефлексировать":
        await message.answer("Мои чувства после сессии")
        await Register.feelings.set()
    else:
        data = await state.get_data()
        tg_id = message.from_user.id
        time = data.get("time")
        client_name = data.get("client_name")
        topic = data.get("topic")
        moment = data.get("moment")
        phase = data.get("phase")
        negative = data.get("negative")
        positive = data.get("positive")
        dpk = data.get("dpk")
        emotions = data.get("emotions")
        shsb = data.get("shsb")
        tel = data.get("tel")
        shsb1 = data.get("shsb1")
        pk = data.get("pk")
        dpk1 = data.get("dpk1")

        phase = data.get("phase")
        shsb11 = data.get("shsb11")
        shsb12 = data.get("shsb12")
        pk1 = data.get("pk1")
        dpk11 = data.get("dpk11")

        rate = data.get("rate")
        extra = data.get("extra")
        supervis = data.get("supervis")
        reflex = data.get("reflex")
        feelings = data.get("feelings")
        result = data.get("result")
        makeBetter = data.get("makeBetter")
        ans = data.get("ans")
        db.add(tg_id, time, client_name, topic, moment, negative, positive, dpk, emotions, shsb, tel, shsb1, pk, dpk1,
               shsb11, shsb12, pk1,
               dpk11, rate, extra, supervis, reflex, feelings, result, makeBetter, ans, phase)

        print(tg_id, time, client_name, topic, moment, negative, positive, dpk, emotions, shsb, tel, shsb1, pk, dpk1,
              shsb11, shsb12, pk1,
              dpk11, rate, extra, supervis, reflex, feelings, result, makeBetter, ans, phase)
        await state.finish()

        await message.answer("=)", reply_markup=keyboard_menu)

        await message.answer("Спасибо, все записал! До встречи. С любовью, Ваш бот.")
        await state.finish()
        await message.answer("=)", reply_markup=keyboard_menu)


@dp.message_handler(state=Register.feelings)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(feelings=answer)
    await message.answer("Что получилось?")
    await Register.result.set()


@dp.message_handler(state=Register.makeBetter)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(makeBetter=answer)
    await message.answer("Что бы хотелось сделать лучше? Чему я учусь? Что мне нужно узнать?")
    await Register.result.set()

@dp.message_handler(state=Register.result)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(result=answer)
    await message.answer("Что бы хотелось сделать лучше? Чему я учусь? Что мне нужно узнать?")
    await Register.ans.set()

@dp.message_handler(state=Register.ans)
async def new(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(ans=answer)

    data = await state.get_data()
    tg_id = message.from_user.id
    time = data.get("time")
    client_name = data.get("client_name")
    topic = data.get("topic")
    moment = data.get("moment")
    phase = data.get("phase")
    negative = data.get("negative")
    positive = data.get("positive")
    dpk = data.get("dpk")
    emotions = data.get("emotions")
    shsb = data.get("shsb")
    tel = data.get("tel")
    shsb1 = data.get("shsb1")
    pk = data.get("pk")
    dpk1 = data.get("dpk1")

    phase = data.get("phase")
    shsb11 = data.get("shsb11")
    shsb12 = data.get("shsb12")
    pk1 = data.get("pk1")
    dpk11 = data.get("dpk11")

    rate = data.get("rate")
    extra = data.get("extra")
    supervis = data.get("supervis")
    reflex = data.get("reflex")
    feelings = data.get("feelings")
    result = data.get("result")
    makeBetter = data.get("makeBetter")
    ans = data.get("ans")
    db.add(tg_id,time, client_name, topic, moment, negative, positive, dpk,emotions, shsb, tel,shsb1, pk, dpk1, shsb11, shsb12, pk1,
                                   dpk11, rate, extra, supervis, reflex, feelings,result, makeBetter, ans, phase)

    print(tg_id,time, client_name, topic, moment, negative, positive, dpk,emotions, shsb, tel,shsb1, pk, dpk1, shsb11, shsb12, pk1,
                                   dpk11, rate, extra, supervis, reflex, feelings,result, makeBetter, ans, phase)
    await state.finish()

    await message.answer("=)", reply_markup=keyboard_menu)


@dp.message_handler()
async def main(message: types.Message):

    if message.text == '/start':
        await message.answer("=)", reply_markup=keyboard_menu)
    elif message.text == "Сделать запись":
        await message.answer(f'Хотите сделать запись EMDR сессии от {datetime.now().strftime("%m/%d/%Y, %H:%M")}?',
                             reply_markup=keyboard_yesno)
    elif message.text == "Получить результаты":
        data = [data[0] for data in db.getClient(message.from_user.id)]
        await message.answer(f'Введите имя клиента из данного списка:  {data}')
    elif message.text in [data[0] for data in db.getClient(message.from_user.id)]:
        import csv
        with open('data.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            for data in db.getClientInfo(message.text):
                writer.writerow(data)
            f.close()
        await bot.send_document(message.chat.id,  open('data.csv', 'rb'))









if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)