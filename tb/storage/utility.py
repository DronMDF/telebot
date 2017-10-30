class StDispatch:
	def __init__(self, *storages):
		self.storages = storages

	def save(self, action):
		for storage in self.storages:
			storage.save(action)
