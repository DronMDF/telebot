import telegram


# @todo #39 Перенести AcMessage в правильное место
class AcTelegramUpdate:
	def __init__(self, update):
		self.update = update

	def json(self):
		return {
			'chat_id': self.update.message.chat.id,
			'text': self.update.message.text,
		}


class SoTelegram:
	def __init__(self, config):
		self.config = config

	def actions(self):
		bot = telegram.Bot(self.config.value("telegram.token"))
		# @todo #39 getUpdates нужно вызывать с номером очередного сообщения.
		#  А пока он повторяет все сообщения, которые к нему поступили.
		update = bot.getUpdates()
		return [AcTelegramUpdate(u) for u in update]
