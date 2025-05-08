from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

YOUR_USER_ID = 123456789  # آیدی عددی تلگرام خودت
BOT_TOKEN = 'توکن رباتت رو اینجا بذار'

async def anonymous_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == 'private' and update.message.text:
        await context.bot.send_message(
            chat_id=YOUR_USER_ID,
            text=f"پیام ناشناس:\n{update.message.text}"
        )
        await update.message.reply_text("پیام شما ناشناس ارسال شد ✅")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, anonymous_message))

app.run_polling()
