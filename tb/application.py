from .sources import SoTelegram
from .storage import StTelegram


class Application:
	def __init__(self, config):
		self.config = config
		self.source = SoTelegram(self.config)
		self.storage = StTelegram(self.config)

	def run(self):
		# @todo #35 Реализовать в Application.run() основной цикл приложения
		#  Этот цикл должен вытягивать события из self.source и отправлять
		#  в self.storage, Интерфейсы описаны в файле types.py, нарушать нельзя.
		pass
