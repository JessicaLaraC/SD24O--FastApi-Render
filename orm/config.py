#Configuración de conexión a la BD, asi como la funcion para crear conexiones 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_BASE_DATOS = "postgresql://usuario-ejemplo:741963@localhost:5432/alumnos"
engine = create_engine(URL_BASE_DATOS,
                       connect_args={
                           "options": "-csearch_path=app"                           
                       })
SessionClass = sessionmaker(engine)

def generador_sesion():
    sesion = SessionClass()
    try:
        yield sesion
    finally:
        sesion.close()

BaseClass = declarative_base ()