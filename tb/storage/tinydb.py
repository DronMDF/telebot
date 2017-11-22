from tinydb import TinyDB, Query


class TinyDataBase:
	def __init__(self, filename):
		self.filename = filename

	def set(self, name, value):
		db = TinyDB(self.filename)
		# @todo #39 нужно использовать update
		db.insert({'name': name, 'value': value})

	def get(self, name):
		db = TunyDB(self.filename)
		Value = Query()
		# должна вернуть последнее значение value
		return db.search(Value.name == name)[-1]['value']
