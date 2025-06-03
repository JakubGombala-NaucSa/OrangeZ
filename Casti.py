class Casti:
    def __init__(self, canvas, slovo):
        self.canvas = canvas
        self.slovo = slovo

    def nakresli_Sibenicu(self):
        self.canvas.create_rectangle(0,390,500,420, fill="green")
        self.canvas.create_rectangle(10,10,30,400, fill="black")
        self.canvas.create_rectangle(10,10,300,30, fill="black")
        self.canvas.create_rectangle(250,30,255,80, fill="black")

    def nakresli_policka(self):
        policka = []
        offset = 600 - (len(self.slovo)+2) * 50
        for i in range(len(self.slovo)):
            x1 = offset / 2 + 10 +(i * 50)
            x2 = x1 + 20
            policko = self.canvas.create_rectangle(x1,500,x2,501, tag=i)
            policka.append(policko) 
        return policka
    
    def nakresli_pozadie(self):
        self.canvas.create_rectangle(0,0,500,400, fill="lightblue")

    def nakresli_cloveka(self, i):
        if i == 0:
            # Hlava
            self.canvas.create_oval(222,80,282,140,fill="black")
        if i == 1:
            # Telo
            self.canvas.create_rectangle(252,140,253,250)
        if i == 2:
            # L Ruka
            self.canvas.create_rectangle(200,170,252,171)
        if i == 3:
            # P Ruka
            self.canvas.create_rectangle(253,170,301,171)
        if i == 4:
            # L Noha
            self.canvas.create_rectangle(241,240,251,360, fill="black")
        if i == 5:
            # P Noha
            self.canvas.create_rectangle(254,240,264,360, fill="black")