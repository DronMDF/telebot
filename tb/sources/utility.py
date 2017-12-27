from datetime import datetime
import itertools
import traceback


class SoJoin:
	def __init__(self, *sources):
		self.sources = sources

	def actions(self):
		return list(itertools.chain.from_iterable(s.actions() for s in self.sources))


class SoJoinTest:
	pass


class SoSafe:
	def __init__(self, source):
		self.source = source

	def actions(self):
		try:
			return self.source.actions()
		except Exception:
			traceback.print_exc()
			return []


class SoNotFlood:
	def __init__(self, source, interval):
		self.source = source
		self.interval = interval
		self.nexttime = datetime.now()

	def actions(self):
		if datetime.now() > self.nexttime:
			actions = self.source.actions()
			if actions:
				self.nexttime = datetime.now() + self.interval
		else:
			actions = []
		return actions
