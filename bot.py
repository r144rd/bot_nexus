# Токен вашего бота
# 8005793509:AAElxfP9IfkZtPUQb5pWiQ-lEVS2rD_g1S8
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
        "title": "Хакатон 2023",
        "description": "Присоединяйтесь к нашему хакатону, где вы сможете создать уникальный проект за 48 часов!",
        "image": "https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg"
    },
    {
        "title": "Курс по Python",
        "description": "Узнайте основы программирования на Python на нашем интенсивном курсе.",
        "image": "https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg"
    },
    {
        "title": "Выставка технологий",
        "description": "Посетите выставку, где представлены последние достижения в области технологий.",
        "image": "https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg"
    }
]

# Стартовое состояние
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer_photo(photo='https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg', caption='Добро пожаловать в нашего бота!')
    await main_menu(message.chat.id)

# Главное меню
async def main_menu(chat_id):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Общая информация", "Программы обучения", "Расписание занятий", "Контакты", "Мероприятия/Новости"]
    keyboard.add(*buttons)
    await bot.send_message(chat_id, "Выберите опцию:", reply_markup=keyboard)

# Обработка выбора "Мероприятия/Новости"
@dp.message_handler(lambda message: message.text == "Мероприятия/Новости")
async def events_info(message: types.Message):
    await show_event(message.chat.id, 0)  # Показываем первое мероприятие

# Функция для отображения мероприятия
async def show_event(chat_id, index):
    event = events[index]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Кнопки навигации
    if index > 0:
        keyboard.add("Назад")
    if index < len(events) - 1:
        keyboard.add("Вперед")
    keyboard.add("Главное меню")
    
    await bot.send_photo(chat_id, photo=event["image"], caption=f"{event['title']}\n\n{event['description']}", reply_markup=keyboard)
    
    # Сохраняем индекс мероприятия в состоянии
    await EventSliderStates.event_index.set()
    async with dp.current_state(user=chat_id).proxy() as data:
        data['event_index'] = index

# Обработка нажатия кнопки "Вперед"
@dp.message_handler(lambda message: message.text == "Вперед", state=EventSliderStates.event_index)
async def next_event(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        current_index = data.get('event_index', 0)
        if current_index < len(events) - 1:
            await show_event(message.chat.id, current_index + 1)

# Обработка нажатия кнопки "Назад"
@dp.message_handler(lambda message: message.text == "Назад", state=EventSliderStates.event_index)
async def previous_event(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        current_index = data.get('event_index', 0)
        if current_index > 0:
            await show_event(message.chat.id, current_index - 1)

# Обработка нажатия кнопки "Главное меню"
@dp.message_handler(lambda message: message.text == "Главное меню", state=EventSliderStates.event_index)
async def back_to_main_menu(message: types.Message, state: FSMContext):
    await state.finish()  # Завершаем текущее состояние
    await main_menu(message.chat.id)

# Обработка выбора "Общая информация"
@dp.message_handler(lambda message: message.text == "Общая информация")
async def general_info(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Назад", "Преподаватели")
    await message.answer("Здесь общая информация.", reply_markup=keyboard)

# Обработка выбора "Назад"
@dp.message_handler(lambda message: message.text == "Назад")
async def back_to_main(message: types.Message):
    await main_menu(message.chat.id)

# Обработка выбора "Преподаватели"
@dp.message_handler(lambda message: message.text == "Преподаватели")
async def teachers_info(message: types.Message):
    await message.answer("Карточка 1: Преподаватель 1\nФото: https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg")
    await message.answer("Карточка 2: Преподаватель 2\nФото: https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg")
    await message.answer("Карточка 3: Преподаватель 3\nФото: https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg")
    await message.answer("Карточка 4: Преподаватель 4\nФото: https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg")
    await message.answer("Нажмите 'Назад' для возврата в меню.")

# Обработка выбора "Расписание занятий"
@dp.message_handler(lambda message: message.text == "Расписание занятий")
async def schedule_info(message: types.Message):
    await message.answer_photo(photo='https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg', caption='Расписание занятий.')

# Обработка выбора "Контакты"
@dp.message_handler(lambda message: message.text == "Контакты")
async def contacts_info(message: types.Message):
    await message.answer_photo(photo='https://i.pinimg.com/736x/c8/cc/24/c8cc24bba37a25c009647b8875aae0e3.jpg', caption='Контактная информация.')

# Обработка выбора "Программы обучения"
@dp.message_handler(lambda message: message.text == "Программы обучения")
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

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)