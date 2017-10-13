class StTelegram:
	def __init__(self, config):
		self.token = config.value('telegram.token')

	def save(self, action):
		# @todo #35 Нужно обратиться к серверу telegram
		#  и залить туда. Для этого нужно использовать
		#  https://python-telegram-bot.org/ Но пример неправильный,
		#  поскольку нам нужно только отправить сообщения на сервер.
		#  что-то типа этого: telegram.Bot.sendMessage
		pass
