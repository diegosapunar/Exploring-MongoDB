'''
Script que crea la base de datos en mongo. 
Y también tiene la función de parsear el json y cargarlo en las colecciones correspondientes.

'''
import json
from pymongo import MongoClient, ASCENDING
import sys
import time
from datetime import datetime

def create_db(connection, name_db, index):
	db = connection[name_db]

	discusion  = db["discusion"]
	discusion.create_index(index)

	tareas  = db["tareas"]
	tareas.create_index(index)

	videos  = db["videos"]
	videos.create_index(index)

	suplementos  = db["suplementos"]
	suplementos.create_index(index)

	navegacion_coursera  = db["navegacion_coursera"]
	navegacion_coursera.create_index(index)

	otros  = db["otros"]
	otros.create_index(index)

	return {"discusion" : discusion, "tareas": tareas, "videos" : videos, "suplementos": suplementos, "navegacion_coursera" : navegacion_coursera, "otros": otros}


def insert_json(colecctions, path):
	with open (path) as data_file:
			data_file = (json.load(data_file))
			for i in data_file:
				document = {"user" : data_file[i]["user"], "url" : data_file[i]["tabUrl"], "time_spent": round(data_file[i]['endTime'] - data_file[i]['startTime']), \
						    "date" : datetime.strptime(time.strftime('%m-%d-%Y %H:%M:%S',  time.gmtime(round(data_file[i]['startTime']))), '%m-%d-%Y %H:%M:%S') }
				
				if "coursera" in document["url"]:
					
					if "/discussions" in document["url"]:
						# agregar a collecion discusion
						colecctions["discusion"].insert(document)

					elif "/exam" in document["url"] or "/quiz" in document["url"]:
						#agregar a collecion tareas
						colecctions["tareas"].insert(document)
					
					elif "lecture" in document["url"]:
						#agregar collecion videos
						colecctions["videos"].insert(document)

					elif "/supplement" in document["url"]:
						#agregar a coleccion suplementos
						colecctions["suplementos"].insert(document)

					else:
						#agregar a coleccion navegacion_coursera
						colecctions["navegacion_coursera"].insert(document)
				else:
					colecctions["otros"].insert(document)
					#aregar a collecion otros


			
if __name__ == '__main__':
	try:
		conn = MongoClient('localhost', 27017)
	except:
		print("PROBLEMA: No se pudo conectar al servidor")


	insert_json(create_db(conn, "prueba_1", "user"), "C:\\Users\\Diego\\Documents\\Universidad\\Investigacion en MOOC's\\analisis_url\\Simulacion\\json_simulacion.json")
