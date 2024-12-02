import csv
import os

def load_csv(file: str, delimiter: str) -> tuple[list[str], list[list[str]]]:
    with open(os.path.join('csv', file), newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
        data = []
        for row in spamreader:
            data.append(row)

        return data[:1][0], data[1:]


def write_csv(file: str, data: list[list[str]], header:list[str], delimiter=',') -> None:
    with open(os.path.join('export', f'{file}.csv'), 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=delimiter)
        csv_writer.writerow(header)
        csv_writer.writerows([row for row in data])



if __name__ == '__main__':
    header, data = load_csv('test.csv', ',')
    print(header)
    [print(row) for row in data]

    write_csv('out', data, header)