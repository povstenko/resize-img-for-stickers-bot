import telebot
import numpy as np
import cv2

TOKEN = "TOKEN"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello, send me image and I`ll resize it to fit requirements of Telegram Stickers:\n\n \
     image fits into a 512x512 square (one of the sides should be 512px and the other 512px or less).")

@bot.message_handler(func=lambda message: True)
def ask_photo(message):
	bot.send_message(message.chat.id, "Send me your image, please.")

@bot.message_handler(content_types=['photo'])
def photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("img/image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    
    # bot.send_photo(message.chat.id, res)

bot.polling()