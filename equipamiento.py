class Equipamiento:
    def __init__(self, nombre: str, usos_antes_de_mantenimiento: int = 3) -> None:
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if usos_antes_de_mantenimiento <= 0:
            raise ValueError("Los usos antes de mantenimiento deben ser > 0")

        self.nombre = nombre
        self.disponible = True
        self._usos_antes_de_mantenimiento = usos_antes_de_mantenimiento
        self._usos_desde_mantenimiento = 0

    def usar(self) -> str:
        if not self.disponible:
            raise ValueError(f"{self.nombre} no está disponible (requiere mantenimiento).")

        self._usos_desde_mantenimiento += 1

        if self._usos_desde_mantenimiento >= self._usos_antes_de_mantenimiento:
            self.disponible = False
            return (
                f"Se usó {self.nombre}. Quedó fuera de servicio: "
                "requiere mantenimiento."
            )

        restantes = self._usos_antes_de_mantenimiento - self._usos_desde_mantenimiento
        return f"Se usó {self.nombre}. Usos restantes antes de mantenimiento: {restantes}."

    def realizar_mantenimiento(self) -> str:
        self._usos_desde_mantenimiento = 0
        self.disponible = True
        return f"Mantenimiento realizado a {self.nombre}. Ya está disponible."
