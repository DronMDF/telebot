#Тип объекта - источника

```python
class Source:
	def events(self):
		return []
```

#Тип объекта - хранилища

```python
class Storage:
	def save(self, event):
		pass
```

#Тип объекта - события

```python
class Event:
	def text(self):
		return ''

	def json(self):
		return {}
```
