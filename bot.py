from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext


TOKEN = "8031208842:AAGBsKCHg6BVk-VJxVt-b8jSYIwCVkAj6e4" # ТОКЕН БОТА!!! 


def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("О компании", callback_data='about')],
        [InlineKeyboardButton("Контакты", callback_data='contacts')],
        [InlineKeyboardButton("Часы работы", callback_data='hours')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Добро пожаловать в информационный бот нашей компании! Выберите меню:', reply_markup=reply_markup)

# Функция обработки нажатий на кнопки
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    if query.data == 'about':
        query.edit_message_text(text="Описание организации:\nМиссия: ...\nЦели: ...\nИстория: ...\nОсновные направления работы: ...")
    elif query.data == 'contacts':
        query.edit_message_text(text="Контактная информация:\nАдрес: ...\nТелефон: ...\nЭлектронная почта: ...\nСоцсети: ...")
    elif query.data == 'hours':
        query.edit_message_text(text="Часы работы:\nПн-Пт: 09:00 - 18:00\nСб: 10:00 - 16:00\nВс: Выходной")
    elif query.data == 'back':
        start(update, context)

def main():
    updater = Updater(TOKEN)
    
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()