class SoTelegram:
	def __init__(self, config):
		self.token = config.value('telegram.token')
               

	def actions(self):
                self.config = config
                bot = telegram.Bot(config.value("telegram.token"))
                update = bot.getUpdate()
                return[AcMessage(u) for u in update]
