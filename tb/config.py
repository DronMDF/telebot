class ConfigFromFile:
	# @todo #39 Необходимо организовать чтение конфигурации
	#  из файла конфигурации. Формат файла конфигурации - ini
	#  модуль: https://docs.python.org/3/library/configparser.html
	def __init__(self, filename):
		self.filename = filename

	def has(self, name):
		return False

	def value(self, name):
		raise RuntimeError("Wrong configuration value name")


class ConfigFromArgs:
	# @todo #39 Необходимо организовать разбор параметров из
	#  командной строки. Для начала достаточно поддержать совместимость
	#  С имеющимся классом и достать оттуда токен телеграмма
	#  (первый аргумент) но делать это нужно через модуль:
	#  https://docs.python.org/3/library/argparse.html
	def __init__(self, args):
		self.args = args

	def has(self, name):
		return False

	def value(self, name):
		raise RuntimeError("Wrong configuration value name")


class Config:
	def __init__(self, args):
		self.args = args

	def value(self, name):
		if name == 'telegram.token':
			return self.args[1]
		raise RuntimeError("Wrong configuration value name")
