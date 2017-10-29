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
		# @todo #39 В процессе выполнения action может возникнуть
		#  исключение. В этом случае необходимо донести
		#  до админитратора информацию о том, что пошло не так.
		return self.source.actions()
