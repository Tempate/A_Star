from optparse import OptionParser

from core.a_star import A_Star

import json


def main():
    options = read_commands()
    graph = parse_graph_json(options.graph)

    a_star = A_Star(graph, options.origin, options.target)
    a_star.run()


def read_commands():
    parser = OptionParser("%prog -g <graph_json>")
    parser.add_option("-g", dest="graph", help="JSON file with graph")
    parser.add_option("-o", dest="origin", help="Station at the origin")
    parser.add_option("-t", dest="target", help="Station at the target")

    (options, args) = parser.parse_args()

    # Show help if no input graph is given
    if not options.graph:
        parser.print_help()
        exit(0)

    return options


def parse_graph_json(file_name):
    with open(file_name) as file:
        return json.loads(file.read())


if __name__ == "__main__":
    main()
