#!/usr/bin/env python

from distutils.core import setup

setup(
	name='Telebot',
	version='1.0',
	description='Security Telegram bot for small servers',
	author='Andrey Valyaev',
	author_email='dron.valyaev@gmail.com',
	url='https://github.com/DronMDF/telebot',
	packages=['tb', 'tb.sources', 'tb.storage'],
	data_files=[('/usr/bin/telebot', ['telebot'])]
)
