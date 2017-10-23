from time import sleep
from .sources import SoTelegram
from .storage import StTelegram


class Application:
	def __init__(self, config):
		self.config = config
		self.source = SoTelegram(self.config)
		self.storage = StTelegram(self.config)

	def run(self):
		# 38
		while True:
			acts = self.source.events() #events()->actions()
			for a in acts:
				self.storage.save(a)
				sleep(5)
		pass
