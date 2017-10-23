import telegram


class SoTelegram:
	def __init__(self, config):
		self.config = config

	def actions(self):
		bot = telegram.Bot(config.value("telegram.token"))
		update = bot.getUpdate()
		return [AcMessage(u) for u in update]
