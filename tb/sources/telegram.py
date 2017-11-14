import telegram


# @todo #39 Перенести AcMessage в правильное место
class AcTelegramUpdate:
	def __init__(self, update):
		self.update = update

	def json(self):
		return {
			'chat_id': self.update.message.chat.id,
			'text': self.update.message.text,
			'update_id': self.update.update_id
		}


class TelegramOffsetFromDb:
	def __init__(self, db):
		self.db = db

	def value(self):
		# @todo #39 Нужно восстановить из БД значние счетчика
		#  и использовать его для последующих операций.
		return 0


# @todo #39 Этот класс должен форммировать ответную реакцию на основе заданного
#  набора реакций. И Набор реакций лучше передавать извне,
#  чтобы не раздувать код.
class SoTelegram:
	def __init__(self, config):
		self.config = config
		self.offset = 0

	def actions(self):
		bot = telegram.Bot(self.config.value("telegram.token"))
		update = bot.getUpdates(offset=self.offset)
		self.offset = max((u.update_id for u in update), default=0) + 1
		return [AcTelegramUpdate(u) for u in update]
