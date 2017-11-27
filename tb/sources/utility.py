class SoJoin:
	def __init__(self, *sources):
		self.sources = sources

	def actions(self):
		# @todo #47 Необходимо собрать actions со всех внутренних
		#  источников и вернуть в виде общего списка
		return []


class SoSafe:
	def __init__(self, source):
		self.source = source

	def actions(self):
		try:
			return self.source.actions()
		except Exception:
			if self.source.actions.find("warning") != -1:
				begin = self.source.actions.find("warning") #позиция начала текста
			# @todo #58 Из текста исключения необходимо
			#  сформировать сообщение для администратора
			return []
