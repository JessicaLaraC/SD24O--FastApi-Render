# Mediante el uso de la biblioteca SQLAlchemy, implementa las siguientes consultas (select y delete) a la BD.
import orm.modelos as modelos
from sqlalchemy.orm import Session
import orm.esquemas as esquemas

# SELECT * FROM app.alumnos
def mostrar_alumnos(sesion:Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()
# SELECT * FROM app.alumnos WHERE id={id_al}
def alumnos_por_id(sesion:Session, id_al:int):
    print("SELECT * FROM app.alumnos WHERE id={id_al}", id_al)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_al).first()
# SELECT * FROM app.fotos
def mostrar_fotos (sesion:Session):
    print("SELECT * FROM app.fotos")
    return sesion.query(modelos.Foto).all()
# SELECT * FROM app.fotos WHERE id={id_fo}
def fotos_por_id(sesion:Session, id_fo:int):
    print("SELECT * FROM app.fotos WHERE id={id_fo}", id_fo)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_fo).first()
# SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def fotos_por_id_alumno (sesion:Session, id_al:int):
    print("SELECT * FROM app.fotos WHERE id_alumnos={id_al}", id_al)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_al).all()
# SELECT * FROM app.calificaciones
def mostrar_calificaciones(sesion:Session):
    print("SELECT * FROM app.calificaciones")
    return sesion.query(modelos.Calificacion).all()
# SELECT * FROM app.calificaciones WHERE id={id_fo}
def calificaciones_por_id(sesion:Session, id_califi:int):
    print("SELECT * FROM app.calificaciones WHERE id={id_califi}", id_califi)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id== id_califi).first()
# SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
def calificaciones_por_id_alumno(sesion:Session, id_al:int):
    print("SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}", id_al)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id_al).all()
# DELETE FROM app.alumnos WHERE id_alumnos={id_al}
def borrar_alumno_por_id(sesion: Session, id_al: int):
    print(f"DELETE FROM app.alumnos WHERE id={id_al}")
    alumno = alumnos_por_id(sesion, id_al)
    if alumno is not None:
        sesion.delete(alumno)
        sesion.commit()
        return {"mensaje": f"Alumno con id={id_al} eliminado exitosamente"}
    return {"mensaje": f"No se encontró el alumno con id={id_al}"}

# DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
def borrar_califi_por_id_alum(sesion:Session, id_al:int):
    print("DELETE FROM app.calificaciones WHERE id_alumnos={id_al}", id_al)
    califi_alumn = calificaciones_por_id_alumno(sesion, id_al)
    if califi_alumn is not None:
        for cali_alumno in califi_alumn:
            sesion.delete(cali_alumno)
    sesion.commit()
# DELETE FROM app.fotos WHERE id_alumnos={id_al}
def borrar_foto_por_id(sesion:Session, id_al:int):
    print("DELETE FROM app.fotos WHERE id_alumnos={id_al}", id_al)
    foto_alumn = fotos_por_id_alumno(sesion, id_al)
    if foto_alumn is not None:
        for foto_alumno in foto_alumn:
            sesion.delete(foto_alumno)
    sesion.commit()
    
#INSERT INTO app.alumnos () VALUES ()
def guardar_alumnos(sesion:Session, alum_nuevo_esquema:esquemas.BaseModel):
    alum_bd = modelos.Alumno()
    alum_bd.nombre = alum_nuevo_esquema.nombre
    alum_bd.edad = alum_nuevo_esquema.edad
    alum_bd.domicilio = alum_nuevo_esquema.domicilio
    alum_bd.carrera = alum_nuevo_esquema.carrera
    alum_bd.trimestre = alum_nuevo_esquema.trimestre
    alum_bd.email = alum_nuevo_esquema.email
    alum_bd.password = alum_nuevo_esquema.password

    sesion.add(alum_bd)
    sesion.commit()
    sesion.refresh(alum_bd)
    return alum_bd
#UPDATE app.alumnos SET WHERE id = {id_al}
def actualizar_alumno(sesion:Session, id_al:int, alum_esquema:esquemas.BaseModel):
    alum_bd = alumnos_por_id(sesion, id_al)
    if alum_bd is not None:
        alum_bd.nombre = alum_esquema.nombre
        alum_bd.edad = alum_esquema.edad
        alum_bd.domicilio = alum_esquema.domicilio
        alum_bd.carrera = alum_esquema.carrera
        alum_bd.trimestre = alum_esquema.trimestre
        alum_bd.email = alum_esquema.email
        alum_bd.password = alum_esquema.password
        
        sesion.commit()
        sesion.refresh(alum_bd)
        print(alum_esquema)
        return alum_esquema
    else:
        respuesta= {"mensaje": "No existe el alumno"}
        return respuesta 

#INSERT INTO app.calificaciones() VALUES ()
def guardar_califi_por_id_alum (sesion:Session, id_alumno:int, alum_nuevo_esquema:esquemas.BaseModel):
    alumno = alumnos_por_id(sesion, id_alumno)
    if alumno is not None:
        alum_bd = modelos.Calificacion()
        alum_bd.id_alumno = alumno.id
        alum_bd.uea = alum_nuevo_esquema.uea
        alum_bd.calificacion = alum_nuevo_esquema.calificacion
        sesion.add(alum_bd)
        sesion.commit()
        sesion.refresh(alum_bd)
        return alum_bd
    else:
        return {"mensaje": "No existe el alumno"}

#UPDATE app.calificaciones SET WHERE id = {id_al}
def actualizar_califi_por_id(sesion:Session,id_califi:int, alum_esquema:esquemas.CalificacionBase):
    alum_bd = calificaciones_por_id(sesion, id_califi)
    if alum_bd is not None:
        alum_bd.uea = alum_esquema.uea
        alum_bd.calificacion = alum_esquema.calificacion
        sesion.commit()
        sesion.refresh(alum_bd)
        print(alum_esquema)
        return alum_esquema
    else:
        respuesta = {"mensaje": "No existe la compra"}
        return respuesta 

#INSERT INTO app.fotos() VALUES ()
def guardar_foto_por_id_alum(sesion:Session, id_alumno:int, alum_nuevo_esquema:esquemas.BaseModel):
    alumno = alumnos_por_id(sesion, id_alumno)
    if alumno is not None:
        alum_bd = modelos.Foto()
        alum_bd.id_alumno = alumno.id
        alum_bd.titulo = alum_nuevo_esquema.titulo
        alum_bd.descripcion = alum_nuevo_esquema.descripcion
        alum_bd.ruta = alum_nuevo_esquema.ruta
        sesion.add(alum_bd)
        sesion.commit()
        sesion.refresh(alum_bd)
        return alum_bd
    else:
        return {"mensaje": "No existe el alumno"}

#UPDATE app.fotos SET WHERE id = {id_al}
def actualizar_foto_por_id(sesion:Session,id_fo:int, alum_esquema:esquemas.CalificacionBase):
    alum_bd = fotos_por_id(sesion, id_fo)
    if alum_bd is not None:
        alum_bd.titulo = alum_esquema.titulo
        alum_bd.descripcion = alum_esquema.descripcion
        alum_bd.ruta = alum_esquema.ruta
        sesion.commit()
        sesion.refresh(alum_bd)
        print(alum_esquema)
        return alum_esquema
    else:
        respuesta = {"mensaje": "No existe la Foto"}
        return respuesta 