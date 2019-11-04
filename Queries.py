from Clase import User
from pymongo import MongoClient, ASCENDING


if __name__ == '__main__':
	conn = MongoClient()
	user_prueba = User("test@test", "prueba_1", conn)

	
	# COMPARAR VARIOS EVENTOS 
	print("Tiempo historico gastado por " + str(user_prueba.user) + ":\n", 
		  "Otros: ", user_prueba.time("otros"), "\n", 
		  "Tareas: ", user_prueba.time("tareas"), "\n", 
		  "Videos: ", user_prueba.time("videos"), "\n", 
		  "Suplementos: ", user_prueba.time("suplementos"), "\n", 
		  "Navegacion Coursera: ", user_prueba.time("navegacion_coursera"), "\n", 
		  "Discusiones: ", user_prueba.time("discusion"))
	print("-" * 60)


	#Ir a una fecha en especifico.
	print("Tiempo gastado por " + str(user_prueba.user) + " en el dia " + "2016-09-01: \n",
		"Otros: ", user_prueba.time_date("otros", "2016-09-01"), "\n",
		"Tareas: ", user_prueba.time_date("tareas", "2016-09-01"), "\n",
		"Videos: ", user_prueba.time_date("videos", "2016-09-01"), "\n",
		"Suplementos: ", user_prueba.time_date("suplementos", "2016-09-01"), "\n",
		"Navegacion Coursera: ", user_prueba.time_date("navegacion_coursera", "2016-09-01"), "\n",
		"Discusiones: ", user_prueba.time_date("discusion", "2016-09-01"))
	print("-" * 60)


	# Obtener el tiempo historico gastado en MOOC. 
	print("Tiempo historico gastado en Cursos (tiempo efectivo: Tareas, Videos, Suplementos, Discusiones) por " + str(user_prueba.user) + ":\n", 
		user_prueba.time_MOOC())
	print("-" * 60)


	# Ir a una fecha especifico y el uso en Cursos.
	print("Tiempo historico gastado en Cursos (tiempo efectivo: Tareas, Videos, Suplementos, Discusiones) por " + str(user_prueba.user) + " en el dia " + "2016-09-01: \n",
		user_prueba.time_MOOC_date("2016-09-01") )
	print("-" * 60)


	# Tiempo historico utilizado en un curso en particular.
	print("Tiempo historico (tiempo efectivo: Tareas, Videos, Suplementos, Discusiones) gastado en el curso electrones-en-accion por " +  str(user_prueba.user) + ":\n", 
		user_prueba.time_course("electrones-en-accion"))
	print("-" * 60)

	# Tiempo historico utilizado en un curso y evento:
	print("Tiempo gastado en _____ en el curso electrones-en-accion por " +  str(user_prueba.user) + ":\n",
			"Videos: ", user_prueba.time_course_event("electrones-en-accion", "videos"), "\n"
			" Suplementos: ", user_prueba.time_course_event("electrones-en-accion", "suplementos"), "\n"
			" Discuciones: ", user_prueba.time_course_event("electrones-en-accion", "discusion"), "\n"
			" Tareas: ", user_prueba.time_course_event("electrones-en-accion", "tareas"), "\n"
			" Navegacion Coursera: ", user_prueba.time_course_event("electrones-en-accion", "navegacion_coursera") )
	print("-" * 60)


	# Tiempo utilizado en un curso y una fecha en particular.
	print("Tiempo gastado (tiempo efectivo: Tareas, Videos, Suplementos, Discusiones) en el curso electrones-en-accion por " +  str(user_prueba.user) + " en el dia 2016-09-01: \n", 
		user_prueba.time_course_date("electrones-en-accion", "2016-09-01"))
	print("-" * 60)

	# Tiempo utilizado en un curso, evento y fecha.

	print("Tiempo gastado en _____ en el curso electrones-en-accion por " +  str(user_prueba.user) + " en el dia 2016-09-01:\n",
			"Videos: ", user_prueba.time_course_event_date("electrones-en-accion", "videos", "2016-09-01"), "\n"
			" Suplementos: ", user_prueba.time_course_event_date("electrones-en-accion", "suplementos", "2016-09-01"), "\n"
			" Discuciones: ", user_prueba.time_course_event_date("electrones-en-accion", "discusion", "2016-09-01"), "\n"
			" Tareas: ", user_prueba.time_course_event_date("electrones-en-accion", "tareas", "2016-09-01"), "\n"
			" Navegacion Coursera: ", user_prueba.time_course_event_date("electrones-en-accion", "navegacion_coursera", "2016-09-01") )
	print("-" * 60)


