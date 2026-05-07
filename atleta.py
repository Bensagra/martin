class Atleta:
    def __init__(self, nombre: str, energia: int = 100) -> None:
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if energia < 0:
            raise ValueError("La energía no puede ser negativa")

        self.nombre = nombre
        self.energia = energia

    def entrenar(self, consumo_energia: int) -> None:
        """Acción principal del atleta: consume energía."""
        if consumo_energia <= 0:
            raise ValueError("El consumo de energía debe ser mayor a 0")
        if self.energia < consumo_energia:
            raise ValueError(
                f"{self.nombre} no tiene energía suficiente (tiene {self.energia})."
            )

        self.energia -= consumo_energia

    def recuperar_energia(self, puntos: int, maximo: int = 100) -> None:
        if puntos <= 0:
            raise ValueError("Los puntos a recuperar deben ser mayor a 0")
        if maximo <= 0:
            raise ValueError("El máximo debe ser mayor a 0")

        self.energia = min(maximo, self.energia + puntos)
