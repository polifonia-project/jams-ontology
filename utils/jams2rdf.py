import os
import sys
from subprocess import check_output, CalledProcessError

from rdflib import Graph, URIRef

query_current = "queries/current.rq"

query_test = "queries/jams_ontology.sparql"

choco_namespace = "http://purl.org/choco/data/"


def jams2rdf(input_file: str, output=None, output_format: str = 'ttl'):
    with open(query_test, 'r') as r:
        query_for_file = r.read().replace("%FILEPATH%", input_file)
        with open(query_current, 'w') as w:
            w.write(query_for_file)

    g = Graph()

    try:
        out = check_output(["java", "-jar", "./bin/sa.jar", "-q", query_current])
        g.parse(out)
    except CalledProcessError as e:
        print(e)
        print("Output graph is empty for {}".format(input_file))
        pass

    # Replace root node name

    foo_uri = URIRef(choco_namespace + 'foo')
    jams_file = input_file.split('/')[-1].split('.')[0]
    jams_collection = input_file.split('/')[6]
    resource_uri = URIRef(choco_namespace + jams_collection + '/' + jams_file)
    for s, p, o in g.triples((foo_uri, None, None)):
        g.add((resource_uri, p, o))
        g.remove((s, p, o))

    if output:
        with open(output, 'w') as wo:
            wo.write(g.serialize(format=output_format))
    else:
        print(g.serialize(format=output_format))

    os.remove(query_current)


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: {0} <input file> [<output file>]".format(sys.argv[0]))
        exit(2)
    elif len(sys.argv) == 2:
        # Conversion to stdout 
        infilename = sys.argv[1]
        jams2rdf(os.path.abspath(infilename))
    elif len(sys.argv) == 3:
        # Conversion to file
        infilename = sys.argv[1]
        outfilename = sys.argv[2]
        jams2rdf(os.path.abspath(infilename), outfilename)

    exit(0)
