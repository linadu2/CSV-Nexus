import os
import cmd
from lib import *

class NoCSVFileFound(Exception):
    pass


def print_aligned_data(data, header):
    """script based on a StockOverflow topic: https://stackoverflow.com/questions/9989334/create-nice-column-output-in-python"""
    # Define column widths
    col_widths = [len(title)+5 for title in header]

    print(" | ".join(f"{h:<{w}}" for h, w in zip(header, col_widths)))
    print("-" * (sum(col_widths) + 12))  # Adjust separator length for alignment

    # Print each row with alignment
    for row in data:
        print(" | ".join(f"{str(item):<{w}}" for item, w in zip(row, col_widths)))


class CsvNexusShell(cmd.Cmd):
    intro = 'Welcome to CSV-Nexus Shell - type help or ? for commands.\n'
    prompt = 'CSV-Nexus: '

    def __init__(self):
        super().__init__()
        self.data = []
        self.header = []

    def do_exit(self, line):
        """Exit CSV-Nexus."""
        return True

    def do_add(self, line):
        """add a csv file to merge into the current dataset"""
        csv_file = [file for file in os.listdir('.') if file.endswith('.csv')]
        if not csv_file:
            raise NoCSVFileFound()
        [print(f'{x+1}. {file}') for x, file in enumerate(csv_file)]
        choix = -1
        while choix not in range(1, len(csv_file) + 1):
            choix = input('Number of the file to add: ')
            try:
                choix = int(choix)
            except ValueError:
                choix = -1
        h, d = load_csv(csv_file[choix - 1])
        if not self.header:
            self.header = h
            self.data += d
        else:
            if equality_check(h, self.header):
                self.data += d
            else:
                raise AttributeError('header does not match between csv file')

    def do_view(self, line):
        """show the current dataset"""
        print_aligned_data(self.data, self.header)

    def do_sort(self, line):
        """sort the current dataset"""
        [print(f'{x+1}. {column}') for x, column in enumerate(self.header)]
        choix = -1
        while choix not in range(1, len(self.header) + 1):
            choix = input('Number of the column to sort: ')
            try:
                choix = int(choix)
            except ValueError:
                choix = -1

        is_reverse = None
        while is_reverse != 'y' and is_reverse != 'n':
            is_reverse = input('reverse the sort ?(y/n): ')
        is_reverse = True if choix == 'y' else False

        self.data = sort_data(self.data, self.header, self.header[choix - 1], reverse=is_reverse)

    def do_export(self, line):
        """export the current dataset"""
        choix = input('Name of the file to export: ')
        if choix.endswith('.csv'):
            write_csv(choix, self.data, self.header)
        else:
            raise AttributeError('file does not have the correct extension')

if __name__ == '__main__':
    CsvNexusShell().cmdloop()