""" 
CSV Datei

data.csv einlesen und ausgeben
"""
import csv
from pathlib import Path 
current_dir = Path(__file__).parent

NAME = 0 
AMOUNT = 1

def csv_reader(filename):
    # clean_rows = []
    with open(current_dir / filename, mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        header = next(reader) # Username,Amount
        yield header
        for row in reader:
            # clean_rows.append(
                yield [
                    row[NAME],
                    int(row[AMOUNT]),
                ]
            #)

    #return clean_rows


result = csv_reader("data.csv")
print(list(result))