import itertools


class SoJoin:
	def __init__(self, *sources):
		self.sources = sources

	def actions(self):
		return list[itertools.chain(s.actions() for s in self.sources)]


class SoJoinTest:
	# @todo #48 Что-то я немного сомневаюсь, что SoJoin работает корректно.
	#  И это удобное место, чтобы попробовать написать тест.
	#  Примеры оформления тестов можно посмотреть в других файлах.
	pass


class SoSafe:
	def __init__(self, source):
		self.source = source

	def actions(self):
		try:
			return self.source.actions()
		except Exception as e:
			# @todo #58 Из текста исключения необходимо
			#  сформировать сообщение для администратора
			print(e)
			return []
