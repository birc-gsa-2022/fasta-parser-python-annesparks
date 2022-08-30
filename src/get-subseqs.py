import argparse
import sys


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

    coords = [l.split() for l in args.coords.readlines()]
        
    names = []
    out = []
    index = -1
    for l in args.fasta.readlines():
        if l[0] == ">":
            index += 1
            trimmed = l[1:].strip()
            names.append(trimmed)
            out.append("")
        else:
            out[index] += l.strip()
    
    for c in coords:
        index = names.index(c[0])
        print(out[index][int(c[1])-1:int(c[2])-1])


if __name__ == '__main__':
    main()
