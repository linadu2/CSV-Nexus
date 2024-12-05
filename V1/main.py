import argparse as ag
from lib import *


def main():
    parser = ag.ArgumentParser(description='A programme to performe various operation on csv file', prog='CSV-Nexus')
    parser.add_argument('file', nargs='+', help='the file to load in the programme, if multiple file is given it will be merge')
    parser.add_argument('-o', '--output', default=None, nargs='?', help='a output file if you want to save the result in a csv file')
    parser.add_argument('-s', '--sort', default=None, nargs='?', help='a column to sort the data')
    parser.add_argument('--force-overwrite', action='store_true', help='to force the overwrite if the output file exist')

    args = parser.parse_args()

    #print(args.merge)
    #print(args.output)
    #print(args.sort)
    #print(args.force_overwrite)
    if args.output:
        if not args.output.endswith('.csv'):
            raise ValueError("the output file is not a csv file")

    data = []
    header = None
    if len(args.file) > 1:
        header, data = merge_csv(args.file, data, header)
    else:
        header, data = load_csv(args.file[0])

    #print(header)
    #[print(row) for row in data]

    #print(header, args.sort )

    if args.sort:
        data = sort_data(data, header, args.sort)

    if args.output:
        write_csv(args.output, data, header, force_overwrite = args.force_overwrite)
    else:
        print(header)
        [print(row) for row in data]




if __name__ == '__main__':
    main()