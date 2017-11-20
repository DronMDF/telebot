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
		self.db.set('update_id', message.json('update_id'))
