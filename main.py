import csv
import os
import argparse as ag



def equality_check(arr1: list[str], arr2: list[str]) -> bool:
   if (len(arr1) != len(arr2)):
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
        header.append('region')
        temp = temp[1:]
        data = []
        data += [[row[0], float(row[1]), float(row[2]), row[3], os.path.splitext(file)[0]] for row in temp]

        #print(header)
        return header, data


def write_csv(file: str, data: list[list[str]], header:list[str], delimiter: str=',') -> None:
    print(file in os.listdir('.'))
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


def main():
    parser = ag.ArgumentParser(description='A programme to performe various operation on csv file')
    parser.add_argument('file', nargs='+')
    parser.add_argument('-o', '--output', default=None, nargs='?')
    parser.add_argument('-s', '--sort', default=None, nargs='?')

    args = parser.parse_args()

    #print(args.merge)
    #print(args.output)
    #print(args.sort)
    if args.output.endswith('.csv'):
        output_file = args.output
    else:
        raise ValueError("the output file is not a csv file")

    data = []
    header = None
    for x in args.merge:
        h, d = load_csv(x)
        if not header:
            data += d
            header = h
        else:
            if equality_check(h, header):
                data += d
            else:
                raise AttributeError('header does not match between csv file')
    #print(header)
    #[print(row) for row in data]

    #print(header, args.sort )
    if args.sort in header:
        print(header.index(args.sort))
        data = sorted(data, key=lambda x: x[header.index(args.sort)])
        [print(row) for row in data]
    else:
        raise ValueError('the sort parameter don\'t match a colone')

    if output_file:
        write_csv(output_file, data, header)




if __name__ == '__main__':
    main()