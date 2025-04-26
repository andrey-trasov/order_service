from services import record_id_tg

import logging
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler

BOT_TOKEN = "7631853339:AAGsS9CiWQ0JSlyxdfn-VjQMlKrV5vkillk"

# Определяем этапы разговора
PHONE = 0



# Обработчик команды /start
async def start(update: Update, context) -> int:
    """Отправляет сообщение пользователю с запросом номера телефона."""
    await update.message.reply_text(
        "Напишите ваш номер телефона в формате +7XXXXXXXXXX",
        reply_markup=ReplyKeyboardRemove(),  # Убирает клавиатуру, если есть
    )
    return PHONE


# Обработчик для получения номера телефона
async def get_phone(update: Update, context) -> int:
    """Получает номер телефона от пользователя и запускает функцию record_id_tg."""
    phone_number = update.message.text
    user_id = update.message.from_user.id

    # Проверка формата номера
    if not phone_number.startswith('+7') or len(phone_number) != 12 or not phone_number[1:].isdigit():
        await update.message.reply_text(
            "Неверный формат номера. Пожалуйста, введите номер в формате +7XXXXXXXXXX"
        )
        return PHONE  # Остаемся на этапе ввода номера

    answer = record_id_tg(phone_number, user_id)  # Вызываем вашу функцию

    await update.message.reply_text(
        answer,
        reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END # Заканчиваем разговор


# Обработчик отмены разговора (если пользователь захочет отменить ввод номера)
async def cancel(update: Update, context) -> int:
    """Отменяет и заканчивает разговор."""
    await update.message.reply_text(
        "Ввод номера отменен.", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def main() -> None:
    """Запускает бота."""
    # Включаем логирование для отладки
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    # Создаем Application и передаем токен
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Создаем обработчик разговоров
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # Добавляем обработчик разговоров в приложение
    application.add_handler(conv_handler)

    # Запускаем бота до прерывания сигналами Ctrl-C
    application.run_polling()


if __name__ == '__main__':
    main()
