#Configuración de conexión a la BD, asi como la funcion para crear conexiones 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#importar el modelo de archivos 
from orm import modelos
import os

#URL_BASE_DATOS = "postgresql://usuario-ejemplo:741963@localhost:5432/alumnos"
#engine = create_engine(URL_BASE_DATOS,
#                       connect_args={
#                           "options": "-csearch_path=app"                           
#                      })
#
engine = create_engine (os.getenv("db_uri", "sqlite:///base-ejemplo.db")) 
modelos.BaseClass.metadata.create_all(engine)

SessionClass = sessionmaker(engine)
def generador_sesion():
    sesion = SessionClass()
    try:
        yield sesion
    finally:
        sesion.close()
