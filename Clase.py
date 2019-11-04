from pymongo import MongoClient, ASCENDING
from datetime import datetime 


## La fecha debe ir con el formato especificado, en tipo str().  Ej: "2016-08-23 14:50:15"
def get_date(date):
	return datetime.strptime(date, '%Y-%m-%d %H:%M:%S')


class User:
	def __init__(self, user, db_name, connection):
		self.user = user
		self.db = connection[db_name]
	# TODAS las consultas irán en especifico a un usuario.

	# Tiempo gastado total en un topic especifico.  
	def time(self, evento):
		suma = int()
		for doc in self.db[evento].find({"user" : self.user}):
			suma += doc["time_spent"]
		return suma

	# Tiempo gastado total en un topic especifico y en una fecha especifica.
	# Date solo año, mes, dia. EJ: "2016-08-22"
	def time_date(self, evento, date):
		suma = int()
		date = date.split("-")
		for doc in self.db[evento].find({"user" : self.user }):
			if doc["date"].day == int(date[2]) and doc["date"].month == int(date[1]) and doc["date"].year == int(date[0]):
				suma += doc["time_spent"]
		return suma

	# Tiempo total en MOOC, sin contar navegacion. (tiempo efectivo: Tareas, Videos, Suplementos, Discusiones)
	def time_MOOC(self):
		suma = int()
		for doc in self.db["discusion"].find({"user" : self.user}):
			suma += doc["time_spent"]
		for doc in self.db["tareas"].find({"user" : self.user}):
			suma += doc["time_spent"]
		for doc in self.db["videos"].find({"user" : self.user}):
			suma += doc["time_spent"]		
		for doc in self.db["suplementos"].find({"user" : self.user}):
			suma += doc["time_spent"]
		return suma

	# Tiempo total en MOOC, sin contar navegacion. (tiempo efectivo: Tareas, Videos, Suplementos, Discusiones) y una fecha especifica. 
	def time_MOOC_date(self, date):
		suma = int()
		date = date.split("-")
		for doc in self.db["discusion"].find({"user" : self.user}):
			if doc["date"].day == int(date[2]) and doc["date"].month == int(date[1]) and doc["date"].year == int(date[0]):
				suma += doc["time_spent"]
		for doc in self.db["tareas"].find({"user" : self.user}):
			if doc["date"].day == int(date[2]) and doc["date"].month == int(date[1]) and doc["date"].year == int(date[0]):
				suma += doc["time_spent"]
		for doc in self.db["videos"].find({"user" : self.user}):
			if doc["date"].day == int(date[2]) and doc["date"].month == int(date[1]) and doc["date"].year == int(date[0]):
				suma += doc["time_spent"]	
		for doc in self.db["suplementos"].find({"user" : self.user}):
			if doc["date"].day == int(date[2]) and doc["date"].month == int(date[1]) and doc["date"].year == int(date[0]):
				suma += doc["time_spent"]
		return suma		

	# Tiempo gastado en un Curso. (tiempo efectivo: Tareas, Videos, Suplementos, Discusiones).	<--- Permite buscar un hostname tambien.
	def time_course(self, curso):
		suma = int()
		for doc in self.db["discusion"].find({"user" : self.user} ):
			if curso in doc["url"]:
				suma += doc["time_spent"]
		for doc in self.db["tareas"].find({"user" : self.user}):
			if curso in doc["url"]:
				suma += doc["time_spent"]
		for doc in self.db["videos"].find({"user" : self.user}):
			if curso in doc["url"]:
				suma += doc["time_spent"]		
		for doc in self.db["suplementos"].find({"user" : self.user}):
			if curso in doc["url"]:
				suma += doc["time_spent"]
		return suma

	# Tiempo gastado en un Curso y Fecha. (tiempo efectivo: Tareas, Videos, Suplementos, Discusiones).  <--- Permite buscar un hostname tambien.
	def time_course_date(self, curso, date):
		suma = int()
		date = date.split("-")
		for doc in self.db["discusion"].find({"user" : self.user} ):
			if curso in doc["url"] and doc["date"].day == int(date[2]) and doc["date"].month == int(date[1]) and doc["date"].year == int(date[0]):
				suma += doc["time_spent"]
		for doc in self.db["tareas"].find({"user" : self.user}):
			if curso in doc["url"] and doc["date"].day == int(date[2]) and doc["date"].month == int(date[1]) and doc["date"].year == int(date[0]):
				suma += doc["time_spent"]
		for doc in self.db["videos"].find({"user" : self.user}):
			if curso in doc["url"] and doc["date"].day == int(date[2]) and doc["date"].month == int(date[1]) and doc["date"].year == int(date[0]):
				suma += doc["time_spent"]		
		for doc in self.db["suplementos"].find({"user" : self.user}):
			if curso in doc["url"] and doc["date"].day == int(date[2]) and doc["date"].month == int(date[1]) and doc["date"].year == int(date[0]):
				suma += doc["time_spent"]
		return suma

	# Tiempo gastado en un Curso y evento.
	def time_course_event(self, curso, evento):
		suma = int()
		for doc in self.db[evento].find({"user" : self.user }):
			if curso in doc["url"]:
				suma += doc["time_spent"]
		return suma

	# Tiempo gastado en un Curso, Evento y fecha.		
	def time_course_event_date(self, curso, evento, date):
		suma = int()
		date = date.split("-")
		for doc in self.db[evento].find({"user" : self.user }):
			if curso in doc["url"] and doc["date"].day == int(date[2]) and doc["date"].month == int(date[1]) and doc["date"].year == int(date[0]):
				suma += doc["time_spent"]
		return suma

