class SoSyslog:
	def actions(self):
                sys_history = " "
		with open('./messages.txt') as syslogFile:
                        for line in syslogFile:
                            sys_history += str(line)
                return sys_history
		
