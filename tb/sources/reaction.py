class AcTelegramUpdate:
	# @todo #74 Это мешок с данными. Но этот класс может быть более
	#  ответственным за свои данные. В зависимости от того, какой сторедж -
	#  у экшина будет вызываться метод send, или метод save. В который
	#  будет передаваться интрефейс транспорта, или интерфейс БД
	#  соответственно.
	def __init__(self, update):
		self.update = update

	def json(self):
		return {
			'chat_id': self.update.message.chat.id,
			'text': self.update.message.text,
			'update_id': self.update.update_id
		}


class ReactionEcho:
	def check(self, update):
		return True

	def react(self, update):
		return AcTelegramUpdate(update)


class ReactionChoiced:
	def __init__(self, *reactions):
		self.reactions = reactions

	def check(self, update):
		return True

	def react(self, update):
		for r in self.reactions:
			if r.check(update):
				return r.react(update)
