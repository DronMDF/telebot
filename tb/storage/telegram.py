import telegram


class StTelegram:
	def __init__(self, config):
		self.config = config

	def save(self, action):
		bot = telegram.Bot(self.config.value('telegram.token'))
		bot.sendMessage(**action.json())


class StDbTelegramOffset:
	def __init__(self, db):
		self.db = db

	def save(self, action):
		# @todo #39 Необходимо сохранить в БД номер сообщения,
		#  с которым работал бот. Это необходимо для того, чтобы после
		#  перезапуска бот не повторял свои сообщения. Можно использовать
		#  https://pypi.python.org/pypi/tinydb - достаточно простая штука.
		pass
