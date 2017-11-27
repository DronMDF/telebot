
class AcTelegramUpdate:
	def __init__(self, update):
		self.update = update

	def json(self):
		return {
			'chat_id': self.update.message.chat.id,
			'text': self.update.message.text,
			'update_id': self.update.update_id
		}


class ReactionEcho:
	def react(self, update):
		return AcTelegramUpdate(update)


# @todo #68 Нужно сделать такую реакцию,
#  которая могла бы выбирать из нескольких реакций.
#  То есть необходимо реализовать ReactionChoiced
