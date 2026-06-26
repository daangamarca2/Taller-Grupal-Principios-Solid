from abc import ABC, abstractmethod

class Participante(ABC):
    def __init__(self, nombre: str, nacionalidad: str, id_participante: int):
        self._nombre = nombre
        self._nacionalidad = nacionalidad
        self._id = id_participante

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def nacionalidad(self) -> str:
        return self._nacionalidad

    @property
    def id(self) -> int:
        return self._id

    @abstractmethod
    def obtener_detalles(self) -> str:
        pass


class Jugador(Participante):
    def __init__(self, nombre: str, nacionalidad: str, id_participante: int, posicion: str):
        super().__init__(nombre, nacionalidad, id_participante)
        self._posicion = posicion

    def obtener_detalles(self) -> str:
        return f"Jugador: {self.nombre} ({self.nacionalidad}) - Posición: {self._posicion}"


class Entrenador(Participante):
    def __init__(self, nombre: str, nacionalidad: str, id_participante: int, experiencia: int):
        super().__init__(nombre, nacionalidad, id_participante)
        self._experiencia = experiencia

    def obtener_detalles(self) -> str:
        return f"Entrenador: {self.nombre} - Experiencia: {self._experiencia} años"


class Arbitro(Participante):
    def __init__(self, nombre: str, nacionalidad: str, id_participante: int, categoria: str):
        super().__init__(nombre, nacionalidad, id_participante)
        self._categoria = categoria

    def obtener_detalles(self) -> str:
        return f"Árbitro: {self.nombre} - Categoría: {self._categoria}"


class Reporte(ABC):
    @abstractmethod
    def generar(self, participante: Participante):
        pass

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, participante: Participante):
        pass

class Persistencia(ABC):
    @abstractmethod
    def guardar(self, participante: Participante):
        pass


class ReportePDF(Reporte):
    def generar(self, participante: Participante):
        print(f"[PDF] Generando documento PDF para: {participante.nombre}")

class ReporteExcel(Reporte):
    def generar(self, participante: Participante):
        print(f"[EXCEL] Generando hoja de cálculo para: {participante.nombre}")


class Correo(Notificacion):
    def enviar(self, participante: Participante):
        print(f"[EMAIL] Enviando correo a {participante.nombre}")

class WhatsApp(Notificacion):
    def enviar(self, participante: Participante):
        print(f"[WHATSAPP] Enviando mensaje a {participante.nombre}")


class BaseDatos(Persistencia):
    def guardar(self, participante: Participante):
        print(f"[BD] Ejecutando INSERT en base de datos para ID: {participante.id}")

class Archivo(Persistencia):
    def guardar(self, participante: Participante):
        print(f"[ARCHIVO] Guardando en TXT local los datos de ID: {participante.id}")


class GestorMundial:
    def __init__(self, reporte: Reporte, notificacion: Notificacion, persistencia: Persistencia):
        self.participantes = []
        self.reporte = reporte
        self.notificacion = notificacion
        self.persistencia = persistencia

    def registrar_participante(self, participante: Participante):
        print("\n--- Procesando Registro ---")
        print(participante.obtener_detalles())
        self.participantes.append(participante)
        
        self.persistencia.guardar(participante)
        self.reporte.generar(participante)
        self.notificacion.enviar(participante)
        print("---------------------------\n")


if __name__ == "__main__":
    gestor = GestorMundial(ReportePDF(), WhatsApp(), BaseDatos())

    while True:
        print("¿Qué desea hacer?")
        print("1. Ingresar Jugador")
        print("2. Ingresar Entrenador")
        print("3. Ingresar Árbitro")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "4":
            break

        if opcion in ["1", "2", "3"]:
            nombre = input("Nombre: ")
            nacionalidad = input("Nacionalidad: ")
            id_participante = int(input("ID: "))

            nuevo_participante = None

            if opcion == "1":
                posicion = input("Posición: ")
                nuevo_participante = Jugador(nombre, nacionalidad, id_participante, posicion)
            elif opcion == "2":
                exp = int(input("Años de experiencia: "))
                nuevo_participante = Entrenador(nombre, nacionalidad, id_participante, exp)
            elif opcion == "3":
                cat = input("Categoría: ")
                nuevo_participante = Arbitro(nombre, nacionalidad, id_participante, cat)

            if nuevo_participante:
                gestor.registrar_participante(nuevo_participante)
        else:
            print("Opción inválida.")