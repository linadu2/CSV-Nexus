import csv
import os

def equality_check(arr1: list[str], arr2: list[str]) -> bool:
   if (len(arr1) != len(arr2)):
      return False
   arr1.sort()
   arr2.sort()
   for i in range(0, len(arr2)):
      if arr1[i] != arr2[i]:
         return False
   return True



def load_csv(file: str, delimiter: str='s') -> tuple[list[str], list[list[str]]]:
    if f"{file}.csv" not in os.listdir('.'):
        raise AttributeError("csv file not in the directory")
    with open(f'{file}.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
        data = []
        for row in spamreader:
            data.append(row)

        return data[:1][0], data[1:]


def write_csv(file: str, data: list[list[str]], header:list[str], delimiter: str=',') -> None:
    print(f'{file}.csv' in os.listdir('.'))
    if f'{file}.csv' in os.listdir('.'):
        choix = None
        while choix != 'yes' and choix != 'n':
            choix = input('warning file exist, would you overwrite it ? (yes/n)')
            print(choix)
        if choix == 'n':
            return

    with open(f'{file}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=delimiter)
        csv_writer.writerow(header)
        csv_writer.writerows(data)


def main():
    pass



if __name__ == '__main__':
    main()