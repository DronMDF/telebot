
import time
from datetime import datetime

n = datetime.now() #инициализировать в начале программы

time.sleep(100) #тест

print(datetime.now()-n) #вызывать по надобности
