from telegram.ext import Updater, CommandHandler

# Обработчик команды /groups
def groups(update, context):
    user_id = context.args[0]  # Получение ID пользователя из аргументов команды

    # Получение списка чатов, в которых пользователь состоит
    user_chats = context.bot.get_chat_member(user_id, user_id).user

    # Проверка, является ли пользователь участником группы или супергруппы
    if user_chats:
        chat_info = []
        for chat in user_chats:
            chat_info.append(f"ID чата: {chat.id}, Тип чата: {chat.type}, Название чата: {chat.title}")
        chat_info_text = "\n".join(chat_info)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Пользователь с ID {user_id} состоит в следующих группах и чатах:\n\n{chat_info_text}")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Пользователь с ID {user_id} не состоит в группах или чатах.")

# Создание экземпляра бота с токеном вашего бота
updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

# Получение диспетчера для регистрации обработчиков
dispatcher = updater.dispatcher

# Регистрация обработчика команды /groups
dispatcher.add_handler(CommandHandler('groups', groups))

# Запуск бота
updater.start_polling()
