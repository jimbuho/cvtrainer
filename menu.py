from capturar_imagen import ImageCapture
from entrenar_imagen import TrainPictures
from probar_imagen import TestImage

def menu():
    print('1. Capturar imagenes')
    print('2. Entrenar con imagenes')
    print('3. Mostrar resultados')
    print('0. Salir')
    option = input("Seleccione una opcion: ")
    return option

def main():
    while True:
        option = menu()
        
        if option == '1':
            person_name = input("Ingrese su nombre: ")

            print("Bienvenido {} al registro de imagenes. Vamos a iniciar la digitalización de su rostro,"\
                "para terminar pulse ESC o espere hasta que hayamos terminado.".format(person_name))
            print("Pulse ENTER para continuar...")
            input()
            capturer = ImageCapture(person_name)
            capturer.capture()
        elif option == '2':
            print("Bienvenido al entrenamiento con imagenes.")
            print("Pulse ENTER para continuar...")
            input()
            trainer = TrainPictures()
            trainer.training()
        elif option == '3':
            print("Bienvenido al reconocimiento de imagenes.")
            print("Pulse ENTER para continuar...")
            input()
            tester = TestImage()
            tester.recognize()
        elif option == '0':
            break

    print('Adios!')

if __name__ == "__main__":
    main()