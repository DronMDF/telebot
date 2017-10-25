class Config:
	def __init__(self, args):
		self.args = args

	def value(self, name):
		if name == 'telegram.token':
			return self.args[1]
		raise RuntimeError("Wrong configuration value name")
