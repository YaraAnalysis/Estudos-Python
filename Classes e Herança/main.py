from Mamifero import Mamifero
from Reptil import Reptil

if __name__ == '__main__':

    animal1 = Mamifero('Vaca', 2.5)
    animal2 = Reptil('Jacaré', 3.9)

    animal1.respirar()
    animal2.respirar()

    animal1.alimentar()
    animal2.botar_ovo()