class Question:
    def __init__(self, pitanje, ponudjen_odgovor, tacan_odgovor):
        self.pitanje_broj = 0
        self.rezultat = 0
        self.pitanje = pitanje
        self.ponudjen_odgovor = ponudjen_odgovor
        self.tacan_odgovor = tacan_odgovor


    def postavi_pitanje(self):
        print("Pitanje{} : {}".format(self.pitanje_broj + 1, self.pitanje[self.pitanje_broj]))
        odgovor = input( "Ponudjeni odgovori:{} ".format(self.ponudjen_odgovor[self.pitanje_broj])).lower()
        if odgovor == self.tacan_odgovor[self.pitanje_broj].lower():
            self.rezultat += 1
            print("Yes! tacnih odgovora: {}.".format(self.rezultat))
        else:
            print("Noup! tacnih odgovora:{}.".format(self.rezultat))
        print("Tacan odgovor:{}.".format(self.tacan_odgovor[self.pitanje_broj]))
        self.pitanje_broj += 1
        print("\n")


    def da_li_ima_jos_pitanja(self):
        return self.pitanje_broj < len(self.pitanje)
