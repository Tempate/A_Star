import matplotlib.pyplot as plt


class Gui:
    def __init__(self, data):
        self.data = data
        plt.ion()

    def draw_graph(self, path, permanent=False):
        lines = {
            "red": ['Aghios Antonios', 'Sepolia', 'Attiki', 'Larissa Station', 'Metaxourghio', 'Omonia', 'Panepistimio', 'Syntagma', 'Akropoli', 'Sygrou', 'Neos Kosmos', 'Aghios Ioannis', 'Dafni', 'Aghios Dimitrios'],
            "blue": ['Egaleo', 'Eleonas', 'Kerameikos', 'Monastiraki', 'Syntagma', 'Evangelismos', 'Megaro Moussinis', 'Ambelokipi', 'Panormu', 'Katehaki', 'Ethniki Amnya', 'Holargos', 'Nomismatokopio', 'Agia Paraskevi', 'Holandri', 'Doukissis Plakentias'],
            "green": ['Piraeus', 'Faliro', 'Moschato', 'Kallithea', 'Tavros', 'Petralona', 'Thissio', 'Monastiraki', 'Omonia', 'Viktoria', 'Attiki', 'Aghios Nikolaos', 'Kato Patissia', 'Aghios Eleftherios', 'Ano Patissia', 'Perissos', 'Pefkakia', 'Nea Ionia', 'Iraklio', 'Irini', 'Neratziotissa', 'Maroussi', 'Kat', 'Kifissia']
        }

        for color in lines.keys():
            plt.plot(*self.get_rect(lines[color]), color=color, marker="o", markersize=10, markerfacecolor="white")

        for node in path:
            plt.plot(node.x, node.y, color="orange", marker="o", markersize=9)
        
        plt.gca().invert_yaxis()

        if permanent:
            plt.ioff()
            plt.show()
        else:
            plt.draw()
            plt.pause(0.001)
            plt.clf()



    def get_rect(self, stations):
        x = []
        y = []

        for station in stations:
            x.append(self.data[station]["x"])
            y.append(self.data[station]["y"])

        return [x, y]
