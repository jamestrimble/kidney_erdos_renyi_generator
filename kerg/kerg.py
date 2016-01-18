import argparse
import random

def generate_input(n, p):
    """Generate a .input instance, printing to standard output.

    Args:
        n: Number of patient-donor pairs
        p: Edge probability
    """

    edges = []
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < p:
                edges.append((i, j))

    print "{}\t{}".format(n, len(edges))
    for edge in edges:
        # Print source patient-donor pair, target patient-donor pair, weight
        print "{}\t{}\t{}".format(edge[0], edge[1], 1)

    print "-1\t-1\t-1"

def generate_ndds(n1, n2, p):
    """Generate a .ndds instance, printing to standard output.

    Args:
        n1: Number of NDDs 
        n2: Number of patient-donor pairs
        p: Edge probability
    """

    edges = []
    for i in range(n1):
        for j in range(n2):
            if random.random() < p:
                edges.append((i, j))

    print "{}\t{}".format(n1, len(edges))
    for edge in edges:
        # Print source NDD, target patient-donor pair, weight
        print "{}\t{}\t{}".format(edge[0], edge[1], 1)

    print "-1\t-1\t-1"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Generate a kidney-exchange instance.")

    parser.add_argument("patient_count", type=int,
                        help="number of patient-donor pairs")
    parser.add_argument("ndd_count", type=int,
                        help="number of non-directed donors")
    parser.add_argument("p", type=float,
                        help="edge-existence probability")

    args = parser.parse_args()

    if args.patient_count < 1:
        raise ValueError("Patient count should be greater than zero.")
    if args.ndd_count < 0:
        raise ValueError("NDD count should not be negative.")
    if not 0 < args.p <= 1:
        raise ValueError("p should be in the range (0, 1]")

    generate_input(args.patient_count, args.p)
    generate_ndds(args.ndd_count, args.patient_count, args.p)
