from tinydb import TinyDB, Query

class TinyDateBase:
    def __init__(self, filename):
        self.filename = filename

    def set(self, name, value):
        db = TinyDB(self.filename)
        # @todo #39 нужно использовать update
        db.insert({'name':name, 'value': value})

    def get(self, name):
        db = TunyDB(self.filename)
        Value = Query()
        return db.search(Value.name == name)[-1]['value'] #должна вернуть последнее значение value
