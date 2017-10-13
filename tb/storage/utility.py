class StDispatch:
	def __init__(self, *storages):
		self.storages = storages

	def save(self, action):
		# @todo #47 Необходимо пробросить action
		#  во все вложенные storage
		pass
