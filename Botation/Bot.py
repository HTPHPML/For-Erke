from telegram import *
from telegram.ext import *
import testing
import UkrApi

class CarBot:
    def __init__(self):
        # ТОКЕН ВОТ ТУТ ГЕРА
        self.token = "5795536583:AAGinMCu-OZKscjiFlBmJGl4yuIx0sN-pcE"
        self.updater = Updater(self.token, use_context=True)
        self.dp = self.updater.dispatcher
        self.dic = {"История регистраций": 0,
       "История ДТП": 1,
       "Розыск ТС": 2,
       "Реестр залогов": 6,
       "Последний пробег по ТО": 7,
       "Поиск судебных решений": 9
       }
        self.service = None
        self.first = True

    def start_command(self, update: Update, context: CallbackContext):
        # buttons = [[KeyboardButton("История регистраций")], [KeyboardButton("История ДТП"), KeyboardButton("Розыск ТС")],
        #        [KeyboardButton("Реестр залогов")], [KeyboardButton("Последний пробег по ТО")],
        #        [KeyboardButton("Поиск судебных решений")]]
        context.bot.send_message(chat_id=update.effective_chat.id, text="Введите ВИН")

    def handle_message(self, update: Update, context: CallbackContext):
        print(update.effective_chat.id)
        data = UkrApi.main(update.message.text)
        #im = data.pop(0).split()[0]
        #context.bot.send_photo(chat_id=update.effective_chat.id, photo=im)
        for entry in data:
            context.bot.send_message(chat_id=update.effective_chat.id, text=entry)
        # if update.message.text in self.dic.keys():
        #     self.service = self.dic[update.message.text]
        #     context.bot.send_message(chat_id=update.effective_chat.id, text="Напишите VIN код")
        #
        # else:
        #     context.bot.send_message(chat_id=update.effective_chat.id, text="Бот получает информацию, пожалуйста подождите")
        #     data = testing.findService(update.message.text, self.service)
        #     context.bot.send_message(chat_id=update.effective_chat.id, text=data)

    def main(self):
        self.dp.add_handler(CommandHandler("start", self.start_command))
        self.dp.add_handler(MessageHandler(Filters.text, self.handle_message))
        self.updater.start_polling()
        self.updater.idle()


if __name__ == '__main__':
    bot = CarBot()
    bot.main()
