import psutil


class AcLowHDD:
	def __init__(self, chat_id):
		self.chat_id = chat_id

	def save(self, db):
		pass

	def send(self, transport):
		transport.sendMessage(
			chat_id=self.chat_id,
			text="Мало места на жестком диске"
		)


class SoLowHdd:
	def __init__(self, chat_id, level=90):
		self.chat_id = chat_id
		self.level = level

	def actions(self):
		if psutil.disk_usage('/').percent > self.level:
			return [AcLowHDD(self.chat_id)]
		return []


class StatusHdd:
	def asString(self):
		return 'Диск занят на %u%%' % psutil.disk_usage('/').percent
