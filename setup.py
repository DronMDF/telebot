#!/usr/bin/env python3

from distutils.core import setup, Command
from unittest import TestLoader, TextTestRunner
import glob
import pycodestyle
import sys


class Style(Command):
	user_options = []

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def files(self):
		return glob.iglob('**/*.py', recursive=True)

	def run(self):
		try:
			total_errors = 0
			for f in self.files():
				pep8_errors = pycodestyle.Checker(f, ignore=['W191']).check_all()
				if pep8_errors != 0:
					total_errors = total_errors + 1
			if total_errors != 0:
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
