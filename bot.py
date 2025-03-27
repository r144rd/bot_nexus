# https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg
# 8005793509:AAElxfP9IfkZtPUQb5pWiQ-lEVS2rD_g1S8
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = '8005793509:AAElxfP9IfkZtPUQb5pWiQ-lEVS2rD_g1S8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Состояния для слайдера мероприятий
class EventSliderStates(StatesGroup):
    event_index = State()

# Список мероприятий
events = [
    {
        "title": "⚡️Новые победы⚡️",
        "description": """⚡️Новые победы⚡️
    📌Сегодня состоялось награждение участников Регионального этапа чемпионата «Профессионалы».
    ✔В компетенции «Разработка виртуальной и дополненной реальности» от нашего центра принимал участие Вахрушин Станислав, который занял 3 место💫🌟 Поздравляем!!
    Желаем не останавливаться на достигнутом и постигать новые вершины 🏆
    Благодарим за подготовку педагога доп. образования Воеводина Вячеслава Александровича🥳""",
        "image": "https://sun9-74.userapi.com/s/v1/ig2/-AmE-7PBWiuClsWI005D8S476dOAysf5cRzqBdlVULZZg4WX_ks-iFxeFIvP7kZmvF0fmFkovvhSjoK-XIC5EVaB.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,960x1280&from=bu&u=o-fld_zSIX18I7bdOORC2ZXEkLt7iXVbZIvAI11cDHU&cs=960x1280"
    },
    {
        "title": "⚡️С 10 по 14 марта прошел Региональный этап чемпионата «Профессионалы» по компетенции «Разработка виртуальной и дополненной реальности»⚡️",
        "description": """📌Его участниками стали 6 человек и с ними эксперты-наставники из 5 образовательных учреждений области, из которых 3 Центра цифрового образования детей (Нижегородского радиотехнического колледжа, Арзамасского техникума строительства и предпринимательства и Княгининского университета) и детский технопарк «Кванториум.Нижний Новгород», а также школы № 132 г. Н. Новгорода.
    ✔От нашего центра принял участие Вахрушин Станислав под наставничеством педагога дополнительного образования Воеводина Вячеслава Александровича.
    📌Результаты и призовые места каждый сможет узнать только 18 марта на церемонии закрытия соревнований Регионального этапа, которая состоится в Технопарке «Анкудиновка».
    Только один участник, который займет первое место, сможет представлять наш регион в финале Соревнований🏆""",
        "image": "https://sun83-1.userapi.com/impg/500H2GViCgX-xbssjducGMFCcpEPKjnKIxJTqA/SWtNy9vlclc.jpg?size=1280x853&quality=95&sign=cf72b2307eae158d4d83205ea61e1d22&type=album"
    },
    {
        "title": "⚡Итоги: «IT-SURPRISE IV»⚡",
        "description": """🖇В конкурсе приняло участие более 350 человек со всей России🇷🇺
    Благодарим всех за участие 🏆
    С итогами конкурса можно ознакомиться во вложении📋
    Рассылка сертификатов и дипломов участникам будет осуществляться 14 АПРЕЛЯ на адрес электронной почты, указанной в электронной форме при регистрации.""",
        "image": "https://sun83-1.userapi.com/impg/5Haj7C80IBVudlxwB29aB8B3NdXglRd2_sfytQ/m1agXjswC5I.jpg?size=1280x1033&quality=95&sign=e930f0f31331f6b448a4e66ae0a99b3e&type=album"
    },
    {
        "title": "⚡️Мастер-классы «Цифровые каникулы»⚡️",
        "description": """
✔️Сегодня педагоги нашего центра провели увлекательные мастер-классы и познакомили ребят с деятельностью нашего центра. 
✔️Ребята попробовали создать игру «Змейка», познакомились с направлением «Web-разработка» и роботами-манипуляторами DoBOT»🕹️🖥️""",
        "image": "https://sun9-32.userapi.com/impg/J2B9L1LhBUVCm5njtYQavxfKmb4R_PBzjltwIQ/vvNSgdZFt3w.jpg?size=1280x994&quality=95&sign=739202f875c94127f884343117160c8a&type=album"
    },
    {
        "title": "⚡️Новые победы⚡️",
        "description": """Сегодня наши ребята приняли участие в робототехническом марафоне «Сумо за выживание», который прошел в рамках фестиваля «ТехноФест-Нижний Новгород». 
        В средней категории 1 место заняли: 
        🥇Гущин Андрей;
        🥇Чаров Марк.
        В старшей категории 1 место занял: 
        🥇Железнов Тимофей.
        Поздравляем ребят с победой 🎊🥳 Благодарим педагога дополнительного образования Воронцова Алексея Анатольевича🏆""",
        "image": "https://sun9-77.userapi.com/impg/_3IE79_7B_hmVfiCJgY58FK1CYLGn3CFe7h-5A/js8Erzqpqug.jpg?size=1280x960&quality=95&sign=2654dbd46a506649b037297a0e2ba943&type=album"
    },
    {
        "title": "⚡Продолжается набор: открыты новые группы⚡",
        "description": """
📌Scratch Junior (6-7 лет)
Группа: АЛ-1
Расписание: ПН, ЧТ 15.30-17.00
Ссылка: xn--52-kmc.xn--80aafey1amqq.xn--d1acj3b/program/40... 
📌Основы алгоритмики и логики (8-11 лет)
Группа: ПР/М-1
Расписание: СР, ПТ 15.30-17.00
Ссылка: xn--52-kmc.xn--80aafey1amqq.xn--d1acj3b/program/40... 
Продолжается набор в следующие группы:
📌Медиа. Основы создания цифрового контента (13-17 лет)
Группа: М-1
Расписание: СР 15.30 - 17.00 (раз в 2 недели до 17.50), СБ 09.50 - 11.20
Ссылка: xn--52-kmc.xn--80aafey1amqq.xn--d1acj3b/program/36...  """,
        "image": "https://sun9-2.userapi.com/s/v1/ig2/bc1eBhzFaKgjzZYYknDS5Rn0OhNAc0NS0iNprusNkxbYT3jFyyUZIvGeyhvIIQmGrSqJOzFJrcXeLYTK11bYQlJz.jpg?quality=95&as=32x32,48x48,72x72,108x108,160x160,240x240,360x360,480x480,540x540,640x640,720x720,1080x1080,1280x1280,1440x1440,2480x2480&from=bu&u=Vs6xb3oUoqyYcubDva_-JwudJS-A1NL3TE_apcGLYQ8&cs=1280x1280"
    }
]

# Стартовое состояние
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer_photo(photo='https://sun9-33.userapi.com/impg/BJ9AYKKFnvbwruq5c2VT-ikraDb0O4s1XG5qvQ/k-m-fQWyA38.jpg?size=1235x966&quality=95&sign=e4db72b83b77d7482e7529c7134f364f&type=album', caption='Добро пожаловать в нашего бота!')
    await main_menu(message.chat.id)

# Главное меню
async def main_menu(chat_id):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["📝 Общая информация 📝", "📚 Программы обучения 📚", "🗓 Расписание занятий 🗓", "📞 Контакты 📞", "📰 Мероприятия/Новости 📰", "❓ Частые вопросы ❓"]
    keyboard.add(*buttons)
    await bot.send_message(chat_id, "Выберите опцию:", reply_markup=keyboard)

# Обработка выбора "Мероприятия/Новости"
@dp.message_handler(lambda message: message.text == "📰 Мероприятия/Новости 📰")
async def events_info(message: types.Message):
    await show_event(message.chat.id, 0)  # Показываем первое мероприятие

# Функция для отображения мероприятия
async def show_event(chat_id, index):
    event = events[index]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Кнопки навигации
    if index > 0:
        keyboard.add("↩️ Назад ↩️")
    if index < len(events) - 1:
        keyboard.add("⬆️ Вперед ⬆️")
    keyboard.add("📔 Главное меню 📔")
    
    await bot.send_photo(chat_id, photo=event["image"], caption=f"{event['title']}\n\n{event['description']}", reply_markup=keyboard)
    
    # Сохраняем индекс мероприятия в состоянии
    await EventSliderStates.event_index.set()
    async with dp.current_state(user=chat_id).proxy() as data:
        data['event_index'] = index

# Обработка нажатия кнопки "Вперед"
@dp.message_handler(lambda message: message.text == "⬆️ Вперед ⬆️", state=EventSliderStates.event_index)
async def next_event(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        current_index = data.get('event_index', 0)
        if current_index < len(events) - 1:
            await show_event(message.chat.id, current_index + 1)

# Обработка нажатия кнопки "Назад"
@dp.message_handler(lambda message: message.text == "↩️ Назад ↩️", state=EventSliderStates.event_index)
async def previous_event(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        current_index = data.get('event_index', 0)
        if current_index > 0:
            await show_event(message.chat.id, current_index - 1)

# Обработка нажатия кнопки "Главное меню"
@dp.message_handler(lambda message: message.text == "📔 Главное меню 📔", state=EventSliderStates.event_index)
async def back_to_main_menu(message: types.Message, state: FSMContext):
    await state.finish()  # Завершаем текущее состояние
    await main_menu(message.chat.id)

# Обработка выбора "Общая информация"
@dp.message_handler(lambda message: message.text == "📝 Общая информация 📝")
async def general_info(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("↩️ Назад ↩️", "👨‍🏫 Преподаватели 👨‍🏫", "📍 Адрес 📍")
    await message.answer("""IT-CUBE. Нижний Новгород
«IT-CUBE» — это центр цифрового образования детей по программам, направленным на ускоренное освоение актуальных и востребованных знаний, навыков и компетенций в сфере информационных технологий. Проект формирует современную образовательную экосистему, объединяющую компании-лидеров ИТ-рынка, опытных наставников и начинающих разработчиков от 6 до 18 лет. Всё обучение в нашем центре проводится БЕСПЛАТНО.

Направления обучения:
- Основы алгоритмики и логики;
- Программирование роботов;
- Разработка виртуальной и дополненной реальности;
- Мобильная разработка;
- Программирование на языке JAVA;
- Программирование на языке PYTHON;
- Основы 3D моделирования и 3D печати;
- Основы мехатроники;
- Web-разработка;
- Медиа. Основы создания цифрового контента.

📍Телефон для связи 89915113881""", reply_markup=keyboard)

# Обработка выбора "Назад"
@dp.message_handler(lambda message: message.text == "↩️ Назад ↩️")
async def back_to_main(message: types.Message):
    await main_menu(message.chat.id)

# Обработка выбора "Преподаватели"
@dp.message_handler(lambda message: message.text == "👨‍🏫 Преподаватели 👨‍🏫")
async def teachers_info(message: types.Message):
    await message.answer("Воеводин Вячелав Александрович: Преподаватель 1\nФото: https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg")
    await message.answer("Воронцов Алексей Анатольевич: Преподаватель 2\nФото: https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg")
    await message.answer("Абиева Татьяна Михайловна: Преподаватель 3\nФото: https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg")
    await message.answer("Рябинкова Полина Николаевна: Преподаватель 4\nФото: https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg")
    await message.answer("Нажмите '↩️ Назад ↩️' для возврата в меню.")

# Обработка выбора "Адрес"
@dp.message_handler(lambda message: message.text == "📍 Адрес 📍")
async def question1(message: types.Message):
    await message.answer('Улица Генкиной, 84, Нижний Новгород')

# Обработка выбора "Расписание занятий"
@dp.message_handler(lambda message: message.text == "🗓 Расписание занятий 🗓")
async def schedule_info(message: types.Message):
    await message.answer('Расписание занятий: https://sun83-1.userapi.com/impg/jaQCOoYD_GmdllQl7dAdMyaCD9eJ_Jbj7lda9Q/URCqZ5riyuI.jpg?size=1280x905&quality=95&sign=b9a9248d8feb51a96a9a431bd5a94e0f&type=album')

# Обработка выбора "Контакты"
@dp.message_handler(lambda message: message.text == "📞 Контакты 📞")
async def contacts_info(message: types.Message):
    await message.answer("""+7 (991) 511-38-81
    telegram: @itcubenn
    https://itcube.nntc.nnov.ru/
    улица Генкиной, 84, Нижний Новгород""")

# "Программы обучения"
@dp.message_handler(lambda message: message.text == "📚 Программы обучения 📚")
async def send_programs(message: types.Message):
    programs_text = (
        "Выберите программу обучения:\n\n"
        "1. Программа по программированию:\n"
        "   - Введение в программирование\n"
        "   - Основы Python: синтаксис, переменные, типы данных\n"
        "   - Условные операторы и циклы\n"
        "   - Функции и модули\n"
        "   - Основы работы с библиотеками\n"
        "   - Проект: создание простого приложения\n\n"
        "2. Программа по робототехнике:\n"
        "   - Введение в робототехнику\n"
        "   - Основы механики и электроники\n"
        "   - Программирование микроконтроллеров\n"
        "   - Сборка и настройка робота\n"
        "   - Программирование движений и сенсоров\n"
        "   - Проект: создание автономного робота\n\n"
        "3. Программа по LEGO WeDo:\n"
        "   - Введение в LEGO WeDo\n"
        "   - Основы сборки моделей\n"
        "   - Программирование с помощью LEGO WeDo Software\n"
        "   - Использование датчиков и моторов\n"
        "   - Создание интерактивных проектов\n"
        "   - Проект: создание модели с управлением\n"
    )
    await message.answer(programs_text)

    # FAQ добавление кнопок
@dp.message_handler(lambda message: message.text == "❓ Частые вопросы ❓")
async def faq(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("↩️ Назад ↩️", "❓ Можно ли записаться, если мне нет 14? ❓",
                "❓ Сколько стоит занятия на IT-CUBE? ❓", "❓ Что такое IT-CUBE? ❓",
                "❓ КАК ЗАПИСАТЬСЯ НА ОБУЧЕНИЕ ⁉ ❓")
    await message.answer('Здесь представлены часто задаваемые вопросы.', reply_markup=keyboard)

    # FAQ 
@dp.message_handler(lambda message: message.text == "❓ Можно ли записаться, если мне нет 14? ❓")
async def question1(message: types.Message):
    await message.answer('IT-CUBE принимает всех желающий в возрасте от 6 до 18 лет.')

    # FAQ 
@dp.message_handler(lambda message: message.text == "❓ Сколько стоит занятия на IT-CUBE? ❓")
async def question2(message: types.Message):
    await message.answer('Всё обучение в нашем центре проводится БЕСПЛАТНО.')
    
    # FAQ 
@dp.message_handler(lambda message: message.text == "❓ Что такое IT-CUBE? ❓")
async def question3(message: types.Message):
    await message.answer('«IT-CUBE» — это центр цифрового образования детей по программам, направленным на ускоренное освоение актуальных и востребованных знаний, навыков и компетенций в сфере информационных технологий')
    # FAQ 
@dp.message_handler(lambda message: message.text == "❓ КАК ЗАПИСАТЬСЯ НА ОБУЧЕНИЕ ⁉ ❓")
async def question3(message: types.Message):
    await message.answer("""
                        1. Подайте заявку в «Навигаторе дополнительного образования детей Нижегородской области».
                        2. В ближайшее время с вами свяжется администратор и назначит дату и время для заполнения документов.
                        По вопросам обращайтесь к администратору по телефону - 819915113881 или пишите в поддержку""")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)