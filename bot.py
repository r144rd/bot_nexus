from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
# Токен вашего бота
TOKEN = "8031208842:AAGBsKCHg6BVk-VJxVt-b8jSYIwCVkAj6e4"

def start(update: Update, context: CallbackContext) -> None:
        keyboard = [
            [InlineKeyboardButton("О компании", callback_data='about')],
            [InlineKeyboardButton("Контакты", callback_data='contacts')],
            [InlineKeyboardButton("Часы работы", callback_data='work_hours')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Добро пожаловать! Выберите опцию:', reply_markup=reply_markup)

    
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'about':
        query.edit_message_text(text="""Описание организации:\n
                        Наша миссия - предоставлять качественные услуги и решать проблемы клиентов.\n
                        Цели: развитие, инновации, клиентский сервис.\n
                        История: основаны в 2000 году.\n
                        Основные направления: консультации, разработка, поддержка.""")

    elif query.data == 'contacts':
        query.edit_message_text(text="""Контактная информация:\n
                        Адрес: ул. Примерная, 1\n
                        Телефон: 8-800-XXXX-XXXX\n
                        Электронная почта: info@company.com\n
                        Социальные сети: @example в Instagram и Facebook.""")

    elif query.data == 'work_hours':
        query.edit_message_text(text="""Часы работы:\n
        Пн-Пт: 9:00 - 18:00\n
        Сб: 10:00 - 14:00\n
        Вс: выходной.""")
        
    elif query.data == 'back':
        start(update, context)

def main():
    updater = Updater("8187841294:AAEdPWsLupm_LcDE83iiNf71V3o7NZqXp6w")
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

    if __name__ == '__main__':
        main()