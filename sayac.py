import logging
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Loglama ayarları
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# YKS tarih ve saati
YKS_DATE = datetime(2026, 6, 20, 10, 15)  # 20 Haziran 2026 10:15

async def sayac(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """YKS'ye kalan süreyi hesaplayan komut"""
    now = datetime.now()
    time_left = YKS_DATE - now
    
    # Kalan süreyi hesapla
    days = time_left.days
    hours = time_left.seconds // 3600
    minutes = (time_left.seconds % 3600) // 60
    
    # Mesajı oluştur
    message = f"📚 YKS'ye Kalan Süre:\n\n"
    message += f"📅 {days} gün\n"
    message += f"⏰ {hours} saat\n"
    message += f"⌛ {minutes} dakika\n\n"
    message += "Bol şans! 🍀"
    
    await update.message.reply_text(message)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bot başlatıldığında karşılama mesajı gönderen komut"""
    welcome_message = (
        "Merhaba! 👋\n\n"
        "YKS Sayaç botuna hoş geldiniz!\n"
        "Sınava kalan süreyi öğrenmek için /sayac komutunu kullanabilirsiniz.\n"
        "Başarılar! 📚✨"
    )
    await update.message.reply_text(welcome_message)

def main():
    """Bot'u başlatan ana fonksiyon"""
    # Bot token'ınızı buraya yazın
    application = Application.builder().token('7642212104:AAGjoUsQnJd1F4jaEFrYbpH4VDbGIbVI1Uw').build()

    # Komutları ekle
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("sayac", sayac))

    # Bot'u başlat
    application.run_polling()

if __name__ == '__main__':
    main()
