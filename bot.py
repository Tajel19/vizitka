import telebot
from telebot import types

# Твой токен от BotFather
TOKEN = '8289266510:AAEnlGyA0YGgMNkNSAi1LoNE_FgR25JIS54'
bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    # Главное меню (кнопки у клавиатуры)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👨‍💻 Обо мне")
    btn2 = types.KeyboardButton("💰 Услуги и Прайс")
    btn3 = types.KeyboardButton("📞 Связаться")
    
    markup.add(btn1, btn2)
    markup.add(btn3)
    
    welcome_text = (
        f"Салем, {message.from_user.first_name}! 👋\n\n"
        "Рад видеть тебя в моем боте-визитке. "
        "Меня зовут **Tajel**, и я занимаюсь разработкой Telegram-ботов и автоматизацией на Python.\n\n"
        "Используй меню ниже, чтобы узнать подробнее 👇"
    )
    
    # Красивая фоновая картинка для ИТ-визитки
    photo = "https://images.unsplash.com/photo-1618401471353-b98afee0b2eb?q=80&w=500"
    
    try:
        bot.send_photo(message.chat.id, photo, caption=welcome_text, reply_markup=markup, parse_mode="Markdown")
    except Exception:
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

# Обработка нажатий на кнопки меню
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "👨‍💻 Обо мне":
        about_text = (
            "👨‍💻 **Обо мне (Tajel):**\n\n"
            "Я Python-разработчик. Создаю быстрых, надежных и удобных Telegram-ботов на библиотеке Telebot.\n\n"
            "🛡️ **Мой стек:**\n"
            "• Язык: Python\n"
            "• Инструменты: Работа с API, базами данных, кнопками и сложной логикой меню.\n\n"
            "Помогаю автоматизировать бизнес и создавать удобные инструменты для общения с клиентами!"
        )
        bot.send_message(message.chat.id, about_text, parse_mode="Markdown")

    elif message.text == "💰 Услуги и Прайс":
        price_text = (
           "💰 **Мои услуги (Скидка для первых клиентов!):**\n\n"
            "🔹 **Бот-визитка / Автоответчик** — от 5 000 ₸\n"
            "_(Простое меню, выдача информации, контакты, прайс-листы)_\n\n"
            "🔹 **Бот с базой данных** — от 15 000 ₸\n"
            "_(Сбор заявок, запись на услуги, админ-панель для рассылок)_\n\n"
            "🔹 **Небольшие доработки / Исправление багов** — от 3 000 ₸\n"
            "_(Добавить кнопку, поменять текст, починить падение бота)_\n\n"
            "⏱️ **Сроки:** очень быстрые (от нескольких часов до 2 дней)!"
        )
        bot.send_message(message.chat.id, price_text, parse_mode="Markdown")

    elif message.text == "📞 Связаться":
        # Создаем инлайн-кнопку для быстрого перехода в ЛС
        inline_markup = types.InlineKeyboardMarkup()
        btn_link = types.InlineKeyboardButton(text="💬 Написать в ЛС", url="https://t.me/Tajel19")
        inline_markup.add(btn_link)

        contact_text = (
            "📞 **Как заказать бота или задать вопрос?**\n\n"
            "Вы можете написать мне напрямую в Telegram:\n"
            "👉 @Tajel19\n\n"
            "Или просто нажмите на кнопку ниже, чтобы открыть чат со мной 👇"
        )
        bot.send_message(message.chat.id, contact_text, reply_markup=inline_markup, parse_mode="Markdown")

# Запуск
if __name__ == '__main__':
    print("Бот-визитка для Tajel успешно запущен!")
    bot.infinity_polling()