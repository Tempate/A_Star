from optparse import OptionParser

from core.a_star import A_Star

import json


def main():
    graph = parse_graph_json(read_commands())

    a_star = A_Star(graph, "Holargos", "Irini")
    a_star.run()


def read_commands():
    parser = OptionParser("%prog -g <graph_json>")
    parser.add_option("-g", dest="graph", help="JSON file with graph")

    (options, args) = parser.parse_args()

    # Show help if no input graph is given
    if not options.graph:
        parser.print_help()
        exit(0)

    return options.graph


def parse_graph_json(file_name):
    with open(file_name) as file:
        return json.loads(file.read())


if __name__ == "__main__":
    main()
