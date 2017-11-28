import telegram


class StTelegram:
	def __init__(self, config):
		self.config = config

	def save(self, action):
		bot = telegram.Bot(self.config.value('telegram.token'))
		action.send(bot)


class StDbTelegramOffset:
	def __init__(self, db):
		self.db = db

	def save(self, action):
		action.save(self.db)
