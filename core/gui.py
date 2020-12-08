import matplotlib.pyplot as plt


class Gui:
    def __init__(self, data):
        self.data = data
        plt.ion()

    def draw_graph(self, path, permanent=False):
        lines = {
            "red": ['Aghios Antonios', 'Sepolia', 'Attiki(red)', 'Larissa Station', 'Metaxourghio', 'Omonia(red)', 'Panepistimio', 'Syntagma(blue)', 'Akropoli', 'Sygrou', 'Neos Kosmos', 'Aghios Ioannis', 'Dafni', 'Aghios Dimitrios'],
            "blue": ['Egaleo', 'Eleonas', 'Kerameikos', 'Monastiraki(blue)', 'Syntagma(blue)', 'Evangelismos', 'Megaro Moussinis', 'Ambelokipi', 'Panormu', 'Katehaki', 'Ethniki Amnya', 'Holargos', 'Nomismatokopio', 'Agia Paraskevi', 'Holandri', 'Doukissis Plakentias'],
            "green": ['Piraeus', 'Faliro', 'Moschato', 'Kallithea', 'Tavros', 'Petralona', 'Thissio', 'Monastiraki(green)', 'Omonia(green)', 'Viktoria', 'Attiki(green)', 'Aghios Nikolaos', 'Kato Patissia', 'Aghios Eleftherios', 'Ano Patissia', 'Perissos', 'Pefkakia', 'Nea Ionia', 'Iraklio', 'Irini', 'Neratziotissa', 'Maroussi', 'Kat', 'Kifissia']
        }

        for color in lines.keys():
            plt.plot(*self.get_rect(lines[color]), color=color, marker="o", markersize=10, markerfacecolor="white")

        for node in path:
            plt.plot(node.x, node.y, color="orange", marker="o", markersize=9)
            
        
        plt.gca().invert_yaxis()

        if permanent: 
            for node in path:
               plt.annotate(node.name,[node.x +5,node.y+20],bbox = dict(boxstyle ="round", fc ="0.8"),fontsize= 9)
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
