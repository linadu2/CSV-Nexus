import csv
import os
import argparse as ag



def equality_check(arr1: list[str], arr2: list[str]) -> bool:
   if len(arr1) != len(arr2):
      return False
   for i in range(0, len(arr2)):
      if arr1[i] != arr2[i]:
         return False
   return True



def load_csv(file: str, delimiter: str=',') -> tuple[list[str], list[list[str]]]:
    if file not in os.listdir('.'):
        raise FileNotFoundError("csv file not in the directory")
    with open(file, newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
        temp = []
        for row in spamreader:
            temp.append(row)
        header = temp[:1][0]
        header.append('département')
        temp = temp[1:]
        data = []
        data += [[row[0], float(row[1]), float(row[2]), row[3], os.path.splitext(file)[0]] for row in temp]

        #print(header)
        return header, data


def write_csv(file: str, data: list[list[str]], header:list[str], delimiter: str=',', force_overwrite: bool= False) -> None:
    #print(file in os.listdir('.'))
    if not force_overwrite:
        if file in os.listdir('.'):
            choix = None
            while choix != 'yes' and choix != 'n':
                choix = input('warning file exist, would you overwrite it ? (yes/n)')
            if choix == 'n':
                return

    with open(file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=delimiter)
        csv_writer.writerow(header)
        csv_writer.writerows(data)


def merge_csv(file, data, header):
    for x in file:
        h, d = load_csv(x)
        if not header:
            data += d
            header = h
        else:
            if equality_check(h, header):
                data += d
            else:
                raise AttributeError('header does not match between csv file')
    return header, data


def sort_data(data, header, column):
    if column in header:
        print(header.index(column))
        data = sorted(data, key=lambda x: x[header.index(column)])
        [print(row) for row in data]
    else:
        raise ValueError('the sort parameter don\'t match a colone')

    return data


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