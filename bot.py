# Токен вашего бота
#7910712224:AAFnV_5qwm6yagEkVCoP3oef4cs1P-a4ObI
import logging #библиотека для выведения логов (200 == успешно 404 == не найденно )
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# У Логина мы обращаемся к basicconfig т.е для выведения логов внутри как атрибуты мы указывает формат который будет 
# asctime == время запроса  - в какое время произошел / name == имя обджекта / level_name == уровень взаимодействие или взаи модействие с чем / 
# message == сообщения об ошибке или о успехе (  )
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


TOKEN = "7910712224:AAFnV_5qwm6yagEkVCoP3oef4cs1P-a4ObI"
ADMIN_ID = 901505541  # id админа (мой айди , можно менять на свой или указать списком)



#async def: Это определение асинхронной функции, что позволяет выполнять операции, не блокируя выполнение других задач.
# Асинхронные функции используют await для ожидания завершения операций.
async def start(update: Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        #Здесь мы создаем список кнопок
        [InlineKeyboardButton("Общая Информация",callback_data='info')],                #объект InlineKeyboardButton.
        [InlineKeyboardButton("Программы Обучения" , callback_data='programs')],        #Каждая кнопка имеет два параметра:
        [InlineKeyboardButton("Рассписание Занятий" , callback_data='schedule')],       #Текст кнопки (например, "LOL KEK CHEBUREK").
        [InlineKeyboardButton ("Контакты",callback_data='contacts')],                   #callback_data: данные, которые будут отправлены боту, когда пользователь нажмет на кнопку.
        [InlineKeyboardButton("Мероприятия/Новости", callback_data='events')],          #данные мы будем получать обрабатывать и знать на какую кнопку нажал пользователь
    ]
    
    
    #InlineKeyboardMarkup: Этот объект используется для создания разметки клавиатуры, которая будет отправлена пользователю. 
    #Он принимает список кнопок, который мы создали ранее.
    reply_markup = InlineKeyboardMarkup(keyboard)\
        
    #  await: Ожидает завершения операции, чтобы не блокировать выполнение других задач.
    #update.message.reply_photo: Метод, который отправляет пользователю фотографию.
    #photo: URL изображения
    #caption: Текст под изображением 
    #reply_markup: Передает созданную клавиатуру, чтобы пользователь мог взаимодействовать с ботом
    await update.message.reply_photo(photo='https://sun9-33.userapi.com/impg/BJ9AYKKFnvbwruq5c2VT-ikraDb0O4s1XG5qvQ/k-m-fQWyA38.jpg?size=1235x966&quality=95&sign=e4db72b83b77d7482e7529c7134f364f&type=album',
                                    caption='Добро Пожаловать в бота IT CUBE', reply_markup=reply_markup)
