from tinydb import TinyDB, where


class TinyDataBase:
	def __init__(self, filename):
		self.filename = filename

	def set(self, name, value):
		db = TinyDB(self.filename)
		db.upsert({'name': name, 'value': value}, where('name') == name)

	def get(self, name, default=None):
		db = TinyDB(self.filename)
		try:
			return db.get(where('name') == name)['value']
		except IndexError:
			return default
