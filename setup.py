#!/usr/bin/env python3

import glob
import sys
from distutils.core import setup, Command
from unittest import TestLoader, TextTestRunner

import pycodestyle


class Style(Command):
	user_options = []

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def files(self):
		return glob.iglob('**/*.py', recursive=True)

	def pep8(self, f):
		return pycodestyle.Checker(f, ignore=['W191']).check_all() == 0

	def check(self, f):
		return all((
			self.pep8(f),
		))

	def run(self):
		try:
			if not all((self.check(f) for f in self.files())):
				print("Style check failed")
				sys.exit(-1)
		except Exception as e:
			print(e)
			sys.exit(-1)


class Test(Command):
	user_options = []

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		try:
			suite = TestLoader().discover('.', '*.py')
			runner = TextTestRunner()
			results = runner.run(suite)
			if not results.wasSuccessful():
				print("Test failed")
				sys.exit(-1)
		except Exception as e:
			print(e)
			sys.exit(-1)


if __name__ == '__main__':
	setup(
		name='Telebot',
		version='1.0',
		description='Security Telegram bot for small servers',
		author='Andrey Valyaev',
		author_email='dron.valyaev@gmail.com',
		url='https://github.com/DronMDF/telebot',
		packages=['tb', 'tb.sources', 'tb.storage'],
		data_files=[('/usr/bin/telebot', ['telebot'])],
		cmdclass={'style': Style, 'test': Test}
	)
