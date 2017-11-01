from argparse import ArgumentParser
from unittest import TestCase


class ConfigDefault:
	def __init__(self, values):
		self.values = values

	def value(self, name):
		if name not in self.values:
			raise RuntimeError("No param '%s' in configuration" % name)
		return self.values[name]


class ConfigFromFile:
	# @todo #39 Необходимо организовать чтение конфигурации
	#  из файла конфигурации. Формат файла конфигурации - ini
	#  модуль: https://docs.python.org/3/library/configparser.html
	def __init__(self, filename, defaults):
		self.filename = filename
		self.defaults = defaults

	def value(self, name):
		raise RuntimeError("Wrong configuration value name")


class ConfigFromArgs:
	def __init__(self, args, defaults):
		self.args = args
		self.defaults = defaults

	def value(self, name):
		parser = ArgumentParser()
		parser.add_argument('--token', '-t')
		parser.add_argument('--config', '-c')
		result = vars(parser.parse_args(self.args[1:]))
		params = {
			'config': 'config',
			'telegram.token': 'token'
		}
		if name in params and params[name] in result:
			value = result[params[name]]
		else:
			value = self.defaults.value(name)
		return value


class ConfigFromArgsTest(TestCase):
	def testTelegramTokenInCommandLine(self):
		config = ConfigFromArgs(['prog', '-t', 'token'], ConfigDefault({}))
		self.assertEqual(config.value('telegram.token'), 'token')

	def testConfigFileInCommandLine(self):
		config = ConfigFromArgs(['p', '-c', '/etc/tb.conf'], ConfigDefault({}))
		self.assertEqual(config.value('config'), '/etc/tb.conf')


class Config:
	def __init__(self, args):
		self.args = args

	def value(self, name):
		if name == 'telegram.token':
			return self.args[1]
		raise RuntimeError("Wrong configuration value name")
