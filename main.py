from optparse import OptionParser
from core.a_star import A_Star

import json


def main():
    graph = parse_graph_json(read_commands())
    a_star = A_Star(graph, '0', '3')
    a_star.run()


def read_commands():
    parser = OptionParser("%prog -f <graph_json>")
    parser.add_option("-f", dest="input", help="JSON file with graph")

    (options, args) = parser.parse_args()

    # Mostrar los ayuda si no se especifica el archivo a leer
    if not options.input:
        parser.print_help()
        exit(0)

    return options.input


def parse_graph_json(file_name):
    with open(file_name) as file:
        return json.loads(file.read())


if __name__ == "__main__":
    main()
