#!/usr/bin/env python3

from distutils.core import setup, Command
from os import system
from sys import exit
from unittest import TestLoader, TextTestRunner


class Style(Command):
	user_options = []

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		try:
			if system('find ./ -name "*.py" | xargs pep8 --ignore=W191'):
				print("Style check failed")
				exit(-1)
		except Exception as e:
			print(e)
			exit(-1)


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
				exit(-1)
		except Exception as e:
			print(e)
			exit(-1)


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
