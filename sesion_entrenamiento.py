from atleta import Atleta
from entrenador import Entrenador
from equipamiento import Equipamiento


class SesionEntrenamiento:
    """Clase nexo: relaciona Atleta + Entrenador + Equipamiento."""

    def __init__(
        self, atleta: Atleta, entrenador: Entrenador, equipamiento: Equipamiento
    ) -> None:
        self.atleta = atleta
        self.entrenador = entrenador
        self.equipamiento = equipamiento

    def ejecutar(self, consumo_energia: int = 20) -> list:
        """Demuestra interacción total: orden -> uso de equipo -> baja de energía."""
        eventos = []

        eventos.append(self.entrenador.dar_instruccion(self.atleta, self.equipamiento))
        eventos.append(self.equipamiento.usar())

        energia_antes = self.atleta.energia
        self.atleta.entrenar(consumo_energia)
        eventos.append(
            f"{self.atleta.nombre} entrenó y bajó de {energia_antes} a {self.atleta.energia} energía."
        )

        return eventos
