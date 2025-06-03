import tkinter as tk

class Kreslic:
    def __init__(self):
        self.slovo = "ahoj"
        self.policka = []
        self.chyby = 0
        
        self.root = tk.Tk()
        self.canvas = tk.Canvas(width=500, height=600, bg="white")
        self.canvas.pack()
        
        self.casti = Casti(self.canvas)
        self.casti.nakresli_pozadie()
        self.casti.nakresli_gilotinu()
        self.policka = self.casti.nakresli_policka(self.slovo)        

        self.text = tk.Text(self.root, height=1, width=10)
        self.text.pack()

        button = tk.Button(self.root, text="Vyber", command=self.Vyhodnot)
        button.pack()

    def Vyhodnot(self):
        self.canvas.delete("vyhodnotenie")
        hodnota = self.text.get("1.0", "end-1c")
        self.text.delete("1.0")

        if hodnota in self.slovo:
            self.canvas.create_text(300, 550, font=("Arial", 20), text="Áno", fill="green", tag="vyhodnotenie")
            for i in range(len(self.slovo)):
                if self.slovo[i] == hodnota:
                    coords = self.canvas.coords(self.policka[i])
                    x1 = coords[0]
                    y1 = coords[1]
                    self.canvas.delete(self.policka[i])
                    self.canvas.create_text(x1,y1, text=hodnota, font=("Arial", 20))

        else:
            self.canvas.create_text(300, 550, font=("Arial", 20), text="Nie", fill="red", tag="vyhodnotenie")
            self.chyby += 1
            self.casti.nakresli_cloveka(self.chyby)

class Casti:
    def __init__(self, canvas):
        self.canvas = canvas

    def nakresli_pozadie(self):
        self.canvas.create_rectangle(0,0, 500,400, fill="lightblue")

    def nakresli_gilotinu(self):
        # Zem (podlaha)
        self.canvas.create_rectangle(0,380,500,410, fill="green")
        self.canvas.create_rectangle(20,20,50,390, fill="black")
        self.canvas.create_rectangle(50,20,300,50, fill="black")
        self.canvas.create_rectangle(250,20,260,100, fill="black")

    def nakresli_policka(self, slovo):
        policka = []
        offset = 600 - (len(slovo)+2) * 50
        for i in range(len(slovo)):
            x1 = offset / 2 + 10 +(i * 50)
            x2 = x1 + 20
            y1 = 500
            y2 = 501
            policko = self.canvas.create_rectangle(x1,y1,x2,y2)
            policka.append(policko)
        return policka

    def nakresli_cloveka(self, chyba):
        if chyba == 1:
            self.canvas.create_oval(220,100,290,170, fill="black")
        if chyba == 2:
            self.canvas.create_rectangle(240,170,270,370, fill="black")
        if chyba == 3:
            self.canvas.create_rectangle(200,200,240,220, fill="black")
        if chyba == 4:
            self.canvas.create_rectangle(270,200,310,220, fill="black")
        if chyba == 5:
            self.canvas.create_rectangle(220,350,240,420, fill="black")
        if chyba == 6:
            self.canvas.create_rectangle(270,350,290,420, fill="black")

Kreslic()
