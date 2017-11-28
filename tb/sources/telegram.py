import telegram
import unittest
from .reaction import ReactionEcho


class TelegramOffsetFromDb:
	def __init__(self, db):
		self.db = db

	def value(self):
		return self.db.get('update_id', 0) + 1


class TelegramBot:
	def __init__(self, config, offset):
		self.config = config
		self.offset = offset

	def getUpdates(self):
		bot = telegram.Bot(self.config.value("telegram.token"))
		update = bot.getUpdates(offset=self.offset.value())
		return update


class SoTelegram:
	def __init__(self, bot, reaction):
		self.bot = bot
		self.reaction = reaction

	def actions(self):
		update = self.bot.getUpdates()
		return [self.reaction.react(u) for u in update]


class FakeMessage(telegram.Message):
	def __init__(self, text):
		super().__init__(
			chat=telegram.Chat(id=1, type='private'),
			message_id=1,
			from_user=telegram.User(
				id=1,
				first_name='Test',
				is_bot=False
			),
			date=1,
			text=text,
		)


class FakeBot:
	def __init__(self, text):
		self.text = text

	def getUpdates(self):
		return [telegram.Update(7, FakeMessage(self.text))]


class FakeTransport:
	def sendMessage(self, chat_id, text):
		self.chat_id = chat_id
		self.text = text


class SoTelegramTest(unittest.TestCase):
	def test(self):
		so = SoTelegram(FakeBot("hello"), ReactionEcho())
		transport = FakeTransport()
		so.actions()[0].send(transport)
		self.assertEqual(transport.text, "hello")
