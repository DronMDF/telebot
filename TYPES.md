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

#Тип объекта - действие

```python
class Action:
	def json(self):
		return {}
```
