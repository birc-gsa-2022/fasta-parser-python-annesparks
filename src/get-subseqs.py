import argparse
import sys
import fasta

def main():
    argparser = argparse.ArgumentParser(
        description="Extract sub-sequences from a Simple-FASTA file"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    argparser.add_argument(
        "coords",
        nargs="?",
        type=argparse.FileType('r'),
        default=sys.stdin
    )
    args = argparser.parse_args()

    coords = [l.split() for l in args.coords if l]
    out = fasta.fasta_parse(args.fasta)
    for c in coords:
        e = next(o for o in out if o[0] == c[0])
        print(e[1][int(c[1])-1:int(c[2])-1])


if __name__ == '__main__':
    main()
