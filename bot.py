"""SheerID Student Bot — Telegram bot buat claim ChatGPT Plus student."""
import os, sys, logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tools.identity_gen import IdentityGenerator

BOT_TOKEN = os.getenv("SHEERID_BOT_TOKEN", "")
gen = IdentityGenerator()
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

MENU = [[
    InlineKeyboardButton("🎓 Generate Identity", callback_data="gen_id"),
    InlineKeyboardButton("📋 Guide Park.edu", callback_data="guide_park"),
], [
    InlineKeyboardButton("🌐 Guide Maricopa", callback_data="guide_maricopa"),
    InlineKeyboardButton("⚙️ Claim ChatGPT", callback_data="guide_chatgpt"),
]]

TEXT = {
    "guide_park": (
        "📋 *PARK.EDU (15 menit)*\n\n"
        "1. Buka park.edu → Apply\n"
        "2. Isi pake identity dari bot\n"
        "3. SSN: skip (opsional)\n"
        "4. Online student, Undergraduate, Fall\n"
        "5. Submit → 2 email masuk\n"
        "   • Email 1: Student ID (5 menit)\n"
        "   • Email 2: Portal + password (2-6 jam)\n"
        "6. Login my.park.edu → mail.park.edu\n"
        "7. .edu lo: {StudentID}@park.edu\n\n"
        "🔗 https://www.park.edu/apply/"
    ),
    "guide_maricopa": (
        "📋 *MARICOPA (Arizona)*\n\n"
        "1. Buka application.maricopa.edu\n"
        "2. Isi pake identity dari bot\n"
        "3. SSN: *KOSONGIN*\n"
        "4. Pilih college → 'Take a Class'\n"
        "5. Submit → dapet MEID + password\n"
        "6. Tunggu 6-24 jam\n"
        "7. Login google.maricopa.edu\n"
        "8. Setup Duo 2FA (SMS, nomor real)\n"
        "9. Dapet @maricopa.edu\n\n"
        "📌 Tunggu 24 jam sebelum claim SheerID"
    ),
    "guide_chatgpt": (
        "⚙️ *CLAIM CHATGPT PLUS 4 BULAN*\n\n"
        "1. Buka chatgpt.com/students/2026\n"
        "2. Login akun ChatGPT lo (email biasa)\n"
        "3. Klik 'Claim free offer'\n"
        "4. Masukin email .edu\n"
        "5. Kalo auto-verify → langsung sukses\n"
        "6. Kalo minta dokumen: upload admission\n"
        "   letter + screenshot portal student\n"
        "7. Add payment method (gak dicharge)\n"
        "8. Confirm → 4 bulan gratis\n\n"
        "⚠️ Deadline 31 Okt 2026"
    ),
}


async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *SheerID Student Bot*\n\n"
        "Bantu claim ChatGPT Plus 4 bulan gratis.\n\n"
        "1️⃣ Park.edu — 15 menit, .edu langsung\n"
        "2️⃣ Maricopa — alternatif\n\n"
        "👇 Pilih:",
        reply_markup=InlineKeyboardMarkup(MENU),
        parse_mode="Markdown",
    )


async def button(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == "gen_id":
        ident = gen.generate()
        kb = [[InlineKeyboardButton("🔄 Lagi", callback_data="gen_id")]]
        await q.edit_message_text(
            f"✅ *Identity Baru:*\n```{gen.to_text_block(ident)}```",
            reply_markup=InlineKeyboardMarkup(kb),
            parse_mode="Markdown",
        )
    elif q.data in TEXT:
        kb = [[InlineKeyboardButton("⬅️ Menu", callback_data="menu")]]
        await q.edit_message_text(TEXT[q.data], reply_markup=InlineKeyboardMarkup(kb), parse_mode="Markdown")
    elif q.data == "menu":
        await q.edit_message_text("🤖 *Menu:*", reply_markup=InlineKeyboardMarkup(MENU), parse_mode="Markdown")


def main():
    if not BOT_TOKEN:
        raise SystemExit("[!] SHEERID_BOT_TOKEN not set")
    app = Application.builder().token(BOT_TOKEN).connect_timeout(30).read_timeout(30).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    logging.info("[✓] Bot polling...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()