class SoTelegram:
	def __init__(self, config):
		self.token = config.value('telegram.token')

	def actions(self):
		# @todo #35 Нужно обратиться к серверу telegram
		#  и вытащить оттуда свежие сообщения. Для этого нужно использовать
		#  https://python-telegram-bot.org/ Но пример неправильный,
		#  поскольку нам нужно только забрать сообщения с сервера.
		#  Что-то типа этого: telegram.Bot.getUpdates
		return []
