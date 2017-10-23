from time import sleep
from .sources import SoTelegram
from .storage import StTelegram


class Application:
	def __init__(self, config):
		self.config = config
		self.source = SoTelegram(self.config)
		self.storage = StTelegram(self.config)

	def run(self):
		while True:
			acts = self.source.actions()
			for a in acts:
				self.storage.save(a)
			sleep(5)
