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


class AcTelegramText:
	def __init__(self, update, text):
		self.update = update
		self.text = text

	def save(self, db):
		db.set('update_id', self.update.update_id)

	def send(self, transport):
		transport.sendMessage(
			chat_id=self.update.message.chat.id,
			text=self.text
		)


class ReactionConcrete:
	def __init__(self, pattern, answer):
		self.pattern = pattern
		self.answer = answer

	def check(self, update):
		return update.message.text == self.pattern

	def react(self, update):
		return AcTelegramText(update, self.answer)


class ReactionRestrict:
	def __init__(self, name, reaction):
		self.name = name
		self.reaction = reaction

	def check(self, update):
		if update.effective_user.username != self.name:
			return False
		return self.reaction.check(update)

	def react(self, update):
		assert update.effective_user.username == self.name
		return self.reaction.react(update)


class ReactionChoiced:
	def __init__(self, *reactions):
		self.reactions = reactions

	def check(self, update):
		return any((r.check(update) for r in self.reactions))

	def react(self, update):
		for r in self.reactions:
			if r.check(update):
				return r.react(update)


class ReactionAlways:
	def __init__(self, text):
		self.text = text

	def check(self, update):
		return True

	def react(self, update):
		return AcTelegramText(update, self.text)


class ReactionStatus:
	def __init__(self, status_text):
		self.status_text = status_text

	def check(self, update):
		return update.message.text == '/status'

	def react(self, update):
		return AcTelegramText(update, self.status_text.asString())
