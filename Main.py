from random import choice
from Kreslic import Kreslic

class Main:
    def __init__(self):
        with open(".\Obesenec\slova.txt","r") as file:
            riadky = file.readlines()
            slovo = choice(riadky).rstrip()
        print(slovo)
        Kreslic(slovo)


if __name__ == "__main__":
    Main()
