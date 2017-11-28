from tinydb import TinyDB, where


class TinyDataBase:
	def __init__(self, filename):
		self.filename = filename

	def set(self, name, value):
		db = TinyDB(self.filename)
		db.upsert({'name': name, 'value': value}, where('name') == name)

	def get(self, name, default=None):
		db = TinyDB(self.filename)
		item = db.get(where('name') == name)
		if item is not None:
			return item.get('value', default)
		return default
