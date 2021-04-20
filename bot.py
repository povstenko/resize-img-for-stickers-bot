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
    bot.send_message(message.chat.id, "Send me image without compression, please.")
    
@bot.message_handler(content_types=['document'])
def file(message):
    file_name = message.document.file_name
    file_id = message.document.file_name
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    filename = "img/"+ file_name
    
    nparr = np.frombuffer(downloaded_file, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
    
    (h, w) = image.shape[:2]
    
    # TODO
    
    img_str = cv2.imencode('.png', image)[1].tobytes()
    
    cv2.imwrite(filename, image)
    
    res = open(filename, 'rb')
    bot.send_document(message.chat.id, res)
    
bot.polling()