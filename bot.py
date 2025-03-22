# Токен вашего бота
#7910712224:AAFnV_5qwm6yagEkVCoP3oef4cs1P-a4ObI
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import filters
from aiogram.utils import executor

# Установите уровень логирования
logging.basicConfig(level=logging.INFO)

# Создайте экземпляр бота и диспетчера
API_TOKEN = 'YOUR_API_TOKEN'  # Замените на ваш токен
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# ID администратора
ADMIN_ID = 123456789  # Замените на ваш ID

# Стартовое состояние
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Отправляем приветственное сообщение и картинку
    await message.answer_photo(photo='https://example.com/image.jpg', caption='Добро пожаловать в нашего бота!')
    await main_menu(message.chat.id)

# Главное меню
async def main_menu(chat_id):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Общая информация", "Программы обучения", "Расписание занятий", "Контакты", "Мероприятия/Новости"]
    keyboard.add(*buttons)
    await bot.send_message(chat_id, "Выберите опцию:", reply_markup=keyboard)

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
    # Здесь можно добавить карточки с информацией о преподавателях
    await message.answer("Карточка 1: Преподаватель 1\nФото: https://example.com/teacher1.jpg")
    await message.answer("Карточка 2: Преподаватель 2\nФото: https://example.com/teacher2.jpg")
    await message.answer("Карточка 3: Преподаватель 3\nФото: https://example.com/teacher3.jpg")
    await message.answer("Карточка 4: Преподаватель 4\nФото: https://example.com/teacher4.jpg")
    await message.answer("Нажмите 'Назад' для возврата в меню.")

# Обработка выбора "Расписание занятий"
@dp.message_handler(lambda message: message.text == "Расписание занятий")
async def schedule_info(message: types.Message):
    await message.answer_photo(photo='https://example.com/schedule.jpg', caption='Расписание занятий.')

# Обработка выбора "Контакты"
@dp.message_handler(lambda message: message.text == "Контакты")
async def contacts_info(message: types.Message):
    await message.answer_photo(photo='https://example.com/contact.jpg', caption='Контактная информация.')

# Обработка выбора "Мероприятия/Новости"
@dp.message_handler(lambda message: message.text == "Мероприятия/Новости")
async def events_info(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Назад", "Вперед")
    await message.answer("Слайдер мероприятий:\n1. Мероприятие 1\n2. Мероприятие 2\n3. Мероприятие 3", reply_markup=keyboard)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)