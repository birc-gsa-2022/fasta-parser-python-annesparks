import argparse


def main():
    argparser = argparse.ArgumentParser(
        description="Extract Simple-FASTA records"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()
    
    out = []
    index = -1
    for l in args.fasta.readlines():
        if l[0] == ">":
            index += 1
            trimmed = l[1:].strip()
            out.append(trimmed + "\t")
        else:
            out[index] += l.strip()

    for o in out:
        print(o)


if __name__ == '__main__':
    main()
