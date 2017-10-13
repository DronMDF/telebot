#!/usr/bin/env python3

from unittest import TestCase, main


class FakeTelegramBot:
	def sendMessage(self, **kwargs):
		self.json = kwargs


class AcTelegramReply:
	def __init__(self, chat_id, text):
		self.chat_id = chat_id
		self.text = text

	def json(self):
		return {
			'chat_id': self.chat_id,
			'text': self.text
		}


class StTelegram:
	def __init__(self, bot):
		self.bot = bot

	def save(self, action):
		self.bot.sendMessage(**action.json())


class Test(TestCase):
	def test(self):
		# Given
		bot = FakeTelegramBot()
		st = StTelegram(bot)
		# When
		st.save(AcTelegramReply(chat_id=6, text='Bye'))
		# Then
		self.assertEqual(bot.json, {'chat_id': 6, 'text': 'Bye'})


if __name__ == '__main__':
	main()
