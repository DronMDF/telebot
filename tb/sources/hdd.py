import psutil


class SoHDD:
def free_space(DISK):
		# @todo #40 Необходимо определить размер свободного места
		#  на диске. Если размер свободного места меньше чем 10%
		#  от диска - сгенерировать событие.
		free = psutil.disk_usage(DISK).free
		total = psutil.disk_usage(DISK).total
		if free/(total/100)>=10
			return free
		else
			raise Exception('less then 10% is free')
