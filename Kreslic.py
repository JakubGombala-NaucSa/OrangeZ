import tkinter as tk
from Casti import Casti

class Kreslic:
    def __init__(self, slovo):
        self.chyby = 0
        self.slovo = slovo
        self.pismenka = []

        self.root = tk.Tk()
        self.canvas = tk.Canvas(width=500, height=600, bg="white")
        self.canvas.pack()
        
        self.casti = Casti(self.canvas, self.slovo)
        self.casti.nakresli_pozadie()
        self.casti.nakresli_Sibenicu()
        self.policka = self.casti.nakresli_policka()
        
        self.txt = tk.Text(self.root, height=1, width=10)
        self.txt.pack()
        self.btn = tk.Button(self.root, text="Print", command=self.vyhodnot)
        self.btn.pack()

        self.root.mainloop()


    def vyhodnot(self):
        self.canvas.delete("vysledok")
        vstup = self.txt.get("1.0", "end-1c")
        self.txt.delete("1.0", "end")

        if vstup.lower() in self.pismenka:
            self.canvas.create_text(250, 550, text=f"{vstup.lower()} si uz skusal", font=("Arial", 20), fill="orange", tag="vysledok")
            return
        self.pismenka.append(vstup.lower())

        if vstup.lower() in self.slovo.lower():
            self.canvas.create_text(250, 550, text="Pismeno sa nachadza v slove", font=("Arial", 20), fill="green", tag="vysledok")
            self.skontroluj_pismenko(vstup.lower())          
        else:
            self.canvas.create_text(250, 550, text="Pismeno sa v slove nenachadza", font=("Arial", 20), fill="red", tag="vysledok")
            
            self.casti.nakresli_cloveka(self.chyby)
            self.chyby += 1
            if self.chyby == 6:
                self.canvas.delete("vysledok")
                t = "Prehral si, hladane slovo bolo " + self.slovo
                self.canvas.create_text(250, 550, text=t, font=("Arial", 20), fill="red", tag="vysledok")
            

    def skontroluj_pismenko(self, pismeno):
        for i in range(len(self.slovo)):
            if self.slovo[i].lower() == pismeno:
                policko = self.policka[i]
                coords = self.canvas.coords(policko)
                x1, y1, x2, y2 = coords
                self.canvas.create_text((x1+x2)/2, 500, text=self.slovo[i].upper(), font=("Arial", 20), fill="black")
                self.canvas.delete(policko)