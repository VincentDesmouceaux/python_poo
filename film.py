class Film:

    def __init__(self,name):

       self.name = name

    def watch(self):
        print("Bon visionnage")   

class FilmCassette(Film):
    """Un film en cassette !"""

    def __init__(self, name):
        """Initialise le nom et la bande magnetique."""
        super().__init__(name)
        self.magnetic_tape = True
    
    def rewind(self):
        """Rembobine le film."""
        print("C'est long à rembobiner !")
        self.magnetic_tape = True


# Création d'une instance de Film
mon_film = Film("Les Aventuriers de l'Arche Perdue")
mon_film.watch()  # Cela devrait afficher "Bon visionnage"

# Création d'une instance de FilmCassette
ma_cassette = FilmCassette("Retour vers le futur")
ma_cassette.watch()  # Héritée de Film, affiche également "Bon visionnage"
ma_cassette.rewind()  # Affiche "C'est long à rembobiner !"
