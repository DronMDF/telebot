from time import sleep
from .sources import (
	ReactionChoiced,
	ReactionConcrete,
	ReactionEcho,
	SoSafe,
	SoTelegram,
	TelegramBot,
	TelegramOffsetFromDb
)
from .storage import StTelegram, StDispatch, StDbTelegramOffset, TinyDataBase


class Application:
	def __init__(self, config):
		telegram_db = TinyDataBase('telegram.json')
		self.source = SoSafe(
			SoTelegram(
				TelegramBot(
					config,
					TelegramOffsetFromDb(telegram_db)
				),
				ReactionChoiced(
					ReactionConcrete('Hi', 'Heyya, guest'),
					ReactionEcho()
				)
			)
		)
		self.storage = StDispatch(
			StTelegram(config),
			StDbTelegramOffset(telegram_db)
		)

	def run(self):
		while True:
			acts = self.source.actions()
			for a in acts:
				self.storage.save(a)
			sleep(5)
