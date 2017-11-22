from time import sleep
from .sources import SoTelegram, SoSafe, TelegramBot, ReactionEcho
from .storage import StTelegram, StDispatch, StDbTelegramOffset, TinyDataBase


class Application:
	def __init__(self, config):
		self.config = config
		self.source = SoSafe(
			SoTelegram(
				TelegramBot(self.config),
				ReactionEcho()
			)
		)
		self.storage = StDispatch(
			StTelegram(self.config),
			StDbTelegramOffset(
				TinyDataBase('telegram.json')
			)
		)

	def run(self):
		while True:
			acts = self.source.actions()
			for a in acts:
				self.storage.save(a)
			sleep(5)
