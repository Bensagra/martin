class Entrenador:
    def __init__(self, nombre: str, especialidad: str) -> None:
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if not especialidad:
            raise ValueError("La especialidad no puede estar vacía")

        self.nombre = nombre
        self.especialidad = especialidad

    def dar_instruccion(self, atleta, equipamiento) -> str:
        return (
            f'{self.nombre} ({self.especialidad}) indica: '
            f'"{atleta.nombre}, usá {equipamiento.nombre} con buena técnica."'
        )

    def motivar(self, atleta, puntos: int = 10) -> str:
        atleta.recuperar_energia(puntos)
        return f"{self.nombre} motiva a {atleta.nombre}: +{puntos} energía."
