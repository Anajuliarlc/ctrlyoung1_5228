class Animal():
    def __init__(self, nome, familia, especie):
        self.nome = nome
        self.familia = familia
        self.especie = especie

    def falar(self, som):
        print(f"{self.nome} faz: {som}")


animal1 = Animal("Leão", "Felídeos", "Panthera leo")
animal1.falar("Rawr")

animal2 = Animal("Gato", "Felino", "gatitos felinus")
animal2.falar("miauuuu")