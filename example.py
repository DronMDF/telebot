#!/usr/bin/env python3

from telegram import Update, Message, User, Chat
from unittest import TestCase, main

# >>> up = bot.getUpdates()
# >>> print(up[1])
# {'message': {'text': 'Hello', 'group_chat_created': False,
#  'date': 1507839749, 'new_chat_photo': [], 'message_id': 2, 'entities': [],
#  'new_chat_member': None, 'photo': [], 'channel_chat_created': False,
#  'new_chat_members': [], 'supergroup_chat_created': False,
#  'from': {'first_name': 'Andrey', 'id': 2, 'language_code': 'en',
#  'last_name': 'Valyaev', 'is_bot': False}, 'chat': {'first_name': 'Andrey',
#  'id': 1, 'last_name': 'Valyaev', 'type': 'private'},
#  'delete_chat_photo': False}, 'update_id': 3}
# >>> bot.sendMessage(chat_id=1, text='Ehlo', parse_mode='Markdown')


class FakeTelegramBot:
	def __init__(self, message):
		self.message = message

	def getUpdates(self, **kwargs):
		return [Update(message=self.message, update_id=1)]


class AcTelegramReply:
	def __init__(self, chat_id, text):
		self.chat_id = chat_id
		self.text = text

	def __repr__(self):
		return "AcTelegramReply(chat_id='%s', text='%s')" % (
			self.chat_id,
			self.text
		)


class SoTelegram:
	def __init__(self, bot):
		self.bot = bot

	def actions(self):
		updates = self.bot.getUpdates()
		return [AcTelegramReply(updates[0].message.chat.id, 'Hello')]


class FakeMessage(Message):
	def __init__(self, chat_id):
		super().__init__(
			chat=Chat(id=chat_id, type='private'),
			message_id=1,
			from_user=User(
				id=1,
				first_name='Test',
				is_bot=False
			),
			date=1
		)


class Test(TestCase):
	def test(self):
		so = SoTelegram(FakeTelegramBot(FakeMessage(3)))
		ac = so.actions()
		self.assertEqual(repr(ac[0]), repr(AcTelegramReply(3, 'Hello')))


if __name__ == '__main__':
	main()
