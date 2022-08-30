import argparse
import fasta

def main():
    argparser = argparse.ArgumentParser(
        description="Extract Simple-FASTA records"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()
    
    out = fasta.fasta_parse(args.fasta)

    for o in out:
        print("\t".join(o))


if __name__ == '__main__':
    main()
