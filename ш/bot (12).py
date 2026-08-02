import asyncio
import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Настройки ---
BOT_TOKEN = "7786772822:AAGO8i5-eNW0Q3sLZlHy8TTWdA6HvNAbQDU"  # вставьте сюда токен вашего бота

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет пользователю сообщения после команды /start: текст, фото, текст."""
    chat_id = update.effective_chat.id

    # Первое сообщение — текст
    await context.bot.send_message(chat_id=chat_id, text="Привет, я ксюша, стану твоей личной шлюшкой за деньги. Ну смотря сколько заплатишь))")
    await asyncio.sleep(1)  # небольшая пауза между сообщениями (необязательно)

    # Второе сообщение — фото (из локального файла, должен лежать рядом со скриптом)
    with open("photo.jpg", "rb") as photo_file:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=photo_file,
            caption="Вот прайслист)))",
        )
    await asyncio.sleep(1)

    # Третье сообщение — текст
    await context.bot.send_message(chat_id=chat_id, text="вот мой юз зайка, пиши нсли интересно)) 

@Xnow_mtw")


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    application.run_polling()


if __name__ == "__main__":
    main()
