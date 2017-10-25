import telegram


class StTelegram:
	def __init__(self, config):
		self.config = config

	def save(self, action):
		bot = telegram.Bot(self.config.value('telegram.token'))
		bot.sendMessage(**action.json())
