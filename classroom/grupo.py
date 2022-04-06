from classroom.asignatura import Asignatura

class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas= [], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        if(lista is None):
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = lista + [alumno]

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"): # En java no hay sobrecarga de metodos !!!
        cls.grado = nombre

    def __str__(self) -> str: #To string
        return "Grupo de estudiantes: "+ self._grupo