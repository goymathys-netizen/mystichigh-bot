import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN manquant. Ajoute ton token dans les variables d’environnement.")

CONTACT_PROFILE = "https://t.me/hmzz63_7"
CANAL_LINK = "https://t.me/mistichigh63"
INSTA_LINK = "https://instagram.com/TON_COMPTE"
SIGNAL_LINK = "https://signal.me/#p/+33743262776"
MINI_APP_URL = "https://benevolent-boba-5c725d.netlify.app"

WELCOME_TEXT = (
    "Bienvenue sur Mystic High 63\n\n"
    "Appuie sur « Ouvrir l’application » pour accéder à la mini-app.\n"
    "Le menu est mis à jour régulièrement."
)

INFO_TEXT = (
    "🧾 Informations\n\n"
    "Règles :\n"
    "• Livraison mondial relais : 10€\n"
    "• Livraison selon le montant de la commande\n"
    "• Meet-up prévu le matin\n"
)

def keyboard() -> InlineKeyboardMarkup:
   
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📱 Ouvrir l'application",
                    web_app=WebAppInfo(url=MINI_APP_URL),
                )
            ],
            [
                InlineKeyboardButton("Contact 📲", url=CONTACT_PROFILE),
                InlineKeyboardButton("Canal", url=CANAL_LINK),
            ],
            [
                InlineKeyboardButton("ℹ️ Informations", callback_data="info"),
                InlineKeyboardButton("Instagram", url=INSTA_LINK),
            ],
            [
                InlineKeyboardButton("Signal", url=SIGNAL_LINK),
            ],
        ]
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME_TEXT,
        reply_markup=keyboard(),
        disable_web_page_preview=True,
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        await query.message.reply_text(
            INFO_TEXT,
            disable_web_page_preview=True,
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot en ligne...")
    app.run_polling()

if __name__ == "__main__":
    main()

