from time import sleep
from .sources import *
from .storage import *


class Application:
	def __init__(self, config):
		telegram_db = TinyDataBase(config.value('telegram.db'))
		self.source = SoSafe(
			SoJoin(
				SoTelegram(
					TelegramBot(
						config,
						TelegramOffsetFromDb(telegram_db)
					),
					ReactionChoiced(
						ReactionRestrict(
							config.value('telegram.username'),
							ReactionChoiced(
								ReactionAlways("Не совсем понятно, что ты хочешь мне сказать")
							)
						),
						ReactionAlways("Ты кто такой, давай, досвидания")
					)
				),
				SoLowHdd(config.value('telegram.chat_id'))
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
