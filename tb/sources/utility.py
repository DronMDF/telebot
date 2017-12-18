import itertools
import traceback


class SoJoin:
	def __init__(self, *sources):
		self.sources = sources

	def actions(self):
		return list(itertools.chain.from_iterable(s.actions() for s in self.sources))


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
		except Exception:
			traceback.print_exc()
			# @todo #58 Из текста исключения необходимо
			#  сформировать сообщение для администратора
			return []
