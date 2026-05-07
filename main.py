from atleta import Atleta
from entrenador import Entrenador
from equipamiento import Equipamiento
from sesion_entrenamiento import SesionEntrenamiento


def main() -> None:
    atleta = Atleta(nombre="Martina", energia=80)
    entrenador = Entrenador(nombre="Diego", especialidad="Fuerza")
    equipamiento = Equipamiento(nombre="Banco de press", usos_antes_de_mantenimiento=3)

    sesion = SesionEntrenamiento(
        atleta=atleta, entrenador=entrenador, equipamiento=equipamiento
    )

    for evento in sesion.ejecutar(consumo_energia=25):
        print(evento)


if __name__ == "__main__":
    main()
