import psutil


class AcLowHDD:
        def __init__(self, chat_id):
                self.chat_id = chat_id

        def save(self, db):
                pass

        def send(self, transport):
                transport.sendMessage(
                        chat_id=self.chat_id,
                        text="Мало места на жестком диске"
                )


class SoHDD:
        def __init__(self, chat_id):
                self.chat_id = chat_id

        def actions(self):
                if psutil.disk_usage('/').percent > 90:
                        return [AcLowHDD(self.chat_id)]
                return []
