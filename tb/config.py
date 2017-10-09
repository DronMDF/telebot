class Config:
	def __init__(self, args):
		self.args = args

	def value(self, name):
		# @todo #35 А давайте пока для простоты передадим токен
		#  в параметрах командной строки, пусть будет первым параметром
		#  но запрос нужно делать по ключу. Ключ для токена будет 'telegram.token'
		#  А список аргументов командной строки содержится в self.args
		return None
