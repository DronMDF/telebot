import psutil

class SoHDD:
	def actions(self):
		if psutil.disk_usage('/').percent > 90:
			# @todo #41 Сформировать Action, который доставит админу
			#  уведомление о том, что на диске кончилось место
			pass
		return []
