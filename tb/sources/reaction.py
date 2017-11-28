class AcTelegramUpdate:
	def __init__(self, update):
		self.update = update

	def save(self, db):
		db.set('update_id', self.update.update_id)

	def send(self, transport):
		transport.sendMessage(
			chat_id=self.update.message.chat.id,
			text=self.update.message.text
		)


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
