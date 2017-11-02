from argparse import ArgumentParser
from configparser import ConfigParser, NoOptionError, NoSectionError
from unittest import TestCase


class ConfigDefault:
	def __init__(self, values):
		self.values = values

	def value(self, name):
		if name not in self.values:
			raise RuntimeError("No param '%s' in configuration" % name)
		return self.values[name]


class ConfigFile:
	''' Файл с конфигурацией '''
	def __init__(self, config):
		self.config = config

	def readall(self):
		return open(self.config.value('config'), 'r').readall()


class ConfigString:
	''' Строка с файловой конфигурацией '''
	def __init__(self, content):
		self.content = content

	def readall(self):
		return self.content


class ConfigFromFile:
	def __init__(self, configfile, defaults):
		self.configfile = configfile
		self.defaults = defaults

	def value(self, name):
		config = ConfigParser()
		config.read_string(self.configfile.readall())
		try:
			result = config.get(*name.split('.'))
		except (NoSectionError, NoOptionError):
			result = self.defaults.value(name)
		return result


class ConfigFromFileTest(TestCase):
	def testTelegramTokenInFile(self):
		config = ConfigFromFile(
			ConfigString('[telegram]\ntoken=token'),
			ConfigDefault({})
		)
		self.assertEqual(config.value('telegram.token'), 'token')

	def testConfigFileDefaults(self):
		config = ConfigFromFile(
			ConfigString(''),
			ConfigDefault({'section.key': 'value'})
		)
		self.assertEqual(config.value('section.key'), 'value')

	def testConfigFileDefaultsIfSectionPresent(self):
		config = ConfigFromFile(
			ConfigString('[section]'),
			ConfigDefault({'section.key': 'value'})
		)
		self.assertEqual(config.value('section.key'), 'value')


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
